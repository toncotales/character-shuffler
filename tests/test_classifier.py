import unittest

from character_shuffler.classifier import get_char_type


class GetCharTypeTests(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(get_char_type("A"), "uppercase")

    def test_lowercase(self):
        self.assertEqual(get_char_type("a"), "lowercase")

    def test_digit(self):
        self.assertEqual(get_char_type("7"), "digit")

    def test_ascii_symbol(self):
        self.assertEqual(get_char_type("!"), "symbol")

    def test_unknown_character(self):
        self.assertEqual(get_char_type(" "), "unknown")

    def test_unicode_uppercase(self):
        self.assertEqual(get_char_type("É"), "uppercase")

    def test_unicode_digit(self):
        self.assertEqual(get_char_type("２"), "digit")

    def test_rejects_multiple_characters(self):
        with self.assertRaises(ValueError):
            get_char_type("AB")

    def test_rejects_empty_string(self):
        with self.assertRaises(ValueError):
            get_char_type("")


if __name__ == "__main__":
    unittest.main()
