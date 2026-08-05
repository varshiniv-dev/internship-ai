# Casestudy2


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("student_performance_dataset.csv")
# Explore dataset
print(df.head())
print(df.info())
print(df.describe())
# Check duplicates
print(df["Student_ID"].duplicated().sum())
df.drop_duplicates(subset=["Student_ID"], keep="first", inplace=True)
# Handle missing values (only for dirty dataset)
df.dropna(subset=["Name", "Marks", "Attendance_Percentage"], inplace=True)
# Fix outliers (dirty dataset only)
df.loc[df["Age"] > 100, "Age"] = df["Age"].median()
df.loc[df["Marks"] < 0, "Marks"] = df["Marks"].mean()
df.loc[df["Attendance_Percentage"] > 100, "Attendance_Percentage"] = 100


# 1. Average Marks
average_marks = df["Marks"].mean()
print(f"Average Marks: {average_marks:.2f}")
# 2. High Performers
high = df[df["Marks"] > 75]
print("Students above 75:", len(high))
# 3. Correlation Analysis
correlation = df["Attendance_Percentage"].corr(df["Marks"])
print(f"Correlation: {correlation:.3f}")
if correlation > 0:
print("Higher attendance is associated with higher marks.")
elif correlation < 0:
print("Higher attendance is associated with lower marks.")
else:
print("No correlation.")
# 4. Feature Engineering
df["Pass"] = df["Marks"] >= 50
# 5. Pass / Fail Summary
print("Pass:", df["Pass"].sum())
print("Fail:", (~df["Pass"]).sum())
# 6. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["Marks"], bins=10, kde=True)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()
