# STUDENT INFORMATION DATASET ANALYSIS

# Import the pandas library for data analysis
import matplotlib.pyplot as plt
import pandas as pd

# LOAD THE DATASET

# Read the pipe-separated (|) CSV file
df = pd.read_csv("Student_Data.csv", sep="|")

# Remove extra quotation marks from the column names
df.columns = df.columns.str.replace('"', '', regex=False)

# DISPLAY BASIC INFORMATION

# Display the first 5 rows of the dataset
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Display information about the dataset
print("\n========== DATASET INFORMATION ==========")
print("\nDataset Shape:", df.shape)

# Display statistical summary of all columns
print("\n========== SUMMARY STATISTICS ==========")
print(df.describe(include="all").T)

# Display all column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# CHECK FOR MISSING VALUES

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# CHECK FOR DUPLICATE STUDENT IDs

duplicates = df["Student ID"].duplicated().sum()

print("\n========== DUPLICATE STUDENT IDs ==========")
print("Duplicate Student IDs:", duplicates)

# Remove duplicate records if any exist
df.drop_duplicates(
    subset=["Student ID"],
    keep="first",
    inplace=True
)

# TOTAL NUMBER OF STUDENTS

print("\n========== TOTAL STUDENTS ==========")
print("Total Students:", len(df))

# STUDENTS LIVING IN EACH RESIDENCE HALL

print("\n========== STUDENTS BY RESIDENCE HALL ==========")
print(df["Address 3"].value_counts())

# CHECK MISSING PHONE NUMBERS

print("\n========== MISSING PHONE NUMBERS ==========")

print("Missing Phone 1:",
      df["Phone 1"].isnull().sum())

print("Missing Phone 2:",
      df["Phone 2"].isnull().sum())

print("Missing Phone 3:",
      df["Phone 3"].isnull().sum())

# STUDENTS HAVING MULTIPLE PHONE NUMBERS

students_multiple_numbers = df["Phone 3"].notna().sum()

print("\n========== MULTIPLE PHONE NUMBERS ==========")
print("Students with a third phone number:",
      students_multiple_numbers)

# STUDENTS WITH SECONDARY ADDRESS

secondary_address = df["Address 2"].notna().sum()

print("\n========== SECONDARY ADDRESS ==========")
print("Students having a second address:",
      secondary_address)

# STUDENTS HAVING EMAIL ADDRESS

email_count = df["E-mail Address"].notna().sum()

print("\n========== EMAIL INFORMATION ==========")
print("Students with Email IDs:",
      email_count)

# STUDENTS BY CAMPUS MAIL BOX

print("\n========== CAMPUS MAIL BOXES ==========")
print(df["Address 4"].value_counts())

# VISUALIZATION


# Count students in each residence hall
hall_counts = df["Address 3"].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    hall_counts.index,
    hall_counts.values,
    edgecolor="black"
)

plt.title("Students by Residence Hall")
plt.xlabel("Residence Hall")
plt.ylabel("Number of Students")

plt.xticks(rotation=45)

plt.grid(axis="y", alpha=0.5)

plt.tight_layout()

plt.show()

# BUSINESS SUMMARY

print("\n========== BUSINESS SUMMARY ==========")

print(f"Total Students               : {len(df)}")
print(f"Duplicate Student IDs        : {duplicates}")
print(f"Students with Email IDs      : {email_count}")
print(f"Students with Phone 3        : {students_multiple_numbers}")
print(f"Students with Address 2      : {secondary_address}")

print("\n========== RECOMMENDATIONS ==========")

print("1. Maintain unique Student IDs to avoid duplicate records.")
print("2. Encourage students to keep contact details updated.")
print("3. Verify missing phone numbers and addresses.")
print("4. Use residence hall information for accommodation planning.")
print("5. Regularly validate student records for better data quality.")
