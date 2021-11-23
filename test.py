import unittest
from encoder import encode_word


class TestEncoder(unittest.TestCase):
    def test_if_word_that_has_one_char_is_the_same(self):
        encoded_word = encode_word("I")
        self.assertEqual((encoded_word), "I")

    def test_if_word_that_has_two_char_is_the_same(self):
        encoded_word = encode_word("hi")
        self.assertEqual((encoded_word), "hi")

    def test_if_word_that_has_three_char_is_the_same(self):
        encoded_word = encode_word("him")
        self.assertEqual((encoded_word), "him")


if __name__ == "__main__":
    unittest.main()
