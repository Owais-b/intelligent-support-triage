
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "data/support_tickets.csv"
MODEL_PATH = "src/triage_model.joblib"

# 1. Load the dataset
df = pd.read_csv(DATA_PATH)

# 2. Check that required data is available
df = df.dropna(subset=["message", "category"])
df["message"] = df["message"].astype(str)
df["category"] = df["category"].astype(str)

if df["category"].nunique() < 2:
    raise ValueError("The dataset needs at least two categories.")

if df["category"].value_counts().min() < 2:
    raise ValueError(
        "Each category needs at least two examples."
    )

# 3. Separate messages and their correct categories
X = df["message"]
y = df["category"]

# 4. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 5. Create the machine-learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

# 6. Train the model
model.fit(X_train, y_train)

# 7. Evaluate on examples not used for training
predictions = model.predict(X_test)

# Identify tickets that were classified incorrectly
print("\n--- Error Analysis ---")

errors = []

for message, actual, predicted in zip(
    X_test, y_test, predictions
):
    if actual != predicted:
        errors.append({
            "message": message,
            "actual": actual,
            "predicted": predicted
        })

if errors:
    for index, error in enumerate(errors, start=1):
        print(f"\nError {index}:")
        print("Message:", error["message"])
        print("Actual category:", error["actual"])
        print("Predicted category:", error["predicted"])
else:
    print("No misclassified tickets in this test split.")

print("\n--- Machine Learning Model Results ---")
print("Training tickets:", len(X_train))
print("Testing tickets:", len(X_test))
print(
    f"Test accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%"
)
print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# 8. Save the trained model
joblib.dump(model, MODEL_PATH)
print(f"\nModel saved to: {MODEL_PATH}")
