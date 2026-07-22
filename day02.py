# boolean
stu = True
print(type(stu))
x = 5
y = 7
sum = (x+y)
print(type(sum))

# input = taking data from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
# if int is not used while taking input the sum is just going to merge the both values instead of adding the numbers.
sum = num1+num2
print("The sum is: ", sum)

# lists and tuple - collection of elements in single variable
Characters = {"Spiderman", "Iron man", "Captain America",
              "Thor", "Hulk", "Superman", "Superwoman"}  # list
print(Characters)
Character = ["Spiderman", "Iron man", "Captain America",
             "Thor", "Hulk", "Superman", "Superwoman"]  # tuple
print(Character[0])
print(Character[1])
print(Character[2])
print(Character[3])
print(Character[4])
print(Character[5])
print(Character[6])
# print(Character[7]) #throws error because list is out of range and list only contains 0-6.

Character[0] = "Spider-man"
print(Character[0])

# tuples can be changed but list cannot be changed.

# slicing
print(Character[0:4])
print(Character[1:-2])
print(Character[0:0])
print(Character[5:-7])
print(Character[2:-4])
