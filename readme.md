# School Dropout Synthetic Dataset 🎓

This repository contains a synthetic dataset generated using Python, designed to simulate and analyze the factors influencing school dropout rates. This project fulfills academic requirements for data generation, noise inclusion (nulls/outliers), and variable analysis.

## 📊 Dataset Description

The dataset consists of **500 records** with the following variables:

| Variable | Type | Description | Range/Values |
| :--- | :--- | :--- | :--- |
| `student_id` | Integer | Unique identifier for each student. | 1 - 500 |
| `age` | Integer | Chronological age of the student. | ~17 - 25 years |
| `gpa` | Decimal | Grade Point Average (Academic performance). | 1.0 - 5.0 |
| `attendance_pct`| Integer | Percentage of classes attended. | 40% - 100% |
| `monthly_income`| Integer | Monthly family income (local currency). | Normal Distribution |
| `has_scholarship`| Categorical| Indicates if the student has financial aid. | Yes / No |
| `dropout` | Categorical| **Target Variable** (Output). | Yes / No |

---

## 🛠️ Generation Methodology

To make the dataset realistic and useful for data cleaning practice, the following techniques were applied:

### 1. Introduction of Null Values
Null values (`NaN`) were deliberately introduced into the `gpa` column.
* **Method:** 15 indices were randomly selected using `numpy`, and their original values were replaced with nulls.
* **Purpose:** To simulate data entry errors or missing information in the academic system.

### 2. Outliers (Extreme Values)
Values outside of logical ranges were forced into two key variables:
* **Age:** Extreme values such as **5, 85, and 99 years** were inserted into 10 random records.
* **Monthly Income:** Incomes of **50,000,000** were assigned to 5 records to simulate extreme wealth or typing errors.

### 3. Target Variable Logic
The `dropout` variable is not purely random. A **weighted probability function** was used:
* If a student has a low `gpa` (< 3.0), low `attendance_pct` (< 70%), or lacks a scholarship, their risk score increases.
* Students with high risk scores have an **80% probability** of dropping out.
* Normal cases maintain a baseline **10% dropout probability**.

---

## 🚀 How to Run the Generator

To replicate the data generation, ensure you have `pandas` and `numpy` installed:

```bash
pip install pandas numpy


## member of the group:
Mariana Cala
Edgardo Pacheco
Yairineth Camargo