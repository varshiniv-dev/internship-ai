# Q1. personal introduction repeater
Name = input("Enter your name:")
Age = int(input("Enter your age:"))
college_name = input("Enter your college name:")
for i in range(10):
    print("Name: ", Name)
    print("Age: ", Age)
    print("College name: ", college_name)
    print()

# Q2. Welcome to GlowLogics.
stu_names = ['Anil', 'Ahsan', 'Priyanshu', 'Vivek', 'Aryaan']
for student in stu_names:
    print(student + ", Welcome to the GlowLogics Internship Program.")

# Q3. Digital Greeting System
names = ['Bhuvan', 'Hemaang', 'Kurien', 'Mashaal', 'Shayan',
         'Nisman', 'Kruthika', 'Prajaktha', 'Sharanya', 'Yuktha']
for name in names:
    print("Dear, ", name)
    print("We are excited to have you as part of the internship.")
    print("Regards,")
    print("GlowLogics")
    print()

# Q4. Even number challenge
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# for odd
for i in range(1, 101, 2):
    if i % 2 != 0:
        print(i)

# Q5. Attendance register
stu = []
for i in range(6):
    name = input("Enter student name:")
    stu.append(name)
print("\nAttendance:")
for student in stu:
    print(student, "-Present")

# Q6. Secure login system
password = "Glow123"
user_pass = input("Enter the password:")
while user_pass != password:
    print("Incorrect password. Try again!")
    user_pass = input("Enter the password:")
print("Access Granted!")

# Q7. Multiplication table
num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# Q8. Amazon order confirmation
names = []
for i in range(3):
    name = input("Enter your name:")
    names.append(name)
for name in names:
    print("Hello, ", name)
    print("Your order has been successfully placed.")
    print("Thank you for shopping with us.")

# Q9. Countdown timer
print("Countdown Timer:")
for i in range(10, 0, -1):
    print(i)
print("Launch Successful!")

# Q10. Student information collector - use f-string foe clean formatting
name = input("Enter your name:")
age = int(input("Enter your age:"))
college = input("Enter your college name:")
print(f"Student Information:\nName: {name}\nAge: {age}\nCollege: {college}")

# bonus1- movie list in seperte lines
movies = ["Suzume", "Voicemail for isabelle", "My Oxford Year", "Dhurandhar",
          "3-idiots", "MAD", "DON", "Chamak", "Kiss", "A silent voice", "your name"]
for movie in movies:
    print(movie)

# bonus2 - check the number entered is odd or even
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# bonus3 - 3 attempts to enter correct atm pin
PIN = 1234
attempts = 3
while attempts > 0:
    pin = int(input("Enter 4-digit PIN: "))
    if pin == PIN:
        print("Transaction allowed!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. you have {attempts} attempts left.")
if attempts == 0:
    print("Card blocked")
