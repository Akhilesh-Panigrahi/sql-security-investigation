import sqlite3
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SecurityQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(":memory:")
        cls.connection.executescript(
            (ROOT / "sql" / "01_schema.sql").read_text(encoding="utf-8")
        )
        cls.connection.executescript(
            (ROOT / "sql" / "02_seed_data.sql").read_text(encoding="utf-8")
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_after_hours_failed_logins(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM log_in_attempts
               WHERE login_time > '18:00' AND success = FALSE"""
        ).fetchone()[0]
        self.assertEqual(count, 4)

    def test_specific_dates(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM log_in_attempts
               WHERE login_date = '2022-05-09'
                  OR login_date = '2022-05-08'"""
        ).fetchone()[0]
        self.assertEqual(count, 5)

    def test_outside_mexico(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM log_in_attempts
               WHERE NOT country LIKE 'MEX%'"""
        ).fetchone()[0]
        self.assertEqual(count, 5)

    def test_marketing_east(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM employees
               WHERE department = 'Marketing'
                 AND office LIKE 'East%'"""
        ).fetchone()[0]
        self.assertEqual(count, 2)

    def test_finance_or_sales(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM employees
               WHERE department = 'Finance'
                  OR department = 'Sales'"""
        ).fetchone()[0]
        self.assertEqual(count, 4)

    def test_not_it(self):
        count = self.connection.execute(
            """SELECT COUNT(*) FROM employees
               WHERE NOT department = 'IT'"""
        ).fetchone()[0]
        self.assertEqual(count, 10)


if __name__ == "__main__":
    unittest.main()
