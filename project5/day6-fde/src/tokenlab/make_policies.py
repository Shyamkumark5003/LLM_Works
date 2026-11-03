from pathlib import Path

# (topic, rule, number, how to apply, exception)
POLICIES = [
    (
        "Annual Leave",
        "Every employee gets paid annual leave",
        "20 days per year",
        "Apply on the HR portal at least 7 days before",
        "Leave cannot be carried over after March 31",
    ),
    (
        "Sick Leave",
        "Employees can take paid sick leave",
        "10 days per year",
        "Inform your manager before 10 AM on the same day",
        "A medical certificate is needed after 2 continuous days",
    ),
    (
        "Remote Work",
        "Employees may work from home",
        "2 days per week",
        "Get approval from your manager every month",
        "New joiners must work from office for the first 90 days",
    ),
    (
        "Expense Claims",
        "Business expenses are reimbursed",
        "within 15 working days",
        "Upload bills in the finance portal",
        "Claims older than 30 days are rejected",
    ),
    (
        "Travel",
        "Flights are booked only through the company travel desk",
        "economy class for trips under 6 hours",
        "Raise a travel request 5 days before",
        "Hotel limit is 6000 rupees per night",
    ),
    (
        "Laptop Use",
        "Every employee gets one company laptop",
        "replaced every 4 years",
        "Raise an IT ticket for any fault",
        "Personal software must not be installed",
    ),
    (
        "Password",
        "All passwords must be strong",
        "minimum 12 characters",
        "Change the password every 90 days",
        "Never share passwords, even with the IT team",
    ),
    (
        "Data Privacy",
        "Customer data is confidential",
        "retained for 5 years only",
        "Store it only in approved company systems",
        "Sharing customer data on personal email is a serious violation",
    ),
    (
        "Dress Code",
        "Employees follow smart casual dress",
        "formal wear on client visit days",
        "Check the weekly calendar for client visits",
        "Casual wear is allowed on Fridays",
    ),
    (
        "Working Hours",
        "Standard working time is",
        "9 hours per day including lunch",
        "Core hours are 11 AM to 4 PM",
        "Flexible start time between 8 AM and 10 AM",
    ),
    (
        "Overtime",
        "Overtime must be approved earlier",
        "maximum 20 hours per month",
        "Manager approves in the time tracking tool",
        "Overtime is paid as compensatory leave, not cash",
    ),
    (
        "Training Budget",
        "Each employee gets a learning budget",
        "30000 rupees per year",
        "Submit the course link to HR for approval",
        "Unused budget is not carried forward",
    ),
    (
        "Referral Bonus",
        "Employees get a bonus for good referrals",
        "25000 rupees per hire",
        "Submit the candidate on the referral portal",
        "Bonus is paid after the new hire completes 6 months",
    ),
    (
        "Public Holidays",
        "The company follows a fixed holiday list",
        "12 public holidays per year",
        "The list is published every January",
        "Employees may swap 2 holidays for local festivals",
    ),
    (
        "Resignation",
        "Employees must give notice before leaving",
        "60 days notice period",
        "Send the resignation email to manager and HR",
        "Notice can be shortened only with director approval",
    ),
    (
        "Visitor Access",
        "All visitors must be registered",
        "valid for one day only",
        "The host employee creates the visitor pass",
        "Visitors must always wear a badge and be escorted",
    ),
    (
        "Incident Reporting",
        "Security incidents must be reported",
        "within 24 hours",
        "Email the security team or call the helpline",
        "Do not try to fix the incident yourself",
    ),
    (
        "Software Install",
        "Only approved software can be installed",
        "from the company software catalog",
        "Raise an IT request for new software",
        "Free tools also need security approval",
    ),
    (
        "Parental Leave",
        "New parents get paid parental leave",
        "26 weeks for mothers and 2 weeks for fathers",
        "Inform HR at least 30 days before the due date",
        "Leave can be taken in two parts",
    ),
    (
        "Performance Review",
        "Reviews happen twice a year",
        "in June and December",
        "Fill the self review form 1 week before",
        "Ratings are discussed in a one to one meeting",
    ),
]

out = Path("data/policies")
out.mkdir(parents=True, exist_ok=True)

for i, (topic, rule, number, apply, exception) in enumerate(POLICIES, start=1):
    text = (
        f"{topic} Policy\n\n"
        f"{rule}: {number}. This policy applies to all full time employees of the company.\n\n"
        f"How to follow: {apply}. Please keep a record of every request for audit.\n\n"
        f"Exception: {exception}. For any doubt, contact the HR team."
    )
    slug = topic.lower().replace(" ", "_")
    (out / f"policy_{i:02d}_{slug}.txt").write_text(text, encoding="utf-8")

print("Created", len(POLICIES), "policy files")
