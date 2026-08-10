# ==========================================
# CASE STUDY 2 - STUDENT OUTCOMES ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("student_performance_dataset.csv")

# ==========================================
# Display Dataset Information
# ==========================================

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATA INFO ==========")
print(df.info())

print("\n========== SUMMARY ==========")
print(df.describe())

# ==========================================
# TASK 1
# Average Marks
# ==========================================

average_marks = df["Marks"].mean()

print("\n========== TASK 1 ==========")
print(f"Average Marks: {average_marks:.2f}")

# ==========================================
# TASK 2
# Students scoring above 75
# ==========================================

high_performers = df[df["Marks"] > 75]

print("\n========== TASK 2 ==========")
print("\nStudents Scoring Above 75:")
print(high_performers[["Student_ID", "Name", "Marks"]])
print(f"\nNumber of High Performers: {len(high_performers)}")

# ==========================================
# TASK 3
# Correlation Analysis
# ==========================================

correlation = df["Attendance_Percentage"].corr(df["Marks"])

print("\n========== TASK 3 ==========")
print(f"Correlation Coefficient: {correlation:.3f}")

if correlation > 0:
    print("Higher attendance is associated with higher marks.")

elif correlation < 0:
    print("Higher attendance is associated with lower marks.")

else:
    print("No correlation exists.")

# ==========================================
# TASK 4
# Create Pass Column
# ==========================================

df["Pass"] = df["Marks"] >= 50

print("\n========== TASK 4 ==========")
print(df[["Student_ID", "Name", "Marks", "Pass"]])

# ==========================================
# TASK 5
# Pass / Fail Summary
# ==========================================

pass_count = df["Pass"].sum()
fail_count = (~df["Pass"]).sum()

print("\n========== TASK 5 ==========")
print(f"Pass Students : {pass_count}")
print(f"Fail Students : {fail_count}")

pass_percentage = (pass_count / len(df)) * 100

print(f"Pass Percentage : {pass_percentage:.2f}%")

# ==========================================
# TASK 6
# Histogram
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Marks"],
    bins=8,
    edgecolor="black"
)


plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True)

plt.show()

# ==========================================
# BUSINESS SUMMARY
# ==========================================

print("\n========== BUSINESS SUMMARY ==========")

print(f"Average Marks            : {average_marks:.2f}")
print(f"Students Above 75 Marks  : {len(high_performers)}")
print(f"Pass Students            : {pass_count}")
print(f"Fail Students            : {fail_count}")
print(f"Correlation              : {correlation:.3f}")

print("\nRecommendations")

print("1. Continue supporting high-performing students.")
print("2. Provide extra coaching for students scoring below 50.")
print("3. Analyze additional factors besides attendance that may influence marks.")
print("4. Monitor student performance regularly.")
