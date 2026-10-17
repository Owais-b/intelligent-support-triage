
import re

import pandas as pd

DATA_PATH = "data/support_tickets.csv"

# Simple keyword rules for the baseline classifier
RULES = {
    "account": [
        "login", "log in", "password", "account",
        "locked", "accessed"
    ],
    "payment": [
        "payment", "refund", "charged", "bill",
        "credit card", "deducted"
    ],
    "technical": [
        "crashes", "crash", "error", "slowly",
        "blank screen", "not working", "download"
    ],
    "general": [
        "working hours", "user guide", "services",
        "profile information", "questions", "feedback"
    ]
}

TEAM_MAPPING = {
    "account": "Account Support",
    "payment": "Billing Support",
    "technical": "Technical Support",
    "general": "General Support"
}


def predict_category(message):
    text = message.lower()
    scores = {}

    for category, keywords in RULES.items():
        scores[category] = sum(
            1 for keyword in keywords
            if re.search(
                r"\b" + re.escape(keyword) + r"\b",
                text
            )
        )

    best_category = max(scores, key=scores.get)

    # Do not guess if no rule matches.
    if scores[best_category] == 0:
        return "needs_review"

    # Flag ambiguous messages for human review.
    highest_score = scores[best_category]
    tied_categories = [
        category for category, score in scores.items()
        if score == highest_score
    ]

    if len(tied_categories) > 1:
        return "needs_review"

    return best_category


def main():
    df = pd.read_csv(DATA_PATH)

    correct = 0

    for _, row in df.iterrows():
        predicted = predict_category(row["message"])
        actual = row["category"]

        if predicted == actual:
            correct += 1

        print(f"\nTicket: {row['message']}")
        print(f"Actual category: {actual}")
        print(f"Predicted category: {predicted}")

        if predicted == "needs_review":
            print("Action: Send for human review")
        else:
            print("Suggested team:", TEAM_MAPPING[predicted])

    accuracy = correct / len(df) * 100

    print("\n--- Baseline Summary ---")
    print(f"Tickets evaluated: {len(df)}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy on sample dataset: {accuracy:.2f}%")


if __name__ == "__main__":
    main()
