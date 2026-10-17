
import joblib

MODEL_PATH = "src/triage_model.joblib"
model = joblib.load(MODEL_PATH)

TEAM_MAPPING = {
    "account": "Account Support",
    "payment": "Billing Support",
    "technical": "Technical Support",
    "general": "General Support"
}

HIGH_URGENCY_WORDS = [
    "urgent",
    "fraud",
    "without permission",
    "account hacked",
    "charged twice",
    "money stolen",
    "data breach",
    "unauthorized access"
]

MEDIUM_URGENCY_WORDS = [
    "failed",
    "error",
    "refund",
    "locked",
    "slow",
    "cannot log in",
    "can't log in"
]

REVIEW_WORDS = [
    "fraud",
    "hacked",
    "without permission",
    "unauthorized access",
    "data breach",
    "money stolen"
]

CONFIDENCE_THRESHOLD = 0.55


def predict_urgency(message):
    text = message.lower()

    if any(word in text for word in HIGH_URGENCY_WORDS):
        return "High"

    if any(word in text for word in MEDIUM_URGENCY_WORDS):
        return "Medium"

    return "Low"


def predict_ticket(message):
    message = message.strip()

    if not message:
        print("Please enter a valid message.")
        return None

    text = message.lower()

    # Predict category and model confidence
    probabilities = model.predict_proba([message])[0]
    classes = model.classes_

    best_index = probabilities.argmax()
    predicted_category = classes[best_index]
    confidence = probabilities[best_index]

    urgency = predict_urgency(message)

    # Sensitive keywords require review even if confidence is high
    sensitive_case = any(
        word in text for word in REVIEW_WORDS
    )

    uncertain = confidence < CONFIDENCE_THRESHOLD

    if sensitive_case or uncertain:
        team = "Human Review Required"
        final_category = "needs_review"
    else:
        final_category = predicted_category
        team = TEAM_MAPPING[final_category]

    print("\n--- Ticket Triage Result ---")
    print("Customer message:", message)
    print("Model prediction:", predicted_category)
    print(f"Model confidence: {confidence:.2%}")
    print("Final category:", final_category)
    print("Urgency:", urgency)
    print("Recommended team:", team)

    if sensitive_case:
        print("Review reason: Potentially sensitive issue.")

    if uncertain:
        print("Review reason: Model confidence is below threshold.")

    if team == "Human Review Required":
        print("Action: Human review is required before routing.")

    print("\nNote: Urgency is based on keyword rules.")
    print("Confidence is not a guarantee of correctness.")

    return {
        "category": final_category,
        "predicted_category": predicted_category,
        "confidence": float(confidence),
        "urgency": urgency,
        "assigned_team": team,
        "needs_review": sensitive_case or uncertain
    }


if __name__ == "__main__":
    while True:
        message = input(
            "\nEnter a customer message (or 'exit' to quit): "
        )

        if message.strip().lower() == "exit":
            print("Triage program closed.")
            break

        predict_ticket(message)
