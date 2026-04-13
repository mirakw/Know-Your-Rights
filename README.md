# 🛡️ Know Your Rights

**An AI-powered tool that takes a plain-language description of your situation and tells you your legal rights, the laws behind them, and exactly what to do next.**

> *Legal information shouldn't require a law degree to understand. People dealing with a bad landlord, an aggressive cop, or a shady employer shouldn't have to read through statutes and case law to figure out where they stand. This tool exists because everyone deserves to know their rights in language they can actually understand.*

---

## What It Does

You describe your situation in plain language. The agent:

1. **Analyzes** your situation to identify what area of law applies (tenant rights, police encounter, workplace, consumer, etc.)
2. **Looks up** your rights from a curated legal database with specific protections, legal citations, and action steps
3. **Identifies** the landmark court cases and federal laws that back up your rights
4. **Generates** a plain-language breakdown: what your rights are, what the law says, what to do next, and how strong your position is

### Example

```
> My landlord entered my apartment without telling me while I was at work

  [1/3] Analyzing your situation... ✓
  Identified areas: tenant_rights
  Key rights to research: 4

  [2/3] Looking up your rights and relevant law... ✓
  Found: 4 rights, 3 supporting cases

  [3/3] Generating your rights summary... ✓

  💡 THE SHORT ANSWER
  Your landlord likely broke the law. In most states, landlords must give
  you 24-48 hours written notice before entering your apartment, except in
  emergencies. You have the right to quiet enjoyment of your home, and
  entering without notice is a violation of that right.

  🛡️ YOUR RIGHTS
  - Right to privacy in your home: Your landlord cannot enter without
    reasonable notice (24-48 hours in most states). This applies to
    repairs, inspections, and showings.
  - Protection from retaliation: If you complain about this, your
    landlord cannot raise your rent or try to evict you in response.
  ...

  📜 THE LAW BEHIND IT
  State landlord-tenant statutes require advance notice for entry...
  ...

  ✅ WHAT TO DO NEXT
  1. Document what happened today: write down the date, time, and
     what you found when you got home.
  2. Send your landlord a written letter (email is fine) stating...
  ...

  📊 HOW STRONG IS YOUR POSITION
  This is a clear-cut violation in most states. Unauthorized entry
  without notice is well-established as a breach of quiet enjoyment...
```

---

## Quick Start

```bash
git clone https://github.com/mirakw/know-your-rights.git
cd know-your-rights

pip install -r requirements.txt
```

### Get Your API Key (free, no credit card)

| Service | Sign Up | What It Does |
|---------|---------|-------------|
| **Google Gemini** | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | Powers situation analysis, case identification, and advice generation |

### Configure and Run

```bash
cp .env.example .env
# Add your Gemini API key to .env

python main.py
```

Type your situation at the prompt. Type `quit` to exit.

---

## Architecture

The agent uses a **three-step Gemini pipeline** backed by a curated rights database. Gemini analyzes the situation, the database provides verified legal rights, and Gemini synthesizes everything into plain-language advice.

```
User Situation (plain language)
        │
        ▼
   ┌─────────────────────────────┐
   │  STEP 1: Situation Analyzer  │
   │  Gemini identifies:          │
   │  • Legal categories          │
   │  • Specific rights at issue  │
   │  • Key legal issues          │
   │  • Severity level            │
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │  STEP 2: Rights Fetcher      │
   │  • Pulls matching rights     │
   │    from built-in database    │
   │  • Gemini identifies         │
   │    landmark court cases      │
   └──────────────┬──────────────┘
                  │
        Verified rights + case law + statutes
                  │
                  ▼
   ┌─────────────────────────────┐
   │  STEP 3: Rights Advisor      │
   │  Gemini produces:            │
   │  • The Short Answer          │
   │  • Your Rights               │
   │  • The Law Behind It         │
   │  • What To Do Next           │
   │  • Strength Assessment       │
   └─────────────────────────────┘
```

### Why a Built-in Rights Database?

The rights database provides verified, accurate legal information that doesn't depend on search results or AI generation. Each entry includes the right itself, a plain-language description, the legal basis (statute or case law), and specific action steps. Gemini then takes this verified information and tailors it to the user's specific situation. This means the core legal content is grounded in real law, not generated from scratch.

---

## What It Covers

The built-in rights database covers these categories:

