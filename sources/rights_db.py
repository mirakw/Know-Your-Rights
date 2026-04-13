"""
Rights Database
Built-in knowledge base of common legal rights organized by category.
Provides immediate answers before any API calls.
"""


class RightsDatabase:
    """Curated database of rights by category with legal basis."""

    def __init__(self):
        self.rights = {
            "tenant_rights": [
                {
                    "right": "Right to habitable housing",
                    "description": "Your landlord must maintain the property in a livable condition, including working plumbing, heating, electricity, and structural safety.",
                    "legal_basis": "Implied warranty of habitability (state law varies)",
                    "what_to_do": "Document the issue with photos and dates. Send written notice to your landlord requesting repair. If they don't fix it, you may be able to withhold rent or repair-and-deduct depending on your state."
                },
                {
                    "right": "Right to privacy",
                    "description": "Your landlord cannot enter your apartment without reasonable notice, except in emergencies. Most states require 24-48 hours notice.",
                    "legal_basis": "State landlord-tenant statutes (typically 24-48 hour notice required)",
                    "what_to_do": "If your landlord entered without notice, document what happened. Send a written letter stating they violated your right to quiet enjoyment. If it continues, it may constitute harassment."
                },
                {
                    "right": "Protection from retaliation",
                    "description": "Your landlord cannot evict you, raise rent, or reduce services because you complained about conditions, reported code violations, or exercised your legal rights.",
                    "legal_basis": "Anti-retaliation statutes (most states)",
                    "what_to_do": "Keep records of your complaint and any negative actions taken after. If you believe you're being retaliated against, contact your local tenant rights organization or legal aid."
                },
                {
                    "right": "Security deposit protections",
                    "description": "Your landlord must return your security deposit within a set timeframe after you move out, minus legitimate deductions for damage beyond normal wear and tear.",
                    "legal_basis": "State security deposit laws (timeframes vary by state)",
                    "what_to_do": "Take photos when you move in and out. Request an itemized list of deductions. If your landlord wrongfully withholds your deposit, you may be able to sue in small claims court for the deposit plus penalties."
                },
            ],
            "police_encounter": [
                {
                    "right": "Right to remain silent (5th Amendment)",
                    "description": "You have the right to refuse to answer police questions. You cannot be punished for staying silent. Say clearly: 'I am exercising my right to remain silent.'",
                    "legal_basis": "Fifth Amendment to the U.S. Constitution; Miranda v. Arizona, 384 U.S. 436 (1966)",
                    "what_to_do": "Clearly state you are exercising your right to remain silent. Do not argue, resist, or flee. You must provide your name and ID if asked in most states (stop-and-identify laws)."
                },
                {
                    "right": "Right against unreasonable search (4th Amendment)",
                    "description": "Police generally need a warrant or your consent to search you, your car, or your home. You can refuse consent to a search.",
                    "legal_basis": "Fourth Amendment to the U.S. Constitution; Terry v. Ohio, 392 U.S. 1 (1968); Riley v. California, 573 U.S. 373 (2014)",
                    "what_to_do": "Say clearly: 'I do not consent to a search.' Do not physically resist. If they search anyway, do not interfere but make a note of what happened. Challenge the search later in court."
                },
                {
                    "right": "Right to an attorney (6th Amendment)",
                    "description": "If you are arrested, you have the right to an attorney. If you cannot afford one, one will be appointed. Say: 'I want a lawyer.'",
                    "legal_basis": "Sixth Amendment to the U.S. Constitution; Gideon v. Wainwright, 372 U.S. 335 (1963)",
                    "what_to_do": "Say clearly: 'I want a lawyer.' After invoking this right, police must stop questioning you. Do not answer any more questions until your attorney is present."
                },
                {
                    "right": "Right to record police",
                    "description": "You have the right to record police officers performing their duties in public. This is protected by the First Amendment.",
                    "legal_basis": "First Amendment; multiple federal circuit court rulings",
                    "what_to_do": "You can record from a safe distance. Do not interfere with their duties. If they tell you to stop recording, you can calmly state it is your First Amendment right but do not escalate."
                },
                {
                    "right": "Right to be free from excessive force",
                    "description": "Police may only use force that is objectively reasonable given the circumstances. Excessive force violates the Fourth Amendment.",
                    "legal_basis": "Fourth Amendment; Graham v. Connor, 490 U.S. 386 (1989); 42 U.S.C. § 1983",
                    "what_to_do": "Do not resist physically even if force seems excessive. Document everything after: injuries, witnesses, badge numbers. File a complaint with internal affairs. Consult an attorney about a Section 1983 civil rights claim."
                },
                {
                    "right": "Right to refuse a cell phone search",
                    "description": "Police cannot search the contents of your cell phone without a warrant, even during an arrest.",
                    "legal_basis": "Fourth Amendment; Riley v. California, 573 U.S. 373 (2014)",
                    "what_to_do": "Say: 'I do not consent to a search of my phone.' Lock your phone. If they take it anyway, do not provide your passcode. Challenge the search through your attorney."
                },
            ],
            "workplace_rights": [
                {
                    "right": "Right to a safe workplace",
                    "description": "Your employer must provide a workplace free from recognized hazards that could cause death or serious harm.",
                    "legal_basis": "Occupational Safety and Health Act (OSHA), 29 U.S.C. § 654",
                    "what_to_do": "Report unsafe conditions to your employer in writing. If they don't fix it, file a complaint with OSHA. You have the right to refuse work that poses imminent danger."
                },
                {
                    "right": "Right to be paid fairly",
                    "description": "You must be paid at least minimum wage and receive overtime pay (1.5x) for hours over 40 per week, unless you are exempt.",
                    "legal_basis": "Fair Labor Standards Act (FLSA), 29 U.S.C. § 206-207",
                    "what_to_do": "Keep your own records of hours worked. If you're being shorted, file a complaint with your state labor board or the federal Department of Labor. You can recover back wages plus penalties."
                },
                {
                    "right": "Protection from discrimination",
                    "description": "You cannot be fired, demoted, or harassed based on race, color, religion, sex, national origin, age (40+), disability, or genetic information.",
                    "legal_basis": "Title VII of the Civil Rights Act; Age Discrimination in Employment Act; Americans with Disabilities Act",
                    "what_to_do": "Document discriminatory actions with dates, witnesses, and communications. Report to HR in writing. If unresolved, file a charge with the EEOC within 180 days (300 days in some states)."
                },
                {
                    "right": "Whistleblower protection",
                    "description": "You cannot be fired or retaliated against for reporting illegal activity, safety violations, fraud, or other wrongdoing by your employer.",
                    "legal_basis": "Whistleblower Protection Act; Sarbanes-Oxley Act (public companies); state whistleblower laws",
                    "what_to_do": "Document the wrongdoing and your report of it. Report through proper channels first. If retaliated against, file a complaint with OSHA (for safety) or the SEC (for financial fraud)."
                },
                {
                    "right": "Right to medical and family leave",
                    "description": "If your employer has 50+ employees, you may take up to 12 weeks unpaid leave for serious health conditions, childbirth, or caring for a family member.",
                    "legal_basis": "Family and Medical Leave Act (FMLA), 29 U.S.C. § 2601",
                    "what_to_do": "Notify your employer 30 days in advance when possible. Your job (or an equivalent one) must be held for you. If denied, file a complaint with the Department of Labor."
                },
            ],
            "consumer_rights": [
                {
                    "right": "Protection from debt collector harassment",
                    "description": "Debt collectors cannot call you at unreasonable hours, threaten you, use profane language, or misrepresent the debt. They must stop contacting you if you request it in writing.",
                    "legal_basis": "Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692",
                    "what_to_do": "Send a written cease-and-desist letter. Request debt validation in writing within 30 days. If they violate the FDCPA, you can sue for damages plus attorney fees."
                },
                {
                    "right": "Right to accurate credit reporting",
                    "description": "Credit bureaus must report accurate information. You can dispute errors and they must investigate within 30 days.",
                    "legal_basis": "Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681",
                    "what_to_do": "Pull your free credit report from annualcreditreport.com. Dispute errors in writing with the credit bureau. They have 30 days to investigate and respond."
                },
            ],
            "digital_privacy": [
                {
                    "right": "Right to privacy in cell phone data",
                    "description": "The government needs a warrant to search your cell phone contents or access your historical location data from your carrier.",
                    "legal_basis": "Fourth Amendment; Riley v. California, 573 U.S. 373 (2014); Carpenter v. United States, 585 U.S. 296 (2018)",
                    "what_to_do": "Do not consent to searches of your devices. Use a passcode (not just biometrics, as courts are split on whether you can be compelled to use a fingerprint). If your data was accessed without a warrant, challenge it through your attorney."
                },
                {
                    "right": "Right to know about data breaches",
                    "description": "Companies must notify you if your personal data is compromised in a breach.",
                    "legal_basis": "State data breach notification laws (all 50 states have them)",
                    "what_to_do": "Change passwords immediately. Place a fraud alert or credit freeze with the three credit bureaus. Monitor your accounts for unauthorized activity."
                },
            ],
            "housing_discrimination": [
                {
                    "right": "Protection from housing discrimination",
                    "description": "Landlords, lenders, and real estate agents cannot discriminate based on race, color, national origin, religion, sex, familial status, or disability.",
                    "legal_basis": "Fair Housing Act, 42 U.S.C. § 3601; Civil Rights Act of 1866",
                    "what_to_do": "Document discriminatory statements or actions. File a complaint with HUD within one year. You can also file a lawsuit in federal court within two years."
                },
            ],
            "disability_rights": [
                {
                    "right": "Right to reasonable accommodations at work",
                    "description": "Your employer must provide reasonable accommodations for your disability unless it causes undue hardship.",
                    "legal_basis": "Americans with Disabilities Act (ADA), 42 U.S.C. § 12101",
                    "what_to_do": "Request accommodations in writing. You do not need to disclose your full diagnosis, just the functional limitations. If denied, file a charge with the EEOC."
                },
                {
                    "right": "Right to access public spaces",
                    "description": "Public businesses and government buildings must be accessible to people with disabilities.",
                    "legal_basis": "Americans with Disabilities Act (ADA), Titles II and III",
                    "what_to_do": "If a business is inaccessible, you can file a complaint with the DOJ or bring a private lawsuit. Many states also have accessibility laws with additional protections."
                },
            ],
        }

    def get_rights_for_categories(self, categories: list) -> list:
        """Get all rights matching the given categories."""
        results = []
        for cat in categories:
            cat_lower = cat.lower().strip()
            if cat_lower in self.rights:
                for right in self.rights[cat_lower]:
                    right_copy = dict(right)
                    right_copy["category"] = cat_lower
                    results.append(right_copy)
        return results

    def get_all_categories(self) -> list:
        return list(self.rights.keys())

    def search(self, query: str) -> list:
        """Search across all rights for keyword matches."""
        query_lower = query.lower()
        results = []
        for cat, rights_list in self.rights.items():
            for right in rights_list:
                text = (right["right"] + " " + right["description"] + " " +
                        right["legal_basis"]).lower()
                if any(word in text for word in query_lower.split() if len(word) > 3):
                    right_copy = dict(right)
                    right_copy["category"] = cat
                    results.append(right_copy)
        return results
