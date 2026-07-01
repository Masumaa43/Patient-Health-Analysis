# dashboard.py
# PATIENT HEALTH ANALYZER DASHBOARD

# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 2. PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Patient Health Analyzer",
    page_icon="🏥",
    layout="wide"
)

# ==============================
# 3. LOAD DATA
# ==============================
df = pd.read_csv("final_patient_analysis.csv")

# ==============================
# 4. TITLE
# ==============================
st.title("🏥 Patient Health Analyzer Dashboard")

st.markdown("""
This dashboard provides healthcare insights related to:
- Patient recovery
- Treatment performance
- Department analysis
- Hospital stay trends
- Cost analysis
""")

# ==============================
# 5. SIDEBAR FILTERS
# ==============================
st.sidebar.header("Filter Data")

department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

treatment = st.sidebar.multiselect(
    "Select Treatment Type",
    options=df["Treatment Type"].unique(),
    default=df["Treatment Type"].unique()
)

# Apply filters
filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["Treatment Type"].isin(treatment))
]

# ==============================
# 6. KPI SECTION
# ==============================
st.header("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Patients",
        filtered_df["Patient ID"].nunique()
    )

with col2:
    st.metric(
        "Average Recovery",
        round(filtered_df["Recovery Score"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Cost",
        round(filtered_df["Treatment Cost"].mean(), 2)
    )

with col4:
    st.metric(
        "Average Hospital Stay",
        round(filtered_df["Hospital Stay (Days)"].mean(), 2)
    )

# ==============================
# 7. GRAPH 1
# ==============================
st.header("📌 Patients per Department")

fig1, ax1 = plt.subplots(figsize=(8,5))

filtered_df["Department"].value_counts().plot(
    kind="bar",
    color="skyblue",
    ax=ax1
)

ax1.set_title("Patients in Each Department")
ax1.set_xlabel("Department")
ax1.set_ylabel("Number of Patients")

st.pyplot(fig1)

st.info(
    "This graph shows which department handles the highest number of patients."
)

# ==============================
# 8. GRAPH 2
# ==============================
st.header("📌 Recovery by Treatment Type")

recovery_by_treatment = (
    filtered_df.groupby("Treatment Type")
    ["Recovery Score"]
    .mean()
)

fig2, ax2 = plt.subplots(figsize=(7,5))

recovery_by_treatment.plot(
    kind="bar",
    color="green",
    ax=ax2
)

ax2.set_title("Average Recovery Score")
ax2.set_xlabel("Treatment Type")
ax2.set_ylabel("Recovery Score")

st.pyplot(fig2)

st.info(
    "This graph compares recovery performance of different treatment methods."
)

# ==============================
# 9. GRAPH 3
# ==============================
st.header("📌 Gender Distribution")

fig3, ax3 = plt.subplots(figsize=(6,6))

filtered_df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3
)

ax3.set_ylabel("")

st.pyplot(fig3)

st.info(
    "This pie chart represents gender distribution of patients."
)

# ==============================
# 10. GRAPH 4
# ==============================
st.header("📌 Hospital Stay vs Recovery")

fig4, ax4 = plt.subplots(figsize=(7,5))

ax4.scatter(
    filtered_df["Hospital Stay (Days)"],
    filtered_df["Recovery Score"],
    color="red"
)

ax4.set_title("Hospital Stay vs Recovery")
ax4.set_xlabel("Hospital Stay (Days)")
ax4.set_ylabel("Recovery Score")

st.pyplot(fig4)

st.info(
    "This scatter plot shows the relationship between hospital stay duration and patient recovery."
)

# ==============================
# 11. GRAPH 5
# ==============================
st.header("📌 Correlation Heatmap")

correlation = filtered_df[[
    "Age",
    "Treatment Cost",
    "Hospital Stay (Days)",
    "Recovery Score"
]].corr()

fig5, ax5 = plt.subplots(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="YlGnBu",
    linewidths=1,
    linecolor="white",
    ax=ax5
)

ax5.set_title("Correlation Between Healthcare Factors")

st.pyplot(fig5)

st.info(
    "This heatmap shows relationships between healthcare factors like age, cost, stay duration, and recovery."
)

# ==============================
# 12. SMART INSIGHTS
# ==============================
st.header("💡 Smart Insights")

recovery_by_treatment = (
    filtered_df.groupby("Treatment Type")
    ["Recovery Score"]
    .mean()
)

dept_cost = (
    filtered_df.groupby("Department")
    ["Treatment Cost"]
    .mean()
)

st.success(
    f"✅ Best Treatment Type: {recovery_by_treatment.idxmax()}"
)

st.warning(
    f"💰 Most Expensive Department: {dept_cost.idxmax()}"
)

st.info(
    f"📈 Highest Recovery Score: {round(filtered_df['Recovery Score'].max(), 2)}"
)

st.error(
    f"⚠ Lowest Recovery Score: {round(filtered_df['Recovery Score'].min(), 2)}"
)

# ==============================
# 13. DATASET VIEW
# ==============================
st.header("📄 Patient Dataset")

st.dataframe(filtered_df)

# ==============================
# 14. FOOTER
# ==============================
st.markdown("---")

st.markdown(
    "Developed using Python, Pandas, Matplotlib, Seaborn, and Streamlit"
)