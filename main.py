"""
Know Your Rights — Terminal Version
Describe your situation in plain language. Get your rights, the law behind them,
and what to do next.

Usage: python main.py
"""

import warnings
warnings.filterwarnings("ignore", message="urllib3 v2 only supports")

import os
import sys
import textwrap
from dotenv import load_dotenv

from pipeline.gemini_client import GeminiClient
from pipeline.analyzer import SituationAnalyzer
from pipeline.fetcher import RightsFetcher
from pipeline.advisor import RightsAdvisor
from sources.rights_db import RightsDatabase

load_dotenv()

# ── Colors ──────────────────────────────────────────────────────────
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
LINE = "─" * 70


def wrap(text, indent=2):
    lines = text.split("\n")
    result = []
    for line in lines:
        if line.strip():
            wrapped = textwrap.fill(line.strip(), width=68,
                                    initial_indent=" " * indent,
                                    subsequent_indent=" " * indent)
            result.append(wrapped)
        else:
            result.append("")
    return "\n".join(result)


def main():
    gemini = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))
    rights_db = RightsDatabase()

    analyzer = SituationAnalyzer(gemini)
    fetcher = RightsFetcher(gemini, rights_db)
    advisor = RightsAdvisor(gemini)

    # Header
    print(f"\n{BOLD}{BLUE}{'═' * 70}{RESET}")
    print(f"{BOLD}{BLUE}  🛡️  Know Your Rights{RESET}")
    print(f"{DIM}  Describe your situation. Get your rights and next steps.{RESET}")
    print(f"{BOLD}{BLUE}{'═' * 70}{RESET}")

    if not gemini.is_configured():
        print(f"\n  {YELLOW}⚠ Missing GEMINI_API_KEY in .env{RESET}")
        print(f"  {DIM}Get a free key at https://aistudio.google.com/apikey{RESET}")
        return

    # Examples
    print(f"\n{DIM}  Try things like:{RESET}")
    print(f"{DIM}  • \"My landlord entered my apartment without telling me\"{RESET}")
    print(f"{DIM}  • \"A cop searched my car during a traffic stop without asking\"{RESET}")
    print(f"{DIM}  • \"My employer hasn't paid me overtime in 3 months\"{RESET}")
    print(f"{DIM}  • \"I got fired after reporting safety violations\"{RESET}")

    # Main loop
    while True:
        print(f"\n{CYAN}  Describe your situation (or 'quit'):{RESET}")
        situation = input(f"  {BOLD}> {RESET}").strip()

        if not situation:
            continue
        if situation.lower() in ("quit", "exit", "q"):
            print(f"\n  {DIM}Goodbye!{RESET}\n")
            break

        research(situation, analyzer, fetcher, advisor)


def research(situation, analyzer, fetcher, advisor):
    """Three-step pipeline."""

    # Step 1: Analyze the situation
    print(f"\n{DIM}  [1/3] Analyzing your situation...{RESET}", end="", flush=True)
    analysis = analyzer.analyze(situation)
    print(f" ✓{RESET}")

    categories = analysis.get("categories", [])
    if categories:
        print(f"  {GREEN}Identified areas: {', '.join(categories)}{RESET}")

    rights_needed = analysis.get("rights", [])
    if rights_needed:
        print(f"  {GREEN}Key rights to research: {len(rights_needed)}{RESET}")

    # Step 2: Fetch relevant rights, laws, and cases
    print(f"\n{DIM}  [2/3] Looking up your rights and relevant law...{RESET}",
          end="", flush=True)
    fetched = fetcher.fetch(analysis)
    print(f" ✓{RESET}")

    db_rights = len(fetched.get("rights_from_db", []))
    cases = len(fetched.get("relevant_cases", []))
    print(f"  {GREEN}Found: {db_rights} rights, {cases} supporting cases{RESET}")

    # Step 3: Generate plain-language advice
    print(f"\n{DIM}  [3/3] Generating your rights summary...{RESET}",
          end="", flush=True)
    result = advisor.advise(situation, analysis, fetched)
    print(f" ✓{RESET}")

    display(result)


def display(result):
    """Print the final output."""

    # TLDR
    print(f"\n{BOLD}{YELLOW}{'─' * 70}{RESET}")
    print(f"{BOLD}{YELLOW}  💡 THE SHORT ANSWER{RESET}")
    print(f"{BOLD}{YELLOW}{'─' * 70}{RESET}")
    print(wrap(result.get("short_answer", "No summary available.")))
    print(f"{BOLD}{YELLOW}{'─' * 70}{RESET}")

    # Your Rights
    rights_text = result.get("your_rights", "")
    if rights_text:
        print(f"\n{BOLD}{CYAN}  🛡️  YOUR RIGHTS{RESET}")
        print(f"{DIM}  {LINE}{RESET}")
        print(wrap(rights_text))

    # The Law
    law_text = result.get("the_law", "")
    if law_text:
        print(f"\n{BOLD}{CYAN}  📜 THE LAW BEHIND IT{RESET}")
        print(f"{DIM}  {LINE}{RESET}")
        print(wrap(law_text))

    # What To Do
    steps_text = result.get("what_to_do", "")
    if steps_text:
        print(f"\n{BOLD}{GREEN}  ✅ WHAT TO DO NEXT{RESET}")
        print(f"{DIM}  {LINE}{RESET}")
        print(wrap(steps_text))

    # Strength Assessment
    strength_text = result.get("strength", "")
    if strength_text:
        print(f"\n{BOLD}{DIM}  📊 HOW STRONG IS YOUR POSITION{RESET}")
        print(f"{DIM}  {LINE}{RESET}")
        print(wrap(strength_text))

    print(f"\n{DIM}  {'─' * 70}{RESET}")
    print(f"{DIM}  ⚠️  This is general legal information, not legal advice.{RESET}")
    print(f"{DIM}  Consult an attorney for your specific situation.{RESET}")


if __name__ == "__main__":
    main()
