-- Portfolio analysis queries.
-- These aggregate the investigation results into analyst-friendly counts.

SELECT
    'After-hours failed login attempts' AS investigation,
    COUNT(*) AS result_count
FROM log_in_attempts
WHERE login_time > '18:00'
  AND success = FALSE

UNION ALL

SELECT
    'May 8-9 login attempts',
    COUNT(*)
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08'

UNION ALL

SELECT
    'Login attempts outside Mexico',
    COUNT(*)
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%'

UNION ALL

SELECT
    'Marketing employees in East',
    COUNT(*)
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%'

UNION ALL

SELECT
    'Finance or Sales employees',
    COUNT(*)
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales'

UNION ALL

SELECT
    'Employees outside IT',
    COUNT(*)
FROM employees
WHERE NOT department = 'IT';
