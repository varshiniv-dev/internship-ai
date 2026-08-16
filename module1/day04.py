# loops- for, while
name = "varsh"
for i in range(5):  # i is temporary variable
    print(i, name)

students = ['ayan', 'aryan', 'arush']
for i in students:
    print("Hello ", i)
# inside the loop, statement will print i times. outside loop only prints one time.
print("Welcome to my github!")

# while - repeating till the condition meets
pin = ""
while pin != "1234":
    pin = input("Enter the PIN: ")
print("Phone  unlocked")

# print even numbers
for i in range(10):
    if (i % 2 == 0):
        print(i)

# formatted strings
name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter your course name:")
print(f"My name is {name}. I am {age} years old and now stuyding {course}.")
