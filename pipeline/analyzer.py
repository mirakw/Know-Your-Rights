"""
Situation Analyzer (Step 1)
Takes a plain-language description of someone's situation and
identifies what legal categories, rights, and laws are relevant.
"""

import json
import re
import logging

logger = logging.getLogger(__name__)


class SituationAnalyzer:

    def __init__(self, gemini_client):
        self.gemini = gemini_client

    def analyze(self, situation: str) -> dict:
        prompt = f"""You are a legal rights expert. Someone is describing a situation they're in and they want to know their rights. Analyze their situation and identify what areas of law apply and what specific rights they should know about.

SITUATION:
{situation}

Respond in EXACTLY this JSON format. No markdown, no backticks, no explanation:
{{
    "categories": ["tenant_rights", "police_encounter"],
    "rights": ["Right to habitable housing", "Right to privacy in your home"],
    "relevant_laws": ["Fair Housing Act", "State landlord-tenant law"],
    "relevant_cases": ["Case v. Name if applicable"],
    "key_issues": ["Illegal entry without notice", "Potential lease violation by landlord"],
    "severity": "medium"
}}

Categories must be from this list: tenant_rights, police_encounter, workplace_rights, free_speech, consumer_rights, immigration, digital_privacy, education, criminal_defense, family_law, disability_rights, housing_discrimination

List 3-6 specific rights. List relevant federal/state laws. List any landmark cases. severity is low/medium/high based on urgency."""

        try:
            response = self.gemini.ask(prompt, temperature=0.0, max_tokens=4096)
            return self._parse(response)
        except Exception as e:
            logger.error(f"Analyzer error: {e}")
            return self._fallback(situation)

    def _parse(self, text: str) -> dict:
        text = text.strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'^```\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        text = text.strip()

        try:
            data = json.loads(text)
            return {
                "categories": data.get("categories", []),
                "rights": data.get("rights", []),
                "relevant_laws": data.get("relevant_laws", []),
                "relevant_cases": data.get("relevant_cases", []),
                "key_issues": data.get("key_issues", []),
                "severity": data.get("severity", "medium"),
            }
        except json.JSONDecodeError:
            logger.warning(f"Could not parse analyzer JSON: {text[:200]}")
            return self._fallback("")

    def _fallback(self, situation: str) -> dict:
        return {
            "categories": [],
            "rights": [],
            "relevant_laws": [],
            "relevant_cases": [],
            "key_issues": [],
            "severity": "medium",
        }
