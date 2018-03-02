import unittest

from removeDuplicates import remove_duplicates

class UniqueCharTest(unittest.TestCase):

    def test_remove_dup(self):
        self.assertEqual(remove_duplicates("qwertyu"), "qwertyu")

    def test_sentences(self):
        self.assertEqual(remove_duplicates("unstoppable"),"unstopable")

    def test_empty_string(self):
        self.assertEqual(remove_duplicates(" "), " ")

    def test_no_string(self):
        self.assertEqual(remove_duplicates(""), "")

if __name__ == '__main__':
    unittest.main()
