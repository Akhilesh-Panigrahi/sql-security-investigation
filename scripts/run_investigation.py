#!/usr/bin/env python3
"""Run the SQL security investigation against a temporary SQLite database."""

from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "sql" / "01_schema.sql"
SEED = ROOT / "sql" / "02_seed_data.sql"
QUERIES = ROOT / "sql" / "03_investigation_queries.sql"
ANALYSIS = ROOT / "sql" / "04_analysis_queries.sql"


def load_sql(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run() -> None:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row

    try:
        connection.executescript(load_sql(SCHEMA))
        connection.executescript(load_sql(SEED))

        print("=" * 64)
        print("              SQL SECURITY INVESTIGATION")
        print("=" * 64)
        print()
        print("✓ Database schema loaded")
        print("✓ Synthetic security data loaded")
        print("✓ Investigation queries loaded")
        print()

        investigations = [
            (
                "1. After-hours failed login attempts",
                """SELECT * FROM log_in_attempts
                   WHERE login_time > '18:00' AND success = FALSE""",
            ),
            (
                "2. Login attempts on May 8 or May 9, 2022",
                """SELECT * FROM log_in_attempts
                   WHERE login_date = '2022-05-09'
                      OR login_date = '2022-05-08'""",
            ),
            (
                "3. Login attempts outside Mexico",
                """SELECT * FROM log_in_attempts
                   WHERE NOT country LIKE 'MEX%'""",
            ),
            (
                "4. Marketing employees in the East building",
                """SELECT * FROM employees
                   WHERE department = 'Marketing'
                     AND office LIKE 'East%'""",
            ),
            (
                "5. Employees in Finance or Sales",
                """SELECT * FROM employees
                   WHERE department = 'Finance'
                      OR department = 'Sales'""",
            ),
            (
                "6. Employees not in IT",
                """SELECT * FROM employees
                   WHERE NOT department = 'IT'""",
            ),
        ]

        for title, query in investigations:
            rows = connection.execute(query).fetchall()
            print("-" * 64)
            print(title)
            print("-" * 64)
            print(f"Result count: {len(rows)}")
            for row in rows:
                print(" | ".join(str(value) for value in row))
            print()

        print("-" * 64)
        print("INVESTIGATION SUMMARY")
        print("-" * 64)

        summary = connection.execute(
            """SELECT 'After-hours failed login attempts', COUNT(*)
               FROM log_in_attempts
               WHERE login_time > '18:00' AND success = FALSE
               UNION ALL
               SELECT 'May 8-9 login attempts', COUNT(*)
               FROM log_in_attempts
               WHERE login_date = '2022-05-09'
                  OR login_date = '2022-05-08'
               UNION ALL
               SELECT 'Login attempts outside Mexico', COUNT(*)
               FROM log_in_attempts
               WHERE NOT country LIKE 'MEX%'
               UNION ALL
               SELECT 'Marketing employees in East', COUNT(*)
               FROM employees
               WHERE department = 'Marketing' AND office LIKE 'East%'
               UNION ALL
               SELECT 'Finance or Sales employees', COUNT(*)
               FROM employees
               WHERE department = 'Finance' OR department = 'Sales'
               UNION ALL
               SELECT 'Employees outside IT', COUNT(*)
               FROM employees
               WHERE NOT department = 'IT'"""
        ).fetchall()

        for investigation, count in summary:
            print(f"{investigation:<40} : {count}")

        print()
        print("✓ Investigation completed successfully.")
        print("=" * 64)

    finally:
        connection.close()


if __name__ == "__main__":
    run()
