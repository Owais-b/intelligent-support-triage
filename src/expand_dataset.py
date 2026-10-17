
import csv
import random
from pathlib import Path

random.seed(42)

DATA_PATH = Path("data/support_tickets.csv")

examples = {
    "account": [
        "I want to change my personal information",
        "How can I update my profile details",
        "Please help me correct my account information",
        "I need to change the name on my account",
        "How do I edit my registered details",
        "I cannot sign in to my account",
        "Please help me change my password",
        "My user account is locked",
        "I need to recover my account",
        "I cannot update my account details",
        "Someone logged into my account",
        "My profile information is incorrect",
        "I cannot verify my account",
        "I forgot my login credentials",
        "Please help me unlock my account",
        "I cannot access my profile",
        "My account verification failed",
        "I want to change my registered email",
        "I cannot reset my password",
        "My account details are missing",
        "I am unable to log in",
        "Please help me update my username",
        "My account was accessed without permission",
        "I need help recovering my login",
        "My account is temporarily disabled",
        "I cannot change my registered phone number",
        "The account settings are not saving",
        "I have a problem with account verification",
        "I need to update my personal details",
        "I cannot open my account dashboard"
    ],
    "payment": [
        "My payment failed during checkout",
        "I have not received my refund",
        "I was charged twice for one order",
        "The amount on my bill is incorrect",
        "My card payment is not working",
        "I want to request a refund",
        "My transaction is still pending",
        "Why was I charged an extra fee",
        "The payment was deducted but the order failed",
        "I need a copy of my invoice",
        "My subscription payment failed",
        "I cannot complete the payment",
        "The refund amount is incorrect",
        "My bank transfer has not arrived",
        "I need help understanding my bill",
        "My payment confirmation is missing",
        "I was billed for a cancelled order",
        "The checkout page rejects my card",
        "I need to update my billing details",
        "My transaction was declined",
        "I was charged the wrong price",
        "The refund is taking too long",
        "I cannot download my invoice",
        "My wallet payment failed",
        "I see an unknown charge on my bill"
    ],
    "technical": [
        "I am unable to upload a document",
        "The document upload feature is not working",
        "I get an error when uploading a file",
        "File upload fails every time",
        "The application does not accept my document",
        "The application crashes on startup",
        "The website is very slow",
        "I get an error when uploading a file",
        "The screen remains blank",
        "The search feature does not work",
        "I cannot download a report",
        "The application freezes frequently",
        "The website fails to load",
        "I cannot upload my document",
        "The app closes unexpectedly",
        "The page keeps showing an error",
        "The dashboard is not loading",
        "The application is responding slowly",
        "I cannot open the settings page",
        "The download button does nothing",
        "The search results are incorrect",
        "The software stops responding",
        "I cannot connect to the server",
        "The website displays a technical error",
        "My file upload gets stuck",
        "The application keeps restarting",
        "The page layout is broken",
        "I cannot generate a report",
        "The app shows a connection error",
        "The website crashes when I click submit"
    ],
    "general": [
        "What are your customer support hours",
        "Where can I read the user guide",
        "Please tell me about your services",
        "Where can I find the frequently asked questions",
        "I want to share feedback",
        "How can I contact customer support",
        "Where can I learn about your products",
        "Do you have a product catalogue",
        "I need general information about your company",
        "Where can I find your help centre",
        "How do I submit a suggestion",
        "Can you explain your service plans",
        "Where can I read the documentation",
        "I would like to provide feedback",
        "What services do you offer",
        "Where can I find tutorials",
        "How can I learn more about your company",
        "Please share information about your policies",
        "Where can I find contact information",
        "I have a general question about your service",
        "Can you explain how your service works",
        "Where can I find announcements",
        "I want to learn about available features",
        "How can I give a suggestion",
        "Please provide general product information"
    ]
}

urgency_rules = {
    "account": "Low",
    "payment": "Medium",
    "technical": "Medium",
    "general": "Low"
}

team_mapping = {
    "account": "Account Support",
    "payment": "Billing Support",
    "technical": "Technical Support",
    "general": "General Support"
}

rows = []

for category, messages in examples.items():
    for message in messages:
        rows.append({
            "ticket_id": "",
            "message": message,
            "category": category,
            "urgency": urgency_rules[category],
            "assigned_team": team_mapping[category]
        })

random.shuffle(rows)

for index, row in enumerate(rows, start=1):
    row["ticket_id"] = f"S{index:03d}"

with DATA_PATH.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "ticket_id",
            "message",
            "category",
            "urgency",
            "assigned_team"
        ]
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {len(rows)} simulated tickets.")
print("Important: urgency labels are illustrative, not validated.")
