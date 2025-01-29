import unittest
from ..main import check_email

class TestSolution(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(check_email("test@123.com"))

    def test_invalid_email(self):
        self.assertFalse(check_email("123.com"))

    def test_empty_email(self):
        self.assertFalse(check_email(""))

    def test_email_with_spaces(self):
        self.assertFalse(check_email("test@123 .com"))

    def test_email_without_at(self):
        self.assertFalse(check_email("123.com"))

    def test_email_without_dot(self):
        self.assertFalse(check_email("test@123"))

    def test_email_without_domain(self):
        self.assertFalse(check_email("test@123"))

    def test_email_without_domain_zone(self):
        self.assertFalse(check_email("test@123."))

    def test_email_with_special_characters(self):
        self.assertFalse(check_email("test@123.com!"))

if __name__ == "__main__":
    unittest.main()