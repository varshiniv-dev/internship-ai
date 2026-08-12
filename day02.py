# boolean
stu = True
print(type(stu))
x = 5
y = 7
sum = (x+y)
print(type(sum))
print(7 > 3)
print(10 < 0)
print(10 != 10)  # ('!=' not equal to)

# input = taking data from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
# if int is not used while taking input the sum is just going to merge the both values instead of adding the numbers.
sum = num1+num2
print("The sum is: ", sum)

# lists and tuple - collection of elements in single variable
Characters = ["Spiderman", "Iron man", "Captain America",
              "Thor", "Hulk", "Superman", "Superwoman"]  # list
print(Characters)
Character = ("Spiderman", "Iron man", "Captain America",
             "Thor", "Hulk", "Superman", "Superwoman")  # tuple
print(Characters[0])
print(Characters[1])
print(Characters[2])
print(Characters[3])
print(Characters[4])
print(Characters[5])
print(Characters[6])
# print(Character[7]) #throws error because list is out of range and list only contains 0-6.

print(Character[0])

# tuples ar3e immutable but list are mutable.

# slicing
print(Character[0:4])
print(Character[1:-2])
print(Character[0:0])
print(Character[5:-7])
print(Character[2:-4])
