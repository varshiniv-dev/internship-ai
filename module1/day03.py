# dynamic typing -data type of the variable is determined automatically
# variable assignment - assigning a value to the variable using assignment operator '='
name = ("Varsh")
age = 19.7
dept = ("CSE")
name = "CSE"
print(name)  # prints CSE not Varsh becz of variable reassignment

# logical Operators- AND, OR
x = 4
y = 6
z = 10
print(x+y)
print(((x+y > 5) and (x+z < 5)))
print(((x+y > 5) or (x+z < 5)))

# conditional statements
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")  # true
else:
    print("Not eligible")  # false

# voting..
age1 = int(input("Enter your age:"))
if age1 < 0:
    print("Enter correct age!")
elif age1 < 18:
    print("You cannot vote!")
elif 18 <= age1 <= 30:
    print("You are young voter!")
elif 31 <= age1 <= 60:
    print("You are elder voter!")
else:
    print("You are senior voter!")

# student marks..
marks = int(input("Enter your marks:"))
if marks >= 90:
    print("A grade")
elif marks >= 70:
    print("B grade")
elif marks >= 50:
    print("C grade")
elif marks >= 30:
    print("D grade")
else:
    print("Fail!")
