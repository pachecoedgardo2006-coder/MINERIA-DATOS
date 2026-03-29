# School Dropout Synthetic Dataset
This project was created to generate a synthetic dataset (500 records) that simulates student dropout scenarios. It was developed as part of our academic coursework to practice data generation, handling missing values, and identifying outliers.

## Group Members
* Mariana Cala
* Edgardo Pacheco
* Yairineth Camargo

---

## Dataset Overview
The final CSV contains 500 rows with 7 key variables that help predict if a student might leave school:

| Variable | Description | Type |
| :--- | :--- | :--- |
| `student_id` | Unique ID for each student | Int |
| `age` | Student age (mostly 17-25, includes noise) | Int |
| `gpa` | Academic average (1.0 to 5.0) | Float |
| `attendance_pct`| Percentage of classes attended | Int |
| `monthly_income`| Family income (simulated with normal distribution) | Int |
| `has_scholarship`| Scholarship status (Yes/No) | String |
| `dropout` | Target variable (Yes/No) | String |

## How the data was generated
To make the dataset more realistic for data cleaning exercises, we manually injected some "errors" and specific logic:

* **Missing Data:** We introduced 15 null values (`NaN`) in the `gpa` column to simulate incomplete academic records.
* **Outliers:** * We added extreme ages like 5, 85, and 99 years in 10 records.
    * We set an income of 50,000,000 in 5 records to simulate either extreme wealth or data entry errors.
* **Dropout Logic:** The `dropout` result isn't random. We used a scoring system where students with low GPAs, poor attendance, or no scholarship have an 80% chance of dropping out, while others only have a 10% baseline risk.

## Installation & Usage
You will need `pandas` and `numpy` to run the generator.

```bash
pip install pandas numpy