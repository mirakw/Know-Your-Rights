"""
Rights Advisor (Step 3)
Takes the situation, analysis, and fetched rights/cases and produces
a clear, plain-language answer with:
  - Short answer (TLDR)
  - Your rights (what protections you have)
  - The law (cases and statutes that back it up)
  - What to do next (concrete action steps)
  - Strength assessment (how strong is your position)
"""

import logging

logger = logging.getLogger(__name__)


class RightsAdvisor:

    def __init__(self, gemini_client):
        self.gemini = gemini_client

    def advise(self, situation: str, analysis: dict, fetched: dict) -> dict:
        """Generate plain-language rights advice."""
        rights_text = self._format_rights(fetched.get("rights_from_db", []))
        cases_text = self._format_cases(fetched.get("relevant_cases", []))
        laws_text = ", ".join(fetched.get("relevant_laws", []))

        prompt = f"""You are a legal rights advisor helping an everyday person understand their rights. They are NOT a lawyer. Use plain language. Be direct and practical.

THEIR SITUATION:
{situation}

KEY ISSUES IDENTIFIED:
{', '.join(analysis.get('key_issues', []))}

RIGHTS FROM DATABASE (these are verified):
{rights_text if rights_text else "None found in database."}

RELEVANT COURT CASES:
{cases_text if cases_text else "None identified."}

RELEVANT LAWS:
{laws_text if laws_text else "None identified."}

Now produce EXACTLY these five sections with these EXACT headers. Write for someone with no legal background.

## SHORT ANSWER
2-3 sentences answering "what are my rights here?" in the most direct way possible. No legal jargon.

## YOUR RIGHTS
List each right that applies to their situation. For each one:
- What the right is (one sentence, plain language)
- What it means for THEIR specific situation

Only include rights that are actually relevant. Use the database rights above as your source, but explain them in simpler terms.

## THE LAW
For each relevant law or court case, explain in one sentence what it says and why it matters here. Format:

**Law/Case Name** (citation if available)
What it means for you: one plain-language sentence.

Include both laws from the database AND the court cases. Mark anything not from the provided data with: ⚠️ General legal knowledge

## WHAT TO DO NEXT
Numbered list of concrete action steps they should take, in order. Be specific. Include:
- What to do right now (today)
- What to document
- Who to contact (specific organizations, not just "a lawyer")
- Deadlines they should know about

## STRENGTH
One short paragraph assessing how strong their position is. Be honest. If their situation is clear-cut, say so. If it depends on state law or specific facts, say that too. End with whether they should consult an attorney."""

        try:
            response = self.gemini.ask(prompt, temperature=0.0, max_tokens=8192)
            return self._parse(response)
        except Exception as e:
            logger.error(f"Advisor error: {e}")
            return {
                "short_answer": f"Error generating advice: {e}",
                "your_rights": rights_text,
                "the_law": "",
                "what_to_do": "Consult a local attorney or legal aid organization.",
                "strength": "",
            }

    def _parse(self, text: str) -> dict:
        sections = {
            "short_answer": "",
            "your_rights": "",
            "the_law": "",
            "what_to_do": "",
            "strength": "",
        }

        markers = [
            ("SHORT ANSWER", "short_answer"),
            ("YOUR RIGHTS", "your_rights"),
            ("THE LAW", "the_law"),
            ("WHAT TO DO", "what_to_do"),
            ("STRENGTH", "strength"),
        ]

        current_key = None
        current_lines = []

        for line in text.split("\n"):
            stripped = line.strip().lstrip("#").strip()
            stripped_upper = stripped.upper()

            matched = False
            for keyword, key in markers:
                if stripped_upper.startswith(keyword):
                    if current_key:
                        sections[current_key] = "\n".join(current_lines).strip()
                    current_key = key
                    current_lines = []
                    matched = True
                    break

            if not matched and current_key:
                current_lines.append(line)

        if current_key:
            sections[current_key] = "\n".join(current_lines).strip()

        # Fallback
        if not any(sections.values()):
            sections["short_answer"] = text[:300]
            sections["your_rights"] = text

        return sections

    def _format_rights(self, rights: list) -> str:
        if not rights:
            return ""
        lines = []
        for r in rights:
            entry = f"RIGHT: {r['right']}"
            entry += f"\n  {r['description']}"
            entry += f"\n  Legal basis: {r['legal_basis']}"
            entry += f"\n  Action: {r['what_to_do']}"
            lines.append(entry + "\n")
        return "\n".join(lines)

    def _format_cases(self, cases: list) -> str:
        if not cases:
            return ""
        lines = []
        for c in cases:
            name = c.get("name", "Unknown")
            citation = c.get("citation", "")
            one_liner = c.get("one_liner", "")
            entry = f"{name}"
            if citation:
                entry += f", {citation}"
            if one_liner:
                entry += f"\n  {one_liner}"
            lines.append(entry)
        return "\n".join(lines)
