# =========================================
# visualization.py
# PATIENT HEALTH ANALYZER VISUALIZATION
# =========================================

# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# 2. CREATE OUTPUT FOLDERS
# ==============================
os.makedirs("outputs/charts", exist_ok=True)

# ==============================
# 3. GRAPH STYLE
# ==============================
sns.set_style("whitegrid")

# ==============================
# 4. LOAD DATA
# ==============================
df = pd.read_csv("final_patient_analysis.csv")

# ==============================
# 5. REQUIRED ANALYSIS
# ==============================

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

# Correlation
correlation = df[[
    "Age",
    "Treatment Cost",
    "Hospital Stay (Days)",
    "Recovery Score"
]].corr()

# ==============================
# 6. VISUALIZATIONS
# ==============================

# --------------------------------
# GRAPH 1 : Patients per Department
# --------------------------------
plt.figure(figsize=(8,5))

df["Department"].value_counts().plot(
    kind="bar",
    color="skyblue"
)

plt.title(
    "GRAPH 1: Number of Patients in Each Department",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.figtext(
    0.5,
    -0.08,
    "This graph shows which department handles the highest number of patients.",
    ha="center",
    fontsize=10
)

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph1_department_patients.png"
)

plt.show()

# --------------------------------
# GRAPH 2 : Recovery by Treatment
# --------------------------------
plt.figure(figsize=(7,5))

recovery_by_treatment.plot(
    kind="bar",
    color="green"
)

plt.title(
    "GRAPH 2: Average Recovery Score by Treatment Type",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Treatment Type")
plt.ylabel("Average Recovery Score")

plt.figtext(
    0.5,
    -0.08,
    "This graph compares recovery performance of different treatment types.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph2_recovery_treatment.png"
)

plt.show()

# --------------------------------
# GRAPH 3 : Cost by Treatment
# --------------------------------
plt.figure(figsize=(7,5))

cost_by_treatment.plot(
    kind="bar",
    color="orange"
)

plt.title(
    "GRAPH 3: Average Treatment Cost by Treatment Type",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Treatment Type")
plt.ylabel("Average Cost")

plt.figtext(
    0.5,
    -0.08,
    "This graph shows which treatment type is more expensive.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph3_cost_treatment.png"
)

plt.show()

# --------------------------------
# GRAPH 4 : Gender Distribution
# --------------------------------
plt.figure(figsize=(6,6))

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "GRAPH 4: Gender Distribution of Patients",
    fontsize=14,
    fontweight='bold'
)

plt.ylabel("")

plt.figtext(
    0.5,
    0.02,
    "This pie chart represents male, female, and other patient distribution.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph4_gender_distribution.png"
)

plt.show()

# --------------------------------
# GRAPH 5 : Treatment Distribution
# --------------------------------
plt.figure(figsize=(6,6))

df["Treatment Type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "GRAPH 5: Distribution of Treatment Types",
    fontsize=14,
    fontweight='bold'
)

plt.ylabel("")

plt.figtext(
    0.5,
    0.02,
    "This graph shows the percentage of each treatment type used.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph5_treatment_distribution.png"
)

plt.show()

# --------------------------------
# GRAPH 6 : Hospital Stay vs Recovery
# --------------------------------
plt.figure(figsize=(7,5))

plt.scatter(
    df["Hospital Stay (Days)"],
    df["Recovery Score"],
    color="red"
)

plt.title(
    "GRAPH 6: Hospital Stay vs Recovery Score",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Hospital Stay (Days)")
plt.ylabel("Recovery Score")

plt.figtext(
    0.5,
    -0.08,
    "This scatter plot shows relationship between hospital stay and recovery.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph6_stay_vs_recovery.png"
)

plt.show()

# --------------------------------
# GRAPH 7 : Correlation Heatmap
# --------------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="YlGnBu",
    linewidths=1,
    linecolor='white'
)

plt.title(
    "GRAPH 7: Correlation Between Healthcare Factors",
    fontsize=14,
    fontweight='bold'
)

plt.figtext(
    0.5,
    -0.05,
    "This heatmap shows relationships between age, cost, stay duration, and recovery.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph7_correlation_heatmap.png"
)

plt.show()

# --------------------------------
# GRAPH 8 : Strong Correlation Heatmap
# --------------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=1,
    linecolor='black',
    fmt=".2f"
)

plt.title(
    "GRAPH 8: Strong Positive & Negative Correlation",
    fontsize=14,
    fontweight='bold'
)

plt.figtext(
    0.5,
    -0.05,
    "This heatmap highlights strong positive and negative relationships among healthcare factors.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph8_strong_correlation_heatmap.png"
)

plt.show()

# --------------------------------
# GRAPH 9 : Advanced Correlation Heatmap
# --------------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="magma",
    square=True,
    cbar=True,
    linewidths=2
)

plt.title(
    "GRAPH 9: Advanced Healthcare Correlation Analysis",
    fontsize=14,
    fontweight='bold'
)

plt.figtext(
    0.5,
    -0.05,
    "This graph visually compares correlation intensity between healthcare variables.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph9_advanced_heatmap.png"
)

plt.show()

# --------------------------------
# GRAPH 10 : Recovery Focus Heatmap
# --------------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation[["Recovery Score"]],
    annot=True,
    cmap="viridis",
    linewidths=1,
    linecolor='white'
)

plt.title(
    "GRAPH 10: Factors Affecting Recovery Score",
    fontsize=14,
    fontweight='bold'
)

plt.figtext(
    0.5,
    -0.05,
    "This heatmap specifically shows how age, cost, and hospital stay affect recovery score.",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.savefig(
    "outputs/charts/graph10_recovery_focus_heatmap.png"
)

plt.show()

print("\nAll graphs generated successfully!")
print("Charts saved in outputs/charts/")