# Intelligent Support Triage

## 1. Project Overview

Intelligent Support Triage is a Python-based machine learning project that analyzes customer support messages and recommends a ticket category, urgency level, and support team.

It uses Natural Language Processing (NLP) and Machine Learning to classify messages. Confidence-based checks and human-review rules help reduce the risk of incorrect routing.

This project is an educational prototype and is not intended to replace human judgment.

## 2. Objectives

- Classify support tickets into Account, Payment, Technical, or General categories.
- Estimate ticket urgency using keyword-based rules.
- Recommend an appropriate support team.
- Route uncertain and potentially sensitive cases for human review.
- Evaluate the model and analyze classification errors.
- Test the application using automated unit tests.

## 3. Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib
- Python Unittest

## 4. Project Structure

```text
intelligent-support-triage/
├── data/
│   └── support_tickets.csv
├── src/
│   ├── __init__.py
│   ├── baseline.py
│   ├── expand_dataset.py
│   ├── predict.py
│   └── train_model.py
├── tests/
│   └── test_predictions.py
├── .gitignore
├── README.md
└── requirements.txt
```

The trained model file is generated locally during training and is excluded from Git using `.gitignore`.

## 5. How It Works

1. The user enters a customer support message.
2. TF-IDF converts the text into numerical features.
3. A Logistic Regression model predicts the ticket category.
4. The application checks the model's prediction confidence.
5. Keyword-based rules estimate urgency.
6. Potentially sensitive or low-confidence cases are flagged for human review.
7. Other cases receive a recommended support team.

## 6. Ticket Categories and Teams

| Category | Recommended Team |
|---|---|
| Account | Account Support |
| Payment | Billing Support |
| Technical | Technical Support |
| General | General Support |

## 7. Dataset

The project uses **110 simulated customer support tickets** across four categories:

- Account
- Payment
- Technical
- General

The dataset is manually created for experimentation and learning. It does not represent real customer data, and its labels have not been independently validated.

## 8. Installation

Install Python, then open a terminal in the project directory.

Create and activate a virtual environment if you have not already done so.

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## 9. Train the Model

From the project root, run:

```bash
python -m src.train_model
```

This trains the model, evaluates it on a held-out test split, and generates the trained model file required by the prediction application.

Run this command again whenever you want to retrain the model.

## 10. Run the Application

Run:

```bash
python -m src.predict
```

Enter a customer message when prompted. Type `exit` to close the application.

## 11. Run the Tests

Run:

```bash
python -m unittest discover -s tests -v
```

The test suite contains nine tests covering urgency rules, empty inputs, sensitive-case review, valid category predictions, and confidence values.

The previously reported test run passed all nine tests. Rerun the command above to verify the current version.

## 12. Model Evaluation

The model is evaluated using a held-out test split from the simulated dataset. The training script generates evaluation metrics and a classification report.

Because the dataset is small and synthetic, these metrics should be treated as preliminary experimental results rather than evidence of real-world performance.

For a reliable evaluation, the model should also be tested on a larger, independently collected and properly labelled dataset.

## 13. Safety and Human Review

- Predictions below the configured confidence threshold are flagged for human review.
- Potentially sensitive cases, including suspected fraud or account compromise, require human review.
- Urgency is estimated using keyword-based rules rather than a separately trained urgency classifier.
- Model confidence does not guarantee prediction correctness.
- The prototype should not make consequential decisions without appropriate human oversight.

## 14. Limitations

- The dataset contains simulated examples rather than real, independently validated tickets.
- Keyword rules can miss context or misunderstand a message.
- Unfamiliar wording, spelling errors, and ambiguous messages may lead to misclassification.
- A confidence threshold cannot guarantee that every incorrect prediction will be reviewed.
- Performance on the simulated dataset may not generalize to actual customer support messages.

## 15. Future Improvements

- Collect a larger and more diverse labelled dataset.
- Evaluate the model on independently collected test examples.
- Improve urgency classification using labelled training data.
- Add a web interface for support agents.
- Record human-review decisions and analyze recurring errors.
- Monitor model performance and retrain when appropriate.

## 16. Conclusion

Intelligent Support Triage demonstrates how NLP, machine learning, rule-based urgency estimation, and human-review safeguards can work together to assist customer support teams.

The project is an educational prototype designed to support human decisions, not replace them.
