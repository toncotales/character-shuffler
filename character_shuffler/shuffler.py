"""Core character rearrangement algorithm."""

from __future__ import annotations

import random

from .classifier import get_char_type


def shuffle(text: str) -> str:
    """Randomly rearrange text so adjacent characters have different types.

    Characters belonging to the same type are randomized internally.

    Returns:
        A valid rearrangement, or "" when no valid rearrangement exists.
        Empty input returns "".
    """

    if not text:
        return ""

    # Group characters by their type.
    groups: dict[str, list[str]] = {}

    for char in text:
        char_type = get_char_type(char)

        if char_type not in groups:
            groups[char_type] = []

        groups[char_type].append(char)

    # Randomize characters within each group.
    for chars in groups.values():
        random.shuffle(chars)

    result: list[str] = []
    previous_type: str | None = None

    while groups:

        # Find types that are different from the previous type.
        available_types = [
            char_type
            for char_type in groups
            if char_type != previous_type
        ]

        # No type is available, so a valid arrangement is impossible.
        if not available_types:
            return ""

        # Randomize the order when there is a tie.
        random.shuffle(available_types)

        # Find the largest remaining group.
        max_count = max(
            len(groups[char_type])
            for char_type in available_types
        )

        # Keep only the groups with the largest number of characters.
        candidates = [
            char_type
            for char_type in available_types
            if len(groups[char_type]) == max_count
        ]

        # Randomly choose one of the largest groups.
        char_type = random.choice(candidates)

        # Take one character from that group.
        result.append(groups[char_type].pop())

        # Remove the group if it is now empty.
        if not groups[char_type]:
            del groups[char_type]

        previous_type = char_type

    return "".join(result)