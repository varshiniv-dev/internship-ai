# Q1. Student introduction system
name = input("Enter you name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
dept = input("Enter your course name: ")
print("STUDENT PROFILE")
print()
print(
    f"Hello I am {name}, I am {age} years old. I am currently studying {dept} in {college}")
print()

# Q2. Internship registration form
f_name = input("Enter your full name: ")
email = input("Enter your email address: ")
phno = input("Enter your mobile number: ")
city = input("Enter your city: ")
print(f"Thankyou {f_name}! \n Your internship registration has been completed successfully. \n Email: {email}\n City: {city}")

# Q3. Simple calculator
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
add = num1+num2
sub = num1-num2
mul = num1*num2
if num2 != 0:
    div = num1/num2
else:
    div = "Undefined: Cannot divide by zero"
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)

# Q4. Age after 10 years
curr_age = int(input("Enter your current age: "))
age_10 = curr_age+10
print(f"You are currently {curr_age}. in 10 years you will be {age_10}")

# Q5. Favorite Movies collection
movies = []
for i in range(5):
    movie = input("Enter movie name: ")
    movies.append(movie)
print("All Movies:", movies)
print("First Movie:", movies[0])
print("Last Movie:", movies[-1])
print("Total Movies:", len(movies))

# Q6. Student welcome system
stu = ["Tony", "Tom", "Jack", "Zavir", "Josua",
       "Addie", "Jake", "Kevin", "San", "Jamie"]
for i in stu:
    print(f"Welcome {i}")

# Q7. Attendance register
students = ["Siri", "Google", "OpenAI", "Chat", "Hello"]
for i in range(len(students)):
    print(i+1, students[i])

# Q8. Voting Eligibility checker
age1 = int(input("Enter your age:"))
if age1 >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

# Q9. Grade calculator
marks = int(input("Enter your marks:"))
if marks >= 90:
    print("A grade")
elif 70 <= marks <= 89:
    print("B grade")
elif 50 <= marks <= 69:
    print("C grade")
elif marks < 50:
    print("D grade")

# Q10. Login verification system
username = "admin"
name = input("Enter the username: ")
if (username == name):
    print("Login Successfull!")
else:
    print("Invalid Username ")


# Q11. Print your name 20 times
name = "Starlight"
for i in range(20):
    print(name)

# Q12. Even number generator
for i in range(1, 50):
    if (i % 2 == 0):
        print(i)

# Q13. Multiplication table generator
num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "X", i, "=", num*i)

# Q14. Password verification system
while True:
    password = input("Enter password: ")
    if password == "1234":
        print("Access Granted!")
        break
    else:
        print("Incorrect Password")

# Q15. Personalized greeting system
name = input("Enter your name:")
course = input("Enter your interested course: ")
print(f"Hello {name}, Welcome to the {course} course!")

# Q16. Shopping Bill generator
product = input("Enter the product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
cost = quantity * price
print("Total cost: ", cost)

# Q17. Student bio-data
bio_data = {"Name": "Ansh", "Age": "23",
            "Course": "Architect", "College": "Oxford", "Year": "2nd"}
print(bio_data)

# Q18.Access dictionary values
bio_data = {"Name": "Ansh", "Age": "23", "Course": "Architect",
            "Branch": "Residential", "College": "Oxford", "Year": "2nd"}
print("Name: ", bio_data["Name"])
print("College: ", bio_data["College"])
print("Branch: ", bio_data["Branch"])

# Q19. Update information
bio_data = {"Name": "Ansh", "Age": "23", "Course": "Architect",
            "College": "Oxford", "Year": "2nd", "City": "Los-angels"}
bio_data["City"] = "Malibu"
print(bio_data)

# Q20. Add additional info
bio_data = {"Name": "Ansh", "Age": "23",
            "Course": "Architect", "College": "Oxford", "Year": "2nd"}
bio_data["Email"] = "ansh@email.com"
bio_data["PhNo"] = "9876543210"
print(bio_data)

# Q21. Digital ID card generator
id_data = {
    "Name": "Alex Raein",
    "ID": "01IS89207",
    "Course": "B.Tech in Information Science",
    "Year": "2023-2027",
    "Blood_Group": "A+",
    "College": "Stanford University"
}
id_card = f""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{id_data['College'].upper()}
DIGITAL STUDENT ID 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ID Number : {id_data['ID']}
Name      : {id_data['Name']}
Course    : {id_data['Course']}
Year      : {id_data['Year']}
Blood Grp : {id_data['Blood_Group']}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print(id_card)

# MINI PROJECT-1 : Amazon user profile

print("~~~~~~~~AMAZON USER PROFILE~~~~~~~~")
name = input("Enter your name: ")
email = input("Enter your email: ")
city = input("Enter your city: ")
orders = int(input("Enter number of orders: "))
prime = input("Are you a prime member?(Yes/No): ")
print("\n~~~~~~~~~~~~USER DASHBOARD~~~~~~~~~~~~")
print("Name: ", name)
print("Email: ", email)
print("City: ", city)
print("Orders: ", orders)
print("Prime membership: ", prime)
if prime.lower() == "yes":
    print("\nWelcome,", name, "!")
    print("Thankyou for being an Amazon Prime Member.")
    print("Enjoy fast delivery and exclusive offers!")
else:
    print("\nWelcome,", name, "!")
    print("Upgrade to Amazon Prime to enjoy exclusive benefits.")

# MINI PROJECT-2 : Student Management System
print("~~~~~~~~STUDENT MANAGEMENT SYSTEM~~~~~~~~")
student = {}
student["Name"] = input("Enter student name: ")
student["USN"] = input("Enter USN: ")
student["Age"] = input("Enter Age: ")
student["Dept"] = input("Enter Department: ")
student["Sem"] = input("Enter Semester: ")
student["College"] = input("Enter College name: ")

print("~~~~~~~~~~~~~STUDENT PROFILE~~~~~~~~~~~~~")
print("Name       :", student["Name"])
print("USN        :", student["USN"])
print("Age        :", student["Age"])
print("Department :", student["Dept"])
print("Semester   :", student["Sem"])
print("College    :", student["College"])

# Bonus - Student database system
students = [
    {
        "Name": "Varshini",
        "Age": 19,
        "College": "GMIT",
        "Department": "CSE"
    },
    {
        "Name": "Sai",
        "Age": 20,
        "College": "MIT",
        "Department": "ECE"
    },
    {
        "Name": "Ananya",
        "Age": 19,
        "College": "PES",
        "Department": "ISE"
    },
    {
        "Name": "Rahul",
        "Age": 21,
        "College": "RVCE",
        "Department": "CSE"
    },
    {
        "Name": "Priya",
        "Age": 20,
        "College": "BMS",
        "Department": "AIML"
    }
]
print("Student Names:")
for student in students:
    print(student["Name"])
print("\nComplete Student Information:\n")
for student in students:
    print("Name:", student["Name"])
    print("Age:", student["Age"])
    print("College:", student["College"])
    print("Department:", student["Department"])
    print("---------------------------")
