import unittest
from encoder import encode_word, encode_sentence


class TestEncoder(unittest.TestCase):
    def test_if_word_that_has_one_char_is_the_same(self):
        encoded_word = encode_word("I")
        self.assertEqual(encoded_word[0], "I")

    def test_if_word_that_has_two_char_is_the_same(self):
        encoded_word = encode_word("hi")
        self.assertEqual(encoded_word[0], "hi")

    def test_if_word_that_has_three_char_is_the_same(self):
        encoded_word = encode_word("him")
        self.assertEqual(encoded_word[0], "him")

    def test_if_word_that_cant_be_randomize_is_the_same(self):
        encoded_word = encode_word("Biig")
        self.assertEqual(encoded_word[0], "Biig")

    def test_if_word_that_can_be_randomize_is_not_the_same(self):
        encoded_word = encode_word("Bnig")
        self.assertNotEqual(encoded_word[0], "Bnig")

    def test_if_word_that_cant_be_encoded_dont_have_orginal_word(self):
        encoded_word = encode_word("Loool")
        self.assertIsNone(encoded_word[1])

    def test_if_word_that_can_be_encoded_have_orginal_word(self):
        encoded_word = encode_word("Liol")
        self.assertEqual(encoded_word[1], "Liol")

    def test_check_if_encoded_sentence_has_magic_separator_at_the_beggining(self):
        encoded_sentence = encode_sentence("Hi howow are you today")
        self.assertEqual(encoded_sentence[0][0:9], "\n—weird—\n")

    def test_check_if_encoded_sentence_has_magic_separator_at_the_end(self):
        pass

    def test_check_if_special_characters_are_one_the_same_position(self):
        pass


class TestDecoder(unittest.TestCase):
    def test_if_exception_are_rised_if_encoding_text_without_magic_separator(self):
        pass


if __name__ == "__main__":
    unittest.main()
