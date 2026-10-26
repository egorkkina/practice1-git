import unittest
from utils import greet, farewell


class TestUtils(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Маргарита"), "Здравствуйте, Маргарита!")

    def test_farewell(self):
        self.assertEqual(farewell("Маргарита"), "До свидания, Маргарита!")


if __name__ == "__main__":
    unittest.main()