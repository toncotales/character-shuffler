"""Character classification utilities."""

from __future__ import annotations

import string


def get_char_type(char: str) -> str:
    """Return the character type used by the shuffler.

    Types are:
        uppercase: uppercase letters
        lowercase: lowercase letters
        digit: digits
        symbol: ASCII punctuation
        unknown: everything else
    """
    if len(char) != 1:
        raise ValueError("char must contain exactly one character")

    if char.isupper():
        return "uppercase"
    if char.islower():
        return "lowercase"
    if char.isdigit():
        return "digit"
    if char in string.punctuation:
        return "symbol"
    return "unknown"
