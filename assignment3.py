# Q1. print name, age, fav color + show type of age
from datetime import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_color = input("Enter your favorite color: ")
print("Name:", name)
print("Age:", age)
print("Favorite Color:", fav_color)
print("Type of Age:", type(age))

# Q2. predict and verify "10"+"10", 10+10, 10+int("10")
print("10" + "10")  # Predicted: "1010", Actual: "1010"
print(10 + 10)      # Predicted: 20, Actual: 20
print(10 + int("10"))  # Predicted: 20, Actual: 20

# Q3. Ask name, birth year, city.  calculate age and print using fstring import timedate for dynamic year calculation
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
city = input("Enter your city: ")
age = datetime.now().year - birth_year
print(f"Name: {name}, Age: {age}, City: {city}")

# Q4. Repeat password prompt until "python123" -> "Access Granted" . initialize pin ="", while pin != "python123"
pin = ""
while pin != "python123":
    pin = input("Enter password: ")
print("Access Granted")

# Q5. List of fruits -> print third fruit -> slice second to fourth
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Third fruit:", fruits[2])
print("Second to fourth fruits:", fruits[1:4])

# Q6. loop through temperatures and print each with "°C"
temperatures = [25, 30, 35, 40]
for temp in temperatures:
    print(f"{temp}°C")

# Q7. Print even numbers from 1 to 20 using for and range()
for i in range(2, 21, 2):
    print(i)

# Q8. positive/negative/zero using if-elif-else
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Q9. Grade based on marks (>=90 A, >=75 B, >=50 C, else D)
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: D")

# Q10. Define gree(name) and call wit three different names


def greet(name):
    print(f"Hello, {name}!")


greet("Ally")
greet("Diya")
greet("Kunal")

# Q11. Function calculate_area(lenght, width) that returns area


def calculate_area(length, width):
    area = length * width
    return area


print(calculate_area(10, 4))

# Q12. Dictionary for book -> print author
book = {
    "title": "Edge of darkness",
    "author": "Leigh Rivers",
    "year": 2023
}
print("Author:", book["author"])

# Q13. Ask user for product name & price -> store in dict -> display
product = {}
product["name"] = input("Enter product name: ")
product["price"] = float(input("Enter product price: "))
print("Product Name:", product["name"])
print("Product Price:", product["price"])

# Q14. Fix the bio_data(25, "Ravi", "Mumbai")


def bio_data(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


bio_data(age=25, name="Ravi", city="Mumbai")


# Q15. Employee directory using dictionary + while loop + for loop
employee_directory = {}
while True:
    name = input("Enter employee name (or 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    position = input("Enter employee position: ")
    employee_directory[name] = position
for name, position in employee_directory.items():
    print(f"Name: {name}, Position: {position}")
