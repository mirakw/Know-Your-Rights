"""
Gemini API Client
Shared client for all Gemini calls.
"""

import logging
import requests
from typing import Optional

logger = logging.getLogger(__name__)

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MODEL = "gemini-2.5-flash"


class GeminiClient:

    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_MODEL):
        self.api_key = api_key
        self.model = model

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def ask(self, prompt: str, temperature: float = 0.0, max_tokens: int = 16384) -> str:
        url = f"{GEMINI_API_URL}/{self.model}:generateContent?key={self.api_key}"

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
                "topP": 0.8,
            }
        }

        response = requests.post(url, json=payload, timeout=90)
        response.raise_for_status()
        data = response.json()

        candidates = data.get("candidates", [])
        if candidates:
            content = candidates[0].get("content", {})
            parts = content.get("parts", [])
            for part in reversed(parts):
                if "text" in part:
                    return part["text"]
            raise ValueError(
                f"Empty response - finish reason: "
                f"{candidates[0].get('finishReason', 'unknown')}"
            )

        raise ValueError("No candidates in Gemini response")
