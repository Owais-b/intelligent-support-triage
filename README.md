# Intelligent Support Triage

## 1. Project Overview

Intelligent Support Triage is a Python-based AI project that automatically analyzes customer support messages and recommends an appropriate support category, urgency level, and support team.

It uses Natural Language Processing (NLP) and Machine Learning to classify messages. It also includes confidence-based checks and human-review rules to reduce the risk of incorrect routing.

## 2. Objectives

- Classify customer tickets into Account, Payment, Technical, or General categories.
- Estimate ticket urgency using keyword-based rules.
- Recommend the appropriate support team.
- Send uncertain and potentially sensitive cases for human review.
- Test the system using automated unit tests.
- Analyze errors and document the limitations of the model.

## 3. Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib
- Unittest

## 4. Project Structure

```text
intelligent-support-triage/
├── data/
│   └── support_tickets.csv
├── src/
│   ├── __init__.py
│   ├── baseline.py
│   ├── expand_dataset.py
│   ├── train_model.py
│   ├── predict.py
│   └── triage_model.joblib
├── tests/
│   └── test_predictions.py
├── requirements.txt
└── README.md
```

## 5. How It Works

1. The user enters a customer support message.
2. The TF-IDF vectorizer converts the message into numerical features.
3. The Logistic Regression model predicts the ticket category.
4. The system calculates the model's prediction confidence.
5. Keyword-based rules estimate the urgency level.
6. Sensitive or low-confidence tickets are sent for human review.
7. Other tickets are assigned a recommended support team.

## 6. Ticket Categories and Teams

| Category | Recommended Team |
|---|---|
| Account | Account Support |
| Payment | Billing Support |
| Technical | Technical Support |
| General | General Support |

## 7. Installation

Install Python and open a terminal in the project folder.

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## 8. Train the Model

Run the following command from the project root:

```bash
python -m src.train_model
```

This trains the model using the ticket dataset, evaluates it on a held-out test split, and saves the trained model.

## 9. Run the Application

Run:

```bash
python -m src.predict
```

Enter a customer message when prompted. Type `exit` to close the application.

## 10. Run the Tests

Run:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains nine tests covering urgency rules, empty inputs, sensitive-case review, valid category predictions, and confidence values.

**Latest test result:** 9 tests passed.

## 11. Evaluation Results

The current model achieved **92% accuracy** on a test split of 25 tickets from a dataset of 100 simulated tickets.

This is an initial experimental result, not a measure of expected real-world performance. The dataset is small and manually created, so the result may not generalize to actual customer support messages.

## 12. Safety and Human Review

- Low-confidence predictions are sent for human review.
- Potentially sensitive cases, such as suspected account compromise or fraud, require human review.
- The urgency level is based on keyword rules rather than a separately trained urgency model.
- Model confidence does not guarantee that a prediction is correct.
- The system is a prototype and should not make consequential decisions without appropriate human oversight.

## 13. Limitations

- The dataset contains simulated examples rather than real, independently validated tickets.
- The urgency rules may miss important context or misunderstand a message.
- The model may misclassify unfamiliar wording, spelling mistakes, or ambiguous messages.
- A confidence threshold alone cannot guarantee that every incorrect prediction will be reviewed.

## 14. Future Improvements

- Collect a larger, more diverse, properly labelled dataset.
- Evaluate the model on independently collected test examples.
- Improve urgency classification using a labelled dataset.
- Add a simple web interface for support agents.
- Record review decisions and analyze recurring errors.
- Monitor model performance and update the model when appropriate.

## 15. Conclusion

Intelligent Support Triage demonstrates how NLP, machine learning, rule-based urgency estimation, and human-review safeguards can be combined to assist customer support teams. It is a prototype intended to support human decisions, not replace them.
