import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from character_shuffler.cli import main


class CliTests(unittest.TestCase):
    def test_positional_argument(self):
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["Aa1!"])

        self.assertEqual(exit_code, 0)

        result = output.getvalue().strip()
        self.assertEqual(sorted(result), sorted("Aa1!"))

    def test_reads_from_stdin(self):
        output = io.StringIO()

        with patch("builtins.input", return_value="Aa1!"):
            with redirect_stdout(output):
                exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(sorted(output.getvalue().strip()), sorted("Aa1!"))

    def test_impossible_input_is_reported(self):
        stderr = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with redirect_stderr(stderr):
                main(["AAAA"])

        self.assertNotEqual(exc.exception.code, 0)
        self.assertIn("no valid rearrangement exists", stderr.getvalue())

    def test_help(self):
        stdout = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with redirect_stdout(stdout):
                main(["--help"])

        self.assertEqual(exc.exception.code, 0)
        self.assertIn("usage:", stdout.getvalue().lower())


if __name__ == "__main__":
    unittest.main()
