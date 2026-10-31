import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


@unittest.skipUnless(shutil.which("javac") and shutil.which("java"),
                     "Java hello world test requires a JDK")
class HelloWorldTests(unittest.TestCase):
    def test_program_output(self):
        source = Path(__file__).resolve().with_name("HelloWorld.java")
        with tempfile.TemporaryDirectory() as build_dir:
            subprocess.run(
                ["javac", "-d", build_dir, str(source)],
                capture_output=True, text=True, check=True,
            )
            result = subprocess.run(
                ["java", "-cp", build_dir, "HelloWorld"],
                capture_output=True, text=True, check=True,
            )
        self.assertEqual(result.stdout, "Hello, World!\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
