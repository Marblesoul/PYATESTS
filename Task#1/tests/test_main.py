import unittest
from .. import main


class TestSolution(unittest.TestCase):
    def test_equal_lists(self):
        boys = ["Игорь", "Андрей"]
        girls = ["Оля", "Маша"]
        expected = "Андрей и Маша, Игорь и Оля"
        self.assertEqual(main.solve(boys, girls), expected)

    def test_not_equal_lists(self):
        boys = ["Игорь", "Андрей", "Максим"]
        girls = ["Оля", "Маша"]
        expected = "Кто-то может остаться без пары!"
        self.assertEqual(main.solve(boys, girls), expected)

    def test_empty_lists(self):
        boys = []
        girls = []
        expected = ""
        self.assertEqual(main.solve(boys, girls), expected)

    def test_other_equal_lists(self):
        boys = ["Петя", "Саша"]
        girls = ["Наташа", "Марина"]
        expected = "Петя и Марина, Саша и Наташа"
        self.assertEqual(main.solve(boys, girls), expected)

if __name__ == "__main__":
    unittest.main()