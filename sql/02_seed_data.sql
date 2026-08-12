INSERT INTO log_in_attempts
(attempt_id, login_date, login_time, username, country, ip_address, success)
VALUES
(1, '2022-05-07', '08:14', 'jsmith', 'MEX', '192.0.2.10', 1),
(2, '2022-05-08', '09:22', 'agarcia', 'MEXICO', '192.0.2.11', 1),
(3, '2022-05-08', '19:15', 'bwilson', 'USA', '198.51.100.10', 0),
(4, '2022-05-08', '20:42', 'cpatel', 'MEX', '203.0.113.10', 0),
(5, '2022-05-09', '10:05', 'dlee', 'MEXICO', '192.0.2.14', 1),
(6, '2022-05-09', '18:30', 'emartin', 'CAN', '198.51.100.20', 0),
(7, '2022-05-09', '21:10', 'fthomas', 'GBR', '198.51.100.21', 0),
(8, '2022-05-10', '07:45', 'gkim', 'MEX', '192.0.2.18', 1),
(9, '2022-05-10', '19:05', 'hrodriguez', 'USA', '198.51.100.22', 0),
(10, '2022-05-11', '12:30', 'ijohnson', 'MEXICO', '192.0.2.24', 1),
(11, '2022-05-12', '17:59', 'jchen', 'MEX', '192.0.2.30', 1),
(12, '2022-05-13', '22:15', 'kgreen', 'BRA', '203.0.113.25', 0);

INSERT INTO employees
(employee_id, username, first_name, last_name, department, office, machine_id)
VALUES
(1, 'jsmith', 'Jordan', 'Smith', 'IT', 'East-101', 'MACH-001'),
(2, 'agarcia', 'Alex', 'Garcia', 'Marketing', 'East-201', 'MACH-002'),
(3, 'bwilson', 'Bailey', 'Wilson', 'Marketing', 'East-202', 'MACH-003'),
(4, 'cpatel', 'Casey', 'Patel', 'Finance', 'West-101', 'MACH-004'),
(5, 'dlee', 'Drew', 'Lee', 'Sales', 'North-101', 'MACH-005'),
(6, 'emartin', 'Evan', 'Martin', 'Finance', 'West-102', 'MACH-006'),
(7, 'fthomas', 'Frankie', 'Thomas', 'Sales', 'North-102', 'MACH-007'),
(8, 'gkim', 'Grace', 'Kim', 'IT', 'East-102', 'MACH-008'),
(9, 'hrodriguez', 'Harper', 'Rodriguez', 'HR', 'South-101', 'MACH-009'),
(10, 'ijohnson', 'Isaac', 'Johnson', 'Operations', 'South-102', 'MACH-010'),
(11, 'jchen', 'Jamie', 'Chen', 'Engineering', 'West-201', 'MACH-011'),
(12, 'kgreen', 'Kai', 'Green', 'Legal', 'North-201', 'MACH-012');
