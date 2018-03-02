import unittest

from reverseString import reverse_string

class UniqueCharTest(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("qwertyu"), "uytrewq")

    def test_sentences(self):
        self.assertEqual(reverse_string("The animals are drinking water"),"retaw gniknird era slamina ehT")

    def test_empty_string(self):
        self.assertEqual(reverse_string(" "), " ")

    def test_no_string(self):
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main()
