"""Command-line interface for the character shuffler."""

from __future__ import annotations

import argparse

from .shuffler import shuffle


def build_parser() -> argparse.ArgumentParser:
    """Create and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Randomly rearrange text so adjacent characters "
            "have different character types."
        )
    )

    parser.add_argument(
        "text",
        nargs="?",
        help="text to rearrange; omit it to read from standard input",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    text = args.text if args.text is not None else input()

    result = shuffle(text)

    if not result and text:
        parser.error("no valid rearrangement exists")

    print(result)
    return 0
