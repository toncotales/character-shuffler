# Character Shuffler

A small modular Python application that randomly rearranges characters so
adjacent characters have different character types.

## Project structure

```text
character_shuffler_project/
├── character_shuffler/
│   ├── __init__.py
│   ├── classifier.py
│   ├── shuffler.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_classifier.py
│   ├── test_shuffler.py
│   └── test_cli.py
└── README.md
```

## Requirements

Python 3.10+.

## Run the CLI

From the project directory:

```bash
python -m character_shuffler "Aa1!"
```

You can also pipe input through stdin:

```bash
echo "Aa1!" | python -m character_shuffler
```

Show help:

```bash
python -m character_shuffler --help
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

The implementation is deliberately modular rather than class-based:

- `classifier.py` contains character classification.
- `shuffler.py` contains the rearrangement algorithm.
- `cli.py` contains command-line concerns.
- `tests/` contains focused unit tests for each responsibility.
