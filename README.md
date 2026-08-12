# 🔎 SQL Security Investigation
 
### Security-focused SQL filtering and investigation of authentication activity and employee systems
 
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Security%20Analysis-4479A1?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/Tests-6%20Passed-success)](#testing)
[![Status](https://img.shields.io/badge/Status-Complete-success)](#project-status)
 
---
 
## 📌 Overview
 
This project demonstrates how **SQL filtering techniques can be applied to cybersecurity investigations** to identify suspicious login activity and retrieve specific employee records for security-related actions.
 
The project originated as part of the **Google Cybersecurity Professional Certificate** and has been expanded into a standalone **Portfolio Edition** designed to demonstrate practical SQL investigation skills through a reproducible and tested environment.
 
The investigation works with two primary datasets:
 
- `log_in_attempts` — authentication and login activity
- `employees` — employee and workstation information
The original project required filtering these datasets to investigate potential security incidents and identify employee systems requiring security updates.
 
---
 
## 🎯 Security Objectives
 
The investigation addresses six security-related scenarios:
 
1. Identify failed login attempts occurring after business hours.
2. Investigate login activity occurring on May 8 and May 9, 2022.
3. Identify login attempts originating outside Mexico.
4. Identify Marketing employees located in the East building.
5. Identify employees belonging to Finance or Sales.
6. Identify employees who are not part of the IT department.
These investigations demonstrate how security analysts can use SQL to narrow large datasets down to information relevant to a specific security question.
 
---
 
## 🧠 SQL Techniques Demonstrated
 
| SQL Technique | Security Application |
|---|---|
| `SELECT` | Retrieve relevant security records |
| `WHERE` | Filter investigation results |
| `AND` | Combine multiple security conditions |
| `OR` | Search for multiple possible conditions |
| `NOT` | Exclude trusted or expected values |
| `LIKE` | Match patterns in stored data |
| `%` wildcard | Match variable text patterns |
| `BETWEEN` | Filter activity within a date range |
| `COUNT()` | Quantify investigation findings |
 
The original coursework specifically emphasized the use of `AND`, `OR`, `NOT`, `LIKE`, and the `%` wildcard when filtering the two tables.
 
---
 
## 🔍 Investigation 1 — After-Hours Failed Login Attempts
 
### Security Scenario
 
A potential security incident occurred after normal business hours.
 
Login attempts occurring after **18:00** that were unsuccessful needed to be investigated.
 
The investigation uses a `WHERE` clause with `AND` to combine:
 
- Login time after 18:00
- Failed authentication attempts
### Portfolio Edition Result
 
```text
After-hours failed login attempts : 6
```
 
### Security Relevance
 
After-hours authentication failures can be useful indicators during an investigation because unusual login activity may warrant additional analysis.
 
---
 
## 📅 Investigation 2 — Login Attempts on Specific Dates
 
### Security Scenario
 
A suspicious event occurred on May 9, 2022.
 
The investigation therefore examined login activity occurring on:
 
- May 8, 2022
- May 9, 2022
The investigation uses the `OR` operator to retrieve activity from either date.
 
### Portfolio Edition Result
 
```text
May 8-9 login attempts : 6
```
 
### Security Relevance
 
Filtering authentication activity around the time of a known security event can help analysts establish a timeline and identify potentially relevant activity.
 
---
 
## 🌎 Investigation 3 — Login Attempts Outside Mexico
 
### Security Scenario
 
The organization identified potential concerns with login attempts originating outside Mexico.
 
The investigation uses:
 
```sql
NOT LIKE 'MEX%'
```
 
to exclude locations represented as Mexico-related values in the dataset.
 
The `%` wildcard allows the query to match values beginning with the specified pattern.
 
### Portfolio Edition Result
 
```text
Login attempts outside Mexico : 5
```
 
### Security Relevance
 
Geographic filtering can help analysts identify authentication activity occurring outside an organization's expected operating region.
 
---
 
## 🏢 Investigation 4 — Marketing Employees in the East Building
 
### Security Scenario
 
The organization needed to identify employee machines requiring a security update.
 
The investigation focused specifically on employees who:
 
- Work in the Marketing department
- Are located in the East building
The investigation uses `AND` together with the `LIKE 'East%'` pattern.
 
### Portfolio Edition Result
 
```text
Marketing employees in East : 2
```
 
### Security Relevance
 
Targeted employee queries can help security teams identify which systems or users are affected by a specific security update.
 
---
 
## 💰 Investigation 5 — Finance or Sales Employees
 
### Security Scenario
 
A different security update was required for employees in the:
 
- Finance department
- Sales department
The investigation uses `OR` because employees can belong to either department.
 
### Portfolio Edition Result
 
```text
Finance or Sales employees : 4
```
 
### Security Relevance
 
Department-based filtering can help security teams scope affected systems and users when deploying targeted security controls or updates.
 
---
 
## 💻 Investigation 6 — Employees Outside IT
 
### Security Scenario
 
The final investigation identifies employees who were not part of the Information Technology department.
 
The investigation uses `NOT` to exclude IT employees.
 
### Portfolio Edition Result
 
```text
Employees outside IT : 10
```
 
### Security Relevance
 
Understanding which users fall outside the IT department can help security teams scope system updates, access reviews, and security communications.
 
---
 
## 📊 Investigation Results
 
| Investigation | Findings |
|---|---|
| After-hours failed login attempts | 6 |
| May 8–9 login attempts | 6 |
| Login attempts outside Mexico | 5 |
| Marketing employees in East | 2 |
| Finance or Sales employees | 4 |
| Employees outside IT | 10 |
 
---
 
## 🏗️ Project Architecture
 
```text
                    ┌─────────────────────┐
                    │   Security Dataset  │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
        ┌────────▼────────┐        ┌────────▼────────┐
        │ log_in_attempts │        │    employees    │
        └────────┬────────┘        └────────┬────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               │
                      ┌────────▼────────┐
                      │  SQL Filtering  │
                      │                 │
                      │ WHERE           │
                      │ AND / OR / NOT  │
                      │ LIKE / %        │
                      └────────┬────────┘
                               │
                      ┌────────▼────────┐
                      │   Investigation │
                      │     Results     │
                      └────────┬────────┘
                               │
                      ┌────────▼────────┐
                      │ Security        │
                      │ Findings        │
                      └─────────────────┘
```
 
---
 
## 📁 Repository Structure
 
```text
SQL-Security-Investigation/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── sql/
│   ├── 01_schema.sql
│   ├── 02_seed_data.sql
│   ├── 03_investigation_queries.sql
│   └── 04_analysis_queries.sql
│
├── data/
│   └── README.md
│
├── scripts/
│   └── run_investigation.py
│
├── tests/
│   └── test_queries.py
│
├── docs/
│   └── investigation-methodology.md
│
└── screenshots/
```
 
---
 
## ⚙️ Portfolio Edition Enhancements
 
The original Google Cybersecurity project focused primarily on writing SQL queries to retrieve the required information.
 
This standalone Portfolio Edition expands that work into a reproducible project environment.
 
### Added capabilities
 
- 🗄️ Structured SQL schema
- 📊 Reproducible dataset
- 🔎 Organized investigation queries
- 📈 Analysis queries
- 🐍 Python-based investigation runner
- 🧪 Automated test suite
- 📚 Investigation methodology documentation
- 🧱 Professional repository structure
- 🔄 Reproducible execution through GitHub Codespaces
The original project demonstrated SQL filtering concepts; this Portfolio Edition demonstrates how those concepts can be organized into a repeatable security investigation workflow.
 
---
 
## 🧪 Testing
 
The project includes an automated test suite covering all six investigations.
 
Run:
 
```bash
python -m unittest discover -s tests -v
```
 
Expected result:
 
```text
test_after_hours_failed_logins ... ok
test_finance_or_sales ... ok
test_marketing_east ... ok
test_not_it ... ok
test_outside_mexico ... ok
test_specific_dates ... ok
 
----------------------------------------------------------------------
Ran 6 tests
 
OK
```
 
---
 
## ▶️ Running the Investigation
 
The project can be executed directly from GitHub Codespaces or another Python environment.
 
### 1. Clone the repository
 
```bash
git clone https://github.com/Akhilesh-Panigrahi/SQL-Security-Investigation.git
cd SQL-Security-Investigation
```
 
### 2. Run the investigation
 
```bash
python scripts/run_investigation.py
```
 
### 3. Run the automated tests
 
```bash
python -m unittest discover -s tests -v
```
 
No external Python packages are required for the core investigation runner.
 
---
 
## 🖥️ Example Output
 
```text
============================================================
SQL SECURITY INVESTIGATION
============================================================
 
INVESTIGATION SUMMARY
------------------------------------------------------------
After-hours failed login attempts       : 6
May 8-9 login attempts                  : 6
Login attempts outside Mexico           : 5
Marketing employees in East             : 2
Finance or Sales employees              : 4
Employees outside IT                    : 10
 
✓ Investigation completed successfully.
============================================================
```
 
---
 
## 🎓 Project Origin
 
This project originated from the Google Cybersecurity Professional Certificate.
 
The original assignment focused on applying SQL filters to security-related tasks involving login attempts and employee information.
 
The original work covered:
 
- After-hours failed login attempts
- Login attempts on specific dates
- Login attempts outside Mexico
- Marketing employees in the East building
- Finance or Sales employees
- Employees outside IT
The original coursework used the `log_in_attempts` and `employees` tables together with `AND`, `OR`, `NOT`, `LIKE`, and `%` wildcard filtering.
 
The original coursework document is retained separately from the Portfolio Edition implementation so that the project's origin and subsequent enhancements remain clear.
 
---
 
## 📚 Skills Demonstrated
 
**SQL**
- SQL querying
- Filtering
- Conditional logic
- Pattern matching
- Date filtering
- Data analysis
**Cybersecurity**
- Authentication log investigation
- Security event analysis
- Investigation scoping
- Geographic anomaly identification
- Security update targeting
- Access and user analysis
**Software Development**
- Python
- Automated testing
- Reproducible execution
- Project organization
- Documentation
- Git/GitHub
- GitHub Codespaces
---
 
## 💡 Key Takeaways
 
This project reinforced how SQL can be used as an investigation tool rather than simply as a method for retrieving database records.
 
Security analysts frequently need to answer questions such as:
 
- What happened?
- When did it happen?
- Where did it happen?
- Which users or systems were affected?
SQL filtering provides a practical way to narrow large datasets into information that can support those investigations.
 
---
 
## 🚀 Future Improvements
 
Potential future enhancements include:
 
- Integrating a larger authentication dataset
- Adding additional suspicious-login detection rules
- Calculating failed-login rates by user or location
- Adding severity classification
- Exporting investigation results to CSV
- Building visual security dashboards
- Integrating the workflow with a SIEM platform
- Adding more automated security tests
---
 
## 👨‍💻 Author
 
**Akhilesh Panigrahi**
 
🎓 A.S. in Computer Science and Information Security
🛡️ Aspiring Cybersecurity Analyst
📍 United States
 
---
 
⭐ Thanks for visiting!
 
If you found this project useful, feel free to explore the other cybersecurity projects in my portfolio.
 
**Learn → Build → Investigate → Improve**

---

## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.
