
import unittest

from src.predict import predict_ticket, predict_urgency


class TestTicketTriage(unittest.TestCase):

    def test_high_urgency_fraud(self):
        self.assertEqual(
            predict_urgency(
                "Someone accessed my account without permission"
            ),
            "High"
        )

    def test_high_urgency_double_charge(self):
        self.assertEqual(
            predict_urgency("My payment was charged twice"),
            "High"
        )

    def test_medium_urgency_error(self):
        self.assertEqual(
            predict_urgency("I receive an error while uploading a file"),
            "Medium"
        )

    def test_low_urgency_general_question(self):
        self.assertEqual(
            predict_urgency("Where can I find the user guide"),
            "Low"
        )

    def test_empty_message(self):
        self.assertIsNone(predict_ticket(""))

    def test_whitespace_message(self):
        self.assertIsNone(predict_ticket("   "))

    def test_sensitive_message_requires_review(self):
        result = predict_ticket(
            "Someone accessed my account without permission"
        )
        self.assertTrue(result["needs_review"])
        self.assertEqual(
            result["assigned_team"],
            "Human Review Required"
        )

    def test_normal_message_returns_valid_category(self):
        result = predict_ticket(
            "Where can I find the user guide"
        )
        self.assertIn(
            result["predicted_category"],
            ["account", "payment", "technical", "general"]
        )

    def test_confidence_is_valid(self):
        result = predict_ticket(
            "The application crashes when I open it"
        )
        self.assertGreaterEqual(result["confidence"], 0.0)
        self.assertLessEqual(result["confidence"], 1.0)


if __name__ == "__main__":
    unittest.main()
