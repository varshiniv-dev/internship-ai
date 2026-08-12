# python basics
# variables
name = "Varshini"
age = 19
marks = 85.5
is_student = True

# datatypes
name = "Varshini"     # str
age = 19              # int
marks = 85.5          # float
is_student = True     # bool

# to check the type of datatype
print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))

# input- it always returns string
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert to int
marks = float(input("Enter your marks: "))  # convert to float
is_student = input("Are you a student? (yes/no): ") == "yes"  # convert to bool
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Is Student:", is_student)

# two numbers and print their sum
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
sum = a + b
print("The sum of", a, "and", b, "is:", sum)

# operators
# arithmetic operators
x = 10
y = 3
print("x + y =", x + y)  # addition
print("x - y =", x - y)  # subtraction
print("x * y =", x * y)  # multiplication
print("x / y =", x / y)  # division
print("x // y =", x // y)  # floor division
print("x % y =", x % y)  # modulus
print("x ** y =", x ** y)  # exponentiation
# comparison operators
p = 5
q = 10
print("p > q =", p > q)  # greater than
print("p < q =", p < q)  # less than
print("p == q =", p == q)  # equal to
print("p != q =", p != q)  # not equal to
print("p >= q =", p >= q)  # greater than or equal to
print("p <= q =", p <= q)  # less than or equal to
# logical operators
a = True
b = False
print("a and b =", a and b)  # logical AND
print("a or b =", a or b)  # logical OR
print("not a =", not a)  # logical NOT

# conditional statements
if p > q:
    print("p is greater than q")
elif p < q:
    print("p is less than q")
else:
    print("p is not greater than q")

# another example-
marks = 75
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# loops
# for loop
for i in range(5):
    print(i)

# example
total = 0
for i in range(1, 11):
    total += i
print("The sum of numbers from 1 to 10 is:", total)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# functions


def greet():
    print("Hello, World!")


greet()

# function with parameters


def greet(name):
    print("Hello,", name + "!")


greet("Alice")
# example


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


number = int(input("Enter number: "))
print(check_even(number))

# lists
fruits = ["apple", "banana", "orange"]
print(fruits)
# add, remove, length, loop, max, min, sum, sort, reverse, index, count, slicing
fruits.append("grape")
print(fruits)
fruits.remove("banana")
print(fruits)
print("Length of the list:", len(fruits))
print("Maximum fruit:", max(fruits))
print("Minimum fruit:", min(fruits))
print("Sum of numbers:", sum([1, 2, 3, 4, 5]))
print("Sorted list:", sorted(fruits))
fruits.reverse()
print("Reversed list:", fruits)
for fruit in fruits:
    print(fruit)
print("Index of 'orange':", fruits.index("orange"))
print("Count of 'apple':", fruits.count("apple"))
print("Sliced list:", fruits[1:3])  # Slicing from index 1 to 2
print("Sliced list with step:", fruits[::2])  # Slicing with step of 2
fruits[1] = "kiwi"  # Modifying an element
print("Modified list:", fruits)
fruits.insert(1, "mango")  # Inserting an element at index 1
print("List after insertion:", fruits)

# dictionaries - add, update, loop, keys, values, items, get, pop, popitem, clear
student = {
    "name": "Varshini",
    "age": 19,
    "marks": 85.5,
    "is_student": True
}
print(student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])
print("Is Student:", student["is_student"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
student["age"] = 20  # Update age
print("Updated age:", student["age"])
student["grade"] = "A"  # Add new key-value pair
print("Added grade:", student["grade"])
print("Get marks using get():", student.get("marks"))
student.pop("is_student")  # Remove key-value pair
print("After removing is_student:", student)
student.popitem()  # Remove last inserted key-value pair
print("After popitem:", student)
student.clear()  # Remove all key-value pairs
print("After clear:", student)

# strings -indexing, slicing, concatenation, formatting, methods
text = "Hello, World!"
print("Original text:", text)
print("First character:", text[0])  # Indexing
print("Last character:", text[-1])  # Negative indexing
print("Sliced text:", text[0:5])  # Slicing
print("Concatenated text:", text + " How are you?")  # Concatenation
print("Uppercase text:", text.upper())  # Uppercase
print("Lowercase text:", text.lower())  # Lowercase
print("Title case text:", text.title())  # Title case
print("Count of 'o':", text.count("o"))  # Count occurrences
print("Find 'World':", text.find("World"))  # Find substring
print("Replace 'World' with 'Python':", text.replace(
    "World", "Python"))  # Replace substring

# sets
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers.add(10)
numbers.remove(5)
print(numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# practise questions- 1. Add two numbers
# 2. Find largest of two numbers
# 3. Find largest of three numbers
# 4. Check even/odd
# 5. Check positive/negative
# 6. Calculate factorial
# 7. Generate multiplication table
# 8. Reverse a number
# 9. Check palindrome
# 10. Check prime number
# 11. Generate Fibonacci series
# 12. Find sum of digits
# 13. Count digits
# 14. Find maximum in a list
# 15. Find minimum in a list
# 16. Sort a list
# 17. Count vowels in a string
# 18. Reverse a string
# 19. Create a dictionary of student details
# 20. Write functions for common operations

# 1- Add two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
sum = a + b
print("The sum of", a, "and", b, "is:", sum)
# 2 - Find largest of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is the largest number.")
elif num2 > num1:
    print(num2, "is the largest number.")
else:
    print("Both numbers are equal.")
# 3 - Find largest of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")

# 4 - Check even/odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
# 5 - Check positive/negative
number = float(input("Enter a number: "))
if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")
else:
    print("The number is zero.")
# 6 - Calculate factorial


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# 7 - Generate multiplication table
number = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# 8 - Reverse a number
number = int(input("Enter a number to reverse: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit
    number //= 10
print("Reversed number:", reverse)
# 9 - Check palindrome
number = int(input("Enter a number to check if it's a palindrome: "))
original_number = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit
    number //= 10
if original_number == reverse:
    print(original_number, "is a palindrome.")
else:
    print(original_number, "is not a palindrome.")
# 10 - Check prime number
number = int(input("Enter a number to check if it's prime: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")
# 11 - Generate Fibonacci series
number = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(number):
    print(a, end=" ")
    a, b = b, a + b
# 12 - Find sum of digits
number = int(input("Enter a number to find the sum of its digits: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("Sum of digits:", sum_of_digits)
# 13 - Count digits
number = int(input("Enter a number to count its digits: "))
count = 0
while number > 0:
    count += 1
    number //= 10
print("Number of digits:", count)
# 14 - Find maximum in a list
numbers = [int(x)
           for x in input("Enter numbers separated by spaces: ").split()]
max_number = max(numbers)
print("Maximum number:", max_number)
# 15 - Find minimum in a list
numbers = [int(x)
           for x in input("Enter numbers separated by spaces: ").split()]
min_number = min(numbers)
print("Minimum number:", min_number)
# 16 - Sort a list
numbers = [int(x)
           for x in input("Enter numbers separated by spaces: ").split()]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)
# 17 - Count vowels in a string
text = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
# 18 - Reverse a string
text = input("Enter a string to reverse: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
# 19 - Create a dictionary of student details
student = {
    "name": input("Enter student's name: "),
    "age": int(input("Enter student's age: ")),
    "marks": float(input("Enter student's marks: ")),
    "is_student": input("Is the student enrolled? (yes/no): ").lower() == "yes"
}
print("Student Details:", student)
# 20 - Write functions for common operations


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
