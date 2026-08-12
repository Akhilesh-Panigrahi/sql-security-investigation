-- 1. Retrieve after-hours failed login attempts
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
  AND success = FALSE;


-- 2. Retrieve login attempts on May 8 or May 9, 2022
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';


-- 3. Retrieve login attempts outside of Mexico
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';


-- 4. Retrieve Marketing employees in the East building
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%';


-- 5. Retrieve employees in Finance or Sales
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';


-- 6. Retrieve all employees not in IT
SELECT *
FROM employees
WHERE NOT department = 'IT';
