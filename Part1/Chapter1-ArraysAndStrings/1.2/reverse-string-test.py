import unittest

from reverseString import reverse_string

class UniqueCharTest(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("qwertyu"), "uytrewq")

    def test_sentences(self):
        self.assertEqual(reverse_string("The animals are drinking water"),"retaw gniknird era slamina ehT")

if __name__ == '__main__':
    unittest.main()
