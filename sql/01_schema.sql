DROP TABLE IF EXISTS log_in_attempts;
DROP TABLE IF EXISTS employees;

CREATE TABLE log_in_attempts (
    attempt_id INTEGER PRIMARY KEY,
    login_date TEXT NOT NULL,
    login_time TEXT NOT NULL,
    username TEXT NOT NULL,
    country TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    success BOOLEAN NOT NULL CHECK (success IN (0, 1))
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department TEXT NOT NULL,
    office TEXT NOT NULL,
    machine_id TEXT NOT NULL UNIQUE
);
