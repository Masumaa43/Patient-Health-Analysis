# analysis.py
# PATIENT HEALTH ANALYZER
# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np

# 2. LOAD DATA
df = pd.read_csv("processed_patient_data.csv")

print("=================================")
print("PATIENT HEALTH ANALYZER")
print("=================================")

print("\nFirst 5 Rows:\n")
print(df.head())

# 3. DATA CLEANING

print("\n========== DATA CLEANING ==========")

print("\nDataset Information:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nData cleaning completed successfully!")


# 4. FEATURE ENGINEERING

print("\n========== FEATURE ENGINEERING ==========")

# Cost per Day
df["Cost_per_Day"] = (
    df["Treatment Cost"] /
    df["Hospital Stay (Days)"]
)

# Recovery Category
def recovery_category(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Poor"

df["Recovery Category"] = (
    df["Recovery Score"]
    .apply(recovery_category)
)

# Recovery Efficiency
df["Recovery_Efficiency"] = (
    df["Recovery Score"] /
    df["Hospital Stay (Days)"]
)

# Cost Efficiency
df["Cost_Efficiency"] = (
    df["Recovery Score"] /
    df["Treatment Cost"]
)

# Risk Level
df["Risk_Level"] = (
    df["Recovery Score"]
    .apply(lambda x:
           "High Risk" if x < 50 else "Stable")
)

print("\nFeature engineering completed!")

# 5. KPIs

print("\n========== KPIs ==========")

total_patients = df["Patient ID"].nunique()

avg_age = round(df["Age"].mean(), 2)

avg_cost = round(
    df["Treatment Cost"].mean(), 2
)

avg_stay = round(
    df["Hospital Stay (Days)"].mean(), 2
)

avg_recovery = round(
    df["Recovery Score"].mean(), 2
)

print("Total Patients:", total_patients)

print("Average Age:", avg_age)

print("Average Treatment Cost:", avg_cost)

print("Average Hospital Stay:", avg_stay)

print("Average Recovery Score:", avg_recovery)


# 6. ANALYSIS

print("\n========== ANALYSIS ==========")

# Age Group Distribution
print("\nAge Group Distribution:\n")

print(df["Age Group"].value_counts())

# Gender Distribution
print("\nGender Distribution:\n")

print(df["Gender"].value_counts())

# Treatment Analysis
treatment_counts = (
    df["Treatment Type"]
    .value_counts()
)

recovery_by_treatment = (
    df.groupby("Treatment Type")
    ["Recovery Score"]
    .mean()
)

cost_by_treatment = (
    df.groupby("Treatment Type")
    ["Treatment Cost"]
    .mean()
)

# Department Analysis
dept_patients = (
    df["Department"]
    .value_counts()
)

dept_cost = (
    df.groupby("Department")
    ["Treatment Cost"]
    .mean()
)

# Doctor Analysis
doctor_analysis = (
    df.groupby("Doctor Name")
    .agg({
        "Recovery Score": "mean",
        "Treatment Cost": "mean",
        "Patient ID": "count"
    })
    .rename(columns={
        "Patient ID": "Patients_Treated"
    })
)

# Department Efficiency
dept_efficiency = (
    df.groupby("Department")
    .agg({
        "Recovery Score": "mean",
        "Treatment Cost": "mean",
        "Hospital Stay (Days)": "mean"
    })
)

# 7. CORRELATION ANALYSIS

print("\n========== CORRELATION ==========")

correlation = df[[
    "Age",
    "Treatment Cost",
    "Hospital Stay (Days)",
    "Recovery Score"
]].corr()

print(correlation)


# 8. SMART INSIGHTS

print("\n========== SMART INSIGHTS ==========")

print("Best Treatment Type:",
      recovery_by_treatment.idxmax())

print("Most Expensive Department:",
      dept_cost.idxmax())

print("Top Doctor:",
      doctor_analysis[
          "Recovery Score"
      ].idxmax())

print("Most Efficient Department:",
      dept_efficiency[
          "Recovery Score"
      ].idxmax())

print("Highest Cost Treatment:",
      cost_by_treatment.idxmax())

print(
    "Most Risky Age Group:",
    df.groupby("Age Group")
    ["Recovery Score"]
    .mean()
    .idxmin()
)

# 9. SAVE FINAL DATA

df.to_csv(
    "final_patient_analysis.csv",
    index=False
)

print("\nFinal processed dataset saved!")

print("\nAnalysis completed successfully!")