import random
import subprocess
import sys
import unittest
from pathlib import Path

from bubble_sort import bubble_sort, quick_sort


class QuickSortTests(unittest.TestCase):
    def test_sorts_in_place(self):
        cases = [
            [], [1], [2, 1], [5, 2, 8, 6, 1],
            [3, -2, 0, 3, -2], [1.5, -0.5, 0.0],
            list(range(5000)), list(range(5000, 0, -1)), [7] * 5000,
        ]
        rng = random.Random(25)
        cases.extend([rng.randint(-100, 100) for _ in range(size)]
                     for size in range(100))
        for values in cases:
            with self.subTest(length=len(values), sample=values[:5]):
                expected = sorted(values)
                self.assertIsNone(quick_sort(values))
                self.assertEqual(values, expected)

    def test_legacy_entry_point(self):
        values = [3, 1, 2]
        self.assertIsNone(bubble_sort(values))
        self.assertEqual(values, [1, 2, 3])

    def test_program_output(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("bubble_sort.py"))],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout, "1 2 5 6 8\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
