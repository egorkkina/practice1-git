import unittest
from utils import greet, farewell, get_name_length


class TestUtils(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Маргарита"), "Здравствуйте, Маргарита!")

    def test_farewell(self):
        self.assertEqual(farewell("Маргарита"), "До свидания, Маргарита!")
        
    def test_get_name_length(self):
        self.assertEqual(get_name_length("Маргарита"), 9)
        self.assertEqual(get_name_length("Анна"), 4)
        self.assertEqual(get_name_length(""), 0)


if __name__ == "__main__":
    unittest.main()