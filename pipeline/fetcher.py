"""
Rights Fetcher (Step 2)
Takes the analysis from Step 1 and fetches:
  - Matching rights from the built-in database
  - Relevant case names from Gemini (for citation)
"""

import json
import re
import logging

logger = logging.getLogger(__name__)


class RightsFetcher:

    def __init__(self, gemini_client, rights_db):
        self.gemini = gemini_client
        self.rights_db = rights_db

    def fetch(self, analysis: dict) -> dict:
        """
        Fetch rights from database and identify supporting cases.

        Returns:
            {
                "rights_from_db": [list of matching rights],
                "relevant_cases": [list of case names with brief descriptions],
                "relevant_laws": [list of law names from analysis]
            }
        """
        # Get rights from built-in database
        categories = analysis.get("categories", [])
        db_rights = self.rights_db.get_rights_for_categories(categories)

        # Also search by key issues
        for issue in analysis.get("key_issues", []):
            search_results = self.rights_db.search(issue)
            for r in search_results:
                if r not in db_rights:
                    db_rights.append(r)

        # Get relevant cases from Gemini
        relevant_cases = self._identify_cases(analysis)

        return {
            "rights_from_db": db_rights,
            "relevant_cases": relevant_cases,
            "relevant_laws": analysis.get("relevant_laws", []),
        }

    def _identify_cases(self, analysis: dict) -> list:
        """Ask Gemini for key cases that support these rights."""
        categories = ", ".join(analysis.get("categories", []))
        rights = ", ".join(analysis.get("rights", []))
        issues = ", ".join(analysis.get("key_issues", []))

        prompt = f"""You are a legal expert. For the following legal situation, list the most important court cases that a person should know about. These should be real, landmark cases that establish or protect the rights involved.

Legal categories: {categories}
Rights at issue: {rights}
Key issues: {issues}

Respond in EXACTLY this JSON format. No markdown, no backticks:
{{
    "cases": [
        {{
            "name": "Case v. Name",
            "citation": "XXX U.S. XXX (Year)",
            "one_liner": "What this case established in one plain-language sentence"
        }}
    ]
}}

List 3-6 of the most important cases. Only real cases. Plain language for the one_liner."""

        try:
            response = self.gemini.ask(prompt, temperature=0.0, max_tokens=4096)
            return self._parse_cases(response)
        except Exception as e:
            logger.error(f"Case identification error: {e}")
            # Fall back to cases from the analysis
            return [{"name": c, "citation": "", "one_liner": ""}
                    for c in analysis.get("relevant_cases", [])]

    def _parse_cases(self, text: str) -> list:
        text = text.strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'^```\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        text = text.strip()

        try:
            data = json.loads(text)
            return data.get("cases", [])
        except json.JSONDecodeError:
            logger.warning(f"Could not parse cases JSON: {text[:200]}")
            return []
