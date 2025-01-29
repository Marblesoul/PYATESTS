import unittest
from ..main import solve

class TestSolve(unittest.TestCase):
    def test_example_phrases(self):
        phrases = [
            "нажал кабан на баклажан", "дом как комод", "рвал дед лавр",
            "азот калий и лактоза","а собака боса", "тонет енот",
            "карман мрак", "пуст суп"
        ]
        expected = [
            "нажал кабан на баклажан", "рвал дед лавр",
            "азот калий и лактоза", "а собака боса",
            "тонет енот", "пуст суп"
        ]
        self.assertEqual(solve(phrases), expected)

    def test_empty_list(self):
        phrases = []
        expected = []
        self.assertEqual(solve(phrases), expected)

    def test_no_palindromes(self):
        phrases = ["просто текст", "абра кадабра", "python code"]
        expected = []
        self.assertEqual(solve(phrases), expected)

    def test_single_palindrome(self):
        phrases = ["а роза упала на лапу азора", "random text", "hello"]
        expected = ["а роза упала на лапу азора"]
        self.assertEqual(solve(phrases), expected)

    def test_upper_lower_case(self):
        phrases = ["Anna", "aN nA"]
        expected = []
        self.assertEqual(solve(phrases), expected)

if __name__ == '__main__':
    unittest.main()