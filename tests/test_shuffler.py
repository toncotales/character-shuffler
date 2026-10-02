import random
import unittest

from character_shuffler.classifier import get_char_type
from character_shuffler.shuffler import shuffle


def type_sequence(text: str) -> list[str]:
    return [get_char_type(char) for char in text]


class ShuffleTests(unittest.TestCase):
    def setUp(self):
        random.seed(12345)

    def test_empty_input(self):
        self.assertEqual(shuffle(""), "")

    def test_single_character(self):
        self.assertEqual(shuffle("A"), "A")

    def test_impossible_input(self):
        self.assertEqual(shuffle("AAAA"), "")

    def test_preserves_all_characters(self):
        source = "Aa1! Bb2?"
        result = shuffle(source)

        self.assertEqual(sorted(result), sorted(source))

    def test_adjacent_types_are_different(self):
        source = "AAaa11!!??"
        result = shuffle(source)

        self.assertNotEqual(result, "")

        types = type_sequence(result)
        self.assertTrue(
            all(a != b for a, b in zip(types, types[1:]))
        )

    def test_unicode_characters(self):
        source = "éA２1"
        result = shuffle(source)

        self.assertEqual(sorted(result), sorted(source))

        types = type_sequence(result)
        self.assertTrue(
            all(a != b for a, b in zip(types, types[1:]))
        )

    def test_unknown_characters_are_supported(self):
        source = "A 1!"
        result = shuffle(source)

        self.assertEqual(sorted(result), sorted(source))

        types = type_sequence(result)
        self.assertTrue(
            all(a != b for a, b in zip(types, types[1:]))
        )


if __name__ == "__main__":
    unittest.main()
