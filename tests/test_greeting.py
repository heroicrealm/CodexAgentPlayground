import datetime
import pathlib
import subprocess
import unittest


EXECUTABLE = pathlib.Path(__file__).resolve().parents[1] / "greeting"
PROMPT = "Введите имя пользователя: "


def run_program(value):
    return subprocess.run(
        [str(EXECUTABLE)], input=value, text=True, capture_output=True, timeout=5
    )


class GreetingTests(unittest.TestCase):
    def test_root_gets_greeting_followed_by_current_time(self):
        before = datetime.datetime.now().replace(microsecond=0)
        result = run_program("root\n")
        after = datetime.datetime.now().replace(microsecond=0)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], PROMPT + "Здравствуйте, root!")
        prefix = "Текущее время: "
        self.assertTrue(lines[1].startswith(prefix))
        timestamp = datetime.datetime.strptime(lines[1][len(prefix):], "%Y-%m-%d %H:%M:%S")
        self.assertLessEqual(before, timestamp)
        self.assertLessEqual(timestamp, after)

    def test_other_names_are_rejected_without_time(self):
        for name in ("alice", "Root", "root ", " root", "", "root user"):
            with self.subTest(name=name):
                result = run_program(name + "\n")
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout, PROMPT + "пользователь не найден\n")
                self.assertEqual(result.stderr, "")

    def test_missing_input_fails(self):
        result = run_program("")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, PROMPT)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
