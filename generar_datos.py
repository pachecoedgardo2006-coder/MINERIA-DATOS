import pandas as pd
import numpy as np
import random

# Set a seed so the random results are the same every time you run it
np.random.seed(42)
num_records = 500

# 1. Create an empty DataFrame (like a blank spreadsheet)
df = pd.DataFrame()

# Generate unique IDs for each student
df['student_id'] = range(1, num_records + 1)

# Generate Age with some outliers (extreme values)
# Most students are between 17 and 25, but we inject some "noise"
ages = np.random.randint(17, 26, size=num_records).tolist()
for i in range(10): # Inject 10 illogical values (child or elderly)
    ages[random.randint(0, 499)] = random.choice([5, 85, 99])

df['age'] = ages

# 2. Academic Variable: GPA (0.0 to 5.0 scale)
df['gpa'] = np.round(np.random.uniform(1.0, 5.0, num_records), 2)

# Introduce NULL VALUES (NaN) in GPA (15 missing records)
for _ in range(15):
    df.loc[random.randint(0, 499), 'gpa'] = np.nan

# 3. Academic Variable: Attendance Percentage
df['attendance_pct'] = np.random.randint(40, 101, size=num_records)

# 4. Financial Variable: Monthly Income
# Generate normal income with some "Millionaire" outliers
income = np.random.normal(1500000, 500000, num_records).astype(int)
for i in range(5): # 5 cases of extreme wealth or typing errors
    income[random.randint(0, 499)] = 50000000 
    
df['monthly_income'] = income

# 5. Categorical Variable: Scholarship Status
df['has_scholarship'] = np.random.choice(['Yes', 'No'], size=num_records, p=[0.3, 0.7])

# 6. Target Variable: Dropout (Yes/No)
# Logic: Students with low GPA or low attendance have a higher risk of dropping out
def calculate_dropout(row):
    risk_score = 0
    # Higher risk if GPA is missing or below 3.0
    if pd.isna(row['gpa']) or row['gpa'] < 3.0:
        risk_score += 2
    # Higher risk if attendance is below 70%
    if row['attendance_pct'] < 70:
        risk_score += 2
    # Moderate risk if they don't have a scholarship
    if row['has_scholarship'] == 'No':
        risk_score += 1
        
    # High risk score = 80% chance of Dropout; Low risk = 10% chance
    if risk_score >= 3:
        return np.random.choice(['Yes', 'No'], p=[0.8, 0.2])
    else:
        return np.random.choice(['Yes', 'No'], p=[0.1, 0.9])

df['dropout'] = df.apply(calculate_dropout, axis=1)

# Step 7: Export to CSV
file_name = "school_dropout_dataset.csv"
df.to_csv(file_name, index=False, encoding='utf-8')

# --- FORMATTED TERMINAL REPORT ---
print("\n" + "="*55)
print("       📊 SYNTHETIC DATA GENERATION REPORT")
print("="*55)

print(f"✅ File saved as: {file_name}")
print(f"👥 Total records: {len(df)}")
print("-"*55)

# Quality check for Null Values
print("🔍 Data Quality Check (Null Values):")
nulls = df.isnull().sum()
for col, count in nulls.items():
    status = "❌" if count > 0 else "✅"
    print(f"   {status} {col.ljust(18)}: {count} nulls")

print("-"*55)

# Distribution of the Target Variable
print("📈 Target Variable Distribution (Dropout):")
counts = df['dropout'].value_counts()
for label, total in counts.items():
    percentage = (total / len(df)) * 100
    print(f"   - {label}: {total} ({percentage:.1f}%)")

# Esthetic preview of the data
print("-"*55)
print("📋 Data Preview (First 5 records):")
print(df.head().to_string(index=False))
print("="*55 + "\n")