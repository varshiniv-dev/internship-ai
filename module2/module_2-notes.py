# 4 main libraries - NumPy, Pandas, Matplotlib, Seaborn
# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy as np  # numerical operations
import pandas as pd  # data  manipulation
import matplotlib.pyplot as plt  # visualization
import seaborn as sns  # statistical data visualization
# read csv file
df = pd.read_csv("Student_Data.csv")
df
df.columns  # Display the column names of the DataFrame
df.shape  # Display the shape of the DataFrame
df.info()  # Display information about the DataFrame
df.describe()  # Display summary statistics of the DataFrame
df.head()  # Display the first 5 rows of the DataFrame
df.tail()  # Display the last 5 rows of the DataFrame
df.isnull().sum()  # Check for missing values in the DataFrame
df.duplicated().sum()  # Check for duplicate rows in the DataFrame
df["Student ID"].duplicated().sum()  # Check for duplicate Student IDs
# Remove duplicate Student IDs
df.drop_duplicates(subset=["Student ID"], keep="first", inplace=True)
df.dropna()  # Remove rows with missing values
df["Student ID"].nunique()  # Count the number of unique Student IDs
# Count the number of students living in each residence hall
df["Address 3"].value_counts()
# Create a bar plot of students by residence hall
df["Address 3"].value_counts().plot(kind="bar")
# filtering, sorting, groupby, aggregation, merging, joining, concatenation, pivot tables, reshaping, and data cleaning
# Filter the DataFrame for specific Student IDs
df_filtered = df[df["Student ID"].isin([1, 2, 3])]
df_filtered  # Display the filtered DataFrame
# Sort the DataFrame by Student ID
df_sorted = df.sort_values(by="Student ID", ascending=True)
df_sorted  # Display the sorted DataFrame
# Group the DataFrame by residence hall and count Student IDs
df_grouped = df.groupby("Address 3").agg({"Student ID": "count"})
df_grouped  # Display the grouped DataFrame
# Merge the original DataFrame with the grouped DataFrame
df_merged = pd.merge(df, df_grouped, on="Address 3", how="left")
df_merged  # Display the merged DataFrame
# Join the original DataFrame with the grouped DataFrame
df_joined = df.join(df_grouped, on="Address 3", how="left")
df_joined  # Display the joined DataFrame
# Concatenate the original DataFrame with the grouped DataFrame
df_concat = pd.concat([df, df_grouped], axis=1)
df_concat  # Display the concatenated DataFrame
# Create a pivot table of students by residence hall
df_pivot = df.pivot_table(
    index="Address 3", values="Student ID", aggfunc="count")
df_pivot  # Display the pivot table
print(df_pivot)  # Print the pivot table
print(df["Student ID"].sum())  # Calculate the sum of Student IDs
print(df["Student ID"].mean())  # Calculate the mean of Student IDs
print(df["Student ID"].median())  # Calculate the median of Student IDs
print(df["Student ID"].mode())  # Calculate the mode of Student IDs
# Calculate the standard deviation of Student IDs
print(df["Student ID"].std())
# line chart
plt.figure(figsize=(10, 6))
plt.plot(df["Student ID"], df["Address 3"],
         marker="o", linestyle="-", color="b")
plt.title("Line Chart of Student IDs by Residence Hall")
plt.xlabel("Student ID")
plt.ylabel("Residence Hall")
plt.grid()
plt.show()
# bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Address 3"], df["Student ID"], color="orange")
plt.title("Bar Chart of Student IDs by Residence Hall")
plt.xlabel("Residence Hall")
plt.ylabel("Student ID")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()
# histogram
plt.figure(figsize=(10, 6))
plt.hist(df["Student ID"], bins=10, color="green", edgecolor="black")
plt.title("Histogram of Student IDs")
plt.xlabel("Student ID")
plt.ylabel("Frequency")
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()
# count plot, box plot, scatter plot, pair plot, heatmap, violin plot, swarm plot, joint plot, rug plot, kde plot, lm plot, facet grid, cat plot, and reg plot
sns.countplot(x="Address 3", data=df, palette="Set2")
plt.show()
sns.boxplot(x="Address 3", y="Student ID", data=df, palette="Set3")
plt.show()
sns.scatterplot(x="Student ID", y="Address 3", data=df,
                hue="Address 3", palette="Set1")
plt.show()
sns.pairplot(df, hue="Address 3", palette="Set2")
plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
sns.violinplot(x="Address 3", y="Student ID", data=df, palette="Set2")
plt.show()
sns.swarmplot(x="Address 3", y="Student ID", data=df, palette="Set1")
plt.show()
sns.jointplot(x="Student ID", y="Address 3", data=df,
              kind="scatter", color="purple")
plt.show()
sns.rugplot(df["Student ID"], color="blue")
plt.show()

# correlation
df.corr(numeric_only=True)  # Calculate the correlation matrix of the DataFrame
# Create a heatmap of the correlation matrix
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

# exploratory Data Analysis (EDA)
# business insights

# example for student_performance.csv
# 1. Import libraries
# 2. Load dataset
df = pd.read_csv("student_performance.csv")
# 3. Understand dataset
print(df.head())
print(df.shape)
print(df.columns)
df.info()
# 4. Check missing values
print(df.isnull().sum())
# 5. Statistical summary
print(df.describe())
# 6. Remove/fill missing values if necessary
df = df.dropna()
# 7. Filtering
high_performers = df[df["Marks"] >= 80]
print(high_performers)
# 8. Sorting
top_students = df.sort_values("Marks", ascending=False).head(10)
print(top_students)
# 9. Grouping
print(df.groupby("Gender")["Marks"].mean())
# 10. Visualization
sns.histplot(df["Marks"])
plt.title("Distribution of Student Marks")
plt.show()
# 11. Relationship
sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.title("Study Hours vs Marks")
plt.show()
# 12. Correlation
print(df.corr(numeric_only=True))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# 5 case studies-
# 1. Student Performance
# You analyze:
# marks
# performance
# top/low performers
# grouping
# visualization
# recommendations
# 2. Movie Analysis
# You analyze:
# ratings
# genres
# revenue
# budget
# popularity
# trends
# 3. E-Commerce
# You analyze:
# sales
# customers
# revenue
# products
# regions
# profitability
# 4. HR Analytics
# You analyzise:
# employees
# attrition
# departments
# salary
# satisfaction
# workforce trends
# 5. Healthcare
# You analyze:
# patients
# healthcare trends
# diseases
# demographics
# visualizations
# healthcare insights
