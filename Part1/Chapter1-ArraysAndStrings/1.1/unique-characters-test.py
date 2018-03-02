import unittest

from uniqueCharacters import check_unique_characters

class UniqueCharTest(unittest.TestCase):

    def test_unique_characters(self):
        self.assertTrue(check_unique_characters("qwertyu"))

    def test_repeated_characters(self):
        self.assertFalse(check_unique_characters("animal"))

if __name__ == '__main__':
    unittest.main()