| Category | Examples |
|----------|---------|
| **Tenant Rights** | Habitable housing, privacy, anti-retaliation, security deposits |
| **Police Encounters** | Right to remain silent, refuse searches, request an attorney, record police, protection from excessive force, cell phone search protections |
| **Workplace Rights** | Workplace safety (OSHA), fair pay (FLSA), discrimination (Title VII), whistleblower protections, family/medical leave (FMLA) |
| **Consumer Rights** | Debt collector harassment (FDCPA), credit reporting accuracy (FCRA) |
| **Digital Privacy** | Cell phone search protections, data breach notification |
| **Housing Discrimination** | Fair Housing Act protections |
| **Disability Rights** | Reasonable accommodations (ADA), public accessibility |

---

## Output Structure

Every response follows this format:

| Section | What It Contains |
|---------|-----------------|
| **💡 The Short Answer** | 2-3 sentences directly answering "what are my rights here?" |
| **🛡️ Your Rights** | Each right that applies, explained in plain language for the specific situation |
| **📜 The Law Behind It** | Court cases and statutes with one-sentence plain-language explanations. Content not from the database is labeled "⚠️ General legal knowledge" |
| **✅ What To Do Next** | Numbered action steps: what to do today, what to document, who to contact, deadlines |
| **📊 How Strong Is Your Position** | Honest assessment of the situation and whether to consult an attorney |

---

## Sample Situations

Good starting points to test the tool:

| Situation | Tests |
|-----------|-------|
| "My landlord entered my apartment without telling me" | Tenant privacy rights, quiet enjoyment |
| "A cop searched my car during a traffic stop without asking" | 4th Amendment, consent, vehicle search exceptions |
| "My employer hasn't paid me overtime in 3 months" | FLSA, wage theft, Department of Labor |
| "I got fired after reporting safety violations" | Whistleblower protection, OSHA |
| "A debt collector keeps calling me at 6am threatening to sue" | FDCPA, debt collection harassment |
| "My employer won't let me use a standing desk for my back injury" | ADA, reasonable accommodations |
| "Police took my phone and went through it during a traffic stop" | Riley v. California, cell phone privacy |

---

## Project Structure

```
know-your-rights/
├── main.py                     # Terminal entry point (interactive loop)
├── .env.example                # Template for Gemini API key
├── requirements.txt            # Python dependencies
│
├── pipeline/                   # Three-step processing pipeline
│   ├── gemini_client.py        # Shared Gemini API wrapper (temperature=0.0)
│   ├── analyzer.py             # Step 1: Gemini analyzes the situation
│   ├── fetcher.py              # Step 2: Database lookup + case identification
│   └── advisor.py              # Step 3: Gemini generates plain-language advice
│
└── sources/
    └── rights_db.py            # Curated legal rights database by category
```

---

## Design Decisions

- **Terminal only.** No web UI. The focus is on getting the right answer to the user, not making it look pretty. This is a tool, not a product demo.
- **Built-in rights database.** The core legal content is curated and verified, not generated by AI on the fly. Gemini tailors it to the situation, but the foundation is real law.
- **Plain language first.** Every output is written for someone with zero legal background. If a sentence would confuse a non-lawyer, it doesn't belong in the output.
- **Transparency labeling.** When the system uses Gemini's general knowledge instead of the built-in database, it says so. Users always know what's verified vs. interpreted.
- **One API key.** Only Gemini is required. No CourtListener token, no Congress.gov key. The rights database handles the legal content.
- **Deterministic output.** Temperature set to 0.0 so the same situation produces the same advice every time.

---

## How This Differs from the Constitutional Law Research Agent

These are companion projects targeting different audiences:

| | Constitutional Law Research Agent | Know Your Rights |
|---|---|---|
| **Audience** | Lawyers, researchers | Everyday people |
| **Input** | Legal research questions | Plain-language situation descriptions |
| **Tone** | Professional, citations and holdings | Conversational, no jargon |
| **Data Sources** | CourtListener, SCOTUS, Congress.gov | Built-in rights database + Gemini |
| **Output** | Research memo with case analysis | Action steps and rights summary |
| **Goal** | "What does the law say?" | "What are my rights and what do I do?" |

---

## Limitations and Disclaimer

⚖️ **This is general legal information, not legal advice.** Always consult a licensed attorney for your specific situation.

- Rights and protections vary significantly by state. The database covers federal law and general principles, but your state may have stronger (or weaker) protections.
- The tool cannot assess the full context of your situation. Facts matter in law, and small details can change the outcome.
- Gemini-generated case references are based on AI knowledge and should be verified before relying on them in any legal proceeding.
- This tool does not replace an attorney. For serious situations (arrest, eviction, discrimination), consult legal aid or a local attorney.

---

## Author

**Mira Kapoor Wadehra** — AI Product Manager
[LinkedIn](https://linkedin.com/in/mira-wadehra)

Building AI tools that make legal information accessible to everyone.
