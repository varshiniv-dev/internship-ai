# ==========================================
# HR & TALENT INSIGHTS
# Nexus Corp
# ==========================================

# STEP 1: Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# STEP 2: Load the dataset

df = pd.read_csv("employee_performance_dataset.csv")

# Display first five rows
df.head()


# STEP 3: Explore the dataset

print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()


# STEP 4: Check for missing values

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# ==========================================
# TASK 1: AVERAGE SALARY
# ==========================================

average_salary = df["Monthly_Salary"].mean()

print("\nAverage Monthly Salary:", average_salary)


# ==========================================
# TASK 2: DEPARTMENTAL SALARY COMPARISON
# ==========================================

department_salary = (
    df.groupby("Department")["Monthly_Salary"]
      .mean()
)

print("\nAverage Salary by Department:")
print(department_salary)


# Find department with highest average salary
highest_salary_department = department_salary.idxmax()

highest_average_salary = department_salary.max()

print("\nHighest-paying Department:",
      highest_salary_department)

print("Highest Average Salary:",
      highest_average_salary)


# ==========================================
# TASK 3: IDENTIFY HIGH PERFORMERS
# ==========================================

# Employees with score >= 7 are high performers
df["High_Performer"] = df["Performance_Score"] >= 7

print("\nUpdated Dataset:")
print(df)


# ==========================================
# TASK 4: COUNT HIGH PERFORMERS
# ==========================================

high_performer_count = df["High_Performer"].sum()

print("\nTotal High Performers:",
      high_performer_count)


# Calculate percentage of high performers
high_performer_percentage = (
    df["High_Performer"].mean() * 100
)

print("High Performer Percentage:",
      high_performer_percentage, "%")


# High performers by department
high_performers_by_department = (
    df.groupby("Department")["High_Performer"]
      .sum()
)

print("\nHigh Performers by Department:")
print(high_performers_by_department)


# ==========================================
# TASK 5: EXPERIENCE VS SALARY
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Years_of_Experience"],
    df["Monthly_Salary"]
)

plt.title("Experience vs Monthly Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Monthly Salary")

plt.grid(alpha=0.3)

plt.show()


# ==========================================
# TASK 6: PERFORMANCE BY DEPARTMENT
# ==========================================

department_performance = (
    df.groupby("Department")["Performance_Score"]
      .mean()
)

print("\nAverage Performance Score by Department:")
print(department_performance)


# Create bar chart

plt.figure(figsize=(8, 5))

plt.bar(
    department_performance.index,
    department_performance.values
)

plt.title("Average Performance Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")

plt.grid(axis="y", alpha=0.3)

plt.show()
