# Investigation Methodology

## Source

This project is based on the Google Cybersecurity Professional Certificate exercise "Apply filters to SQL queries."

The source exercise describes two tables:

- `log_in_attempts`
- `employees`

It demonstrates filtering with `AND`, `OR`, `NOT`, `LIKE`, and `%`.

## Investigation Questions

### Authentication activity

- Failed login attempts after 18:00
- Login attempts on May 8 and May 9, 2022
- Login attempts outside Mexico

### Employee targeting

- Marketing employees in the East building
- Finance or Sales employees
- Employees outside IT

## Portfolio Edition

The original coursework is the conceptual source. This repository adds:

- a reproducible SQLite schema
- synthetic data
- separated SQL scripts
- automated validation
- an execution script
- security-focused documentation

The synthetic dataset is deliberately independent of the original course dataset.
