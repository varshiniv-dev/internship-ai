# dictionaries - data is stored in key, value pairs
hobbies = {'movies/series': 'rating', 'outlander': '5/5'}
print(hobbies)

# functions - write once use many times, block of code which performs certain task


def song():  # def- defining function, song-function name, ()-paranthesis
    print("Toxic till the end")  # blockofcode
    # blockofcode


def lyrics():  # def- defining function, greet-function name, ()-paranthesis
    print("Ladies and Gentelmen, I present to you \nTHE EX")  # blockofcode


song()
lyrics()

# function with parameters


def song(name):
    print(f"Toxic till the end - {name}")


song("Rose")  # argument - inside a parameter and a value passed to the function
lyrics()

# ex1


def song(name, age, group):  # different parameters
    print(f"Toxic till the end - {name}")
    print(f"{name} is {age} years old. And she is from {group}")


# argument - inside a parameter and a value passed to the function
song("Rose", 29, "BLACKPINK")
