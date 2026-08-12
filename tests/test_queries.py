import subprocess
import sys
import unittest
from pathlib import Path


class SecurityQueryTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Run the complete SQL investigation and capture
        the resulting terminal output.
        """

        project_root = Path(__file__).resolve().parent.parent
        script_path = project_root / "scripts" / "run_investigation.py"

        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )

        cls.output = result.stdout

    def test_after_hours_failed_logins(self):
        self.assertIn(
            "After-hours failed login attempts       : 6",
            self.output,
        )

    def test_specific_dates(self):
        self.assertIn(
            "May 8-9 login attempts                   : 6",
            self.output,
        )

    def test_outside_mexico(self):
        self.assertIn(
            "Login attempts outside Mexico             : 5",
            self.output,
        )

    def test_marketing_east(self):
        self.assertIn(
            "Marketing employees in East               : 2",
            self.output,
        )

    def test_finance_or_sales(self):
        self.assertIn(
            "Finance or Sales employees                : 4",
            self.output,
        )

    def test_not_it(self):
        self.assertIn(
            "Employees outside IT                      : 10",
            self.output,
        )


if __name__ == "__main__":
    unittest.main()