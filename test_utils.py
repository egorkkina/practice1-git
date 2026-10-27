import unittest
from utils import greet, farewell, get_name_length, get_initials


class TestUtils(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Маргарита"), "Здравствуйте, Маргарита!")

    def test_farewell(self):
        self.assertEqual(farewell("Маргарита"), "До свидания, Маргарита!")
        
    def test_get_name_length(self):
        self.assertEqual(get_name_length("Маргарита"), 9)
        self.assertEqual(get_name_length("Анна"), 4)
        self.assertEqual(get_name_length(""), 0)
        
    def test_get_initials(self):
        self.assertEqual(get_initials("Маргарита", "Валерьевна"), "М.В.")


if __name__ == "__main__":
    unittest.main()