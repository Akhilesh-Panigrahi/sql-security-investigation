# 🔎 SQL Security Investigation

A portfolio-focused SQL security investigation project based on the **Google Cybersecurity Professional Certificate** "Apply filters to SQL queries" exercise.

The project demonstrates how SQL filtering can support security investigations and operational tasks by analyzing authentication activity and identifying employee devices requiring security updates.

> **Portfolio Edition:** The original coursework focused on writing filtered SQL queries. This repository expands that work into a reproducible, self-contained investigation environment using SQLite, synthetic data, organized SQL scripts, validation tests, and documented findings.

## 🎯 Objectives

The investigation answers six security-focused questions:

1. Which login attempts failed after business hours (after 18:00)?
2. Which login attempts occurred on May 8 or May 9, 2022?
3. Which login attempts originated outside Mexico?
4. Which Marketing employees work in the East building?
5. Which employees are in Finance or Sales?
6. Which employees are not in IT?

The original project explicitly uses the `log_in_attempts` and `employees` tables and demonstrates `AND`, `OR`, `NOT`, `LIKE`, and `%` wildcard filtering. fileciteturn3file0L85-L89

## 🧰 Skills Demonstrated

- SQL querying
- Security event investigation
- Authentication log analysis
- Filtering with `WHERE`
- Boolean logic with `AND`, `OR`, and `NOT`
- Pattern matching with `LIKE`
- Wildcard filtering with `%`
- Security-focused data analysis
- Reproducible investigations
- SQLite

## 📁 Repository Structure

```text
sql-security-investigation/
├── README.md
├── LICENSE
├── .gitignore
├── sql/
│   ├── 01_schema.sql
│   ├── 02_seed_data.sql
│   ├── 03_investigation_queries.sql
│   └── 04_analysis_queries.sql
├── data/
│   └── README.md
├── scripts/
│   └── run_investigation.py
├── tests/
│   └── test_queries.py
├── docs/
│   └── investigation-methodology.md
└── screenshots/
```

## 🔍 Investigation Workflow

```text
Synthetic Security Data
          │
          ▼
    SQLite Database
          │
          ▼
   SQL Filtering Logic
          │
          ├── After-hours failures
          ├── Suspicious dates
          ├── Non-Mexico activity
          ├── Marketing + East
          ├── Finance OR Sales
          └── Non-IT employees
          │
          ▼
    Investigation Results
          │
          ▼
 Security-focused findings
```

## 🧪 Running the Project

No external Python packages are required.

From the repository root:

```bash
python scripts/run_investigation.py
```

The script creates a temporary SQLite database from the included schema and synthetic data, executes every investigation query, and prints the results.

Run the automated tests with:

```bash
python -m unittest discover -s tests -v
```

## 🗃️ Data

The repository uses **synthetic data created for this Portfolio Edition**. It is not presented as the original Google dataset.

The synthetic dataset intentionally contains records needed to reproduce the six investigation scenarios described in the original coursework.

## 🔐 Security Investigation Queries

### 1. After-hours failed login attempts

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
  AND success = FALSE;
```

The original exercise specifies investigating failed login attempts after 18:00 and describes the use of `WHERE`, `AND`, `login_time > '18:00'`, and `success = FALSE`. fileciteturn3file0L9-L19

### 2. Activity on May 8 or May 9

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';
```

The original exercise identifies May 9, 2022 and the preceding day as dates requiring investigation and uses `OR` to retrieve both dates. fileciteturn3file0L22-L32

### 3. Login attempts outside Mexico

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

The source explains that Mexico appears as both `MEX` and `MEXICO`, so `LIKE 'MEX%'` is used with `NOT` to identify other countries. fileciteturn3file0L33-L45

### 4. Marketing employees in the East building

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%';
```

The source specifies Marketing employees in the East building and explains the use of `AND` and `LIKE 'East%'`. fileciteturn3file0L46-L60

### 5. Finance or Sales employees

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';
```

The source specifically explains that `OR` is required because employees from either department should be returned. fileciteturn3file0L61-L73

### 6. Employees outside IT

```sql
SELECT *
FROM employees
WHERE NOT department = 'IT';
```

The original project uses `NOT` to identify employees who are not in the Information Technology department. fileciteturn3file0L76-L84

## 📊 Investigation Findings

The included synthetic dataset produces deterministic results for demonstration:

| Investigation | Expected Result |
|---|---:|
| After-hours failed logins | 6 |
| May 8–9 login attempts | 6 |
| Login attempts outside Mexico | 5 |
| Marketing + East employees | 2 |
| Finance or Sales employees | 4 |
| Employees outside IT | 10 |

These counts are based on the synthetic dataset in this repository, not the original Google dataset.

## 🧠 Security Relevance

SQL filtering is directly useful to security analysts because large authentication and employee datasets often contain far more records than can be reviewed manually.

The techniques demonstrated here can support:

- suspicious authentication investigations
- after-hours activity review
- geographic anomaly investigation
- targeted endpoint update lists
- access-control analysis
- security operations reporting

The original project summarizes the same core approach: using SQL filters to retrieve specific information from login attempts and employee-machine data. fileciteturn3file0L85-L89

## 📚 Source & Attribution

This project is based on the **Google Cybersecurity Professional Certificate** exercise "Apply filters to SQL queries."

The original coursework is preserved separately as reference material when appropriate. The database, synthetic dataset, test suite, execution script, and portfolio documentation in this repository are my Portfolio Edition enhancements.

## 👤 Author

**Akhilesh Panigrahi**

Cybersecurity | Computer Science & Information Security

- GitHub: `YOUR_GITHUB_USERNAME`
- LinkedIn: `YOUR_LINKEDIN_URL`

---

⭐ If you found this project useful, consider starring the repository.
