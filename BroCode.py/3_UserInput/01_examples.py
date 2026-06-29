# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # convert to int so we can increment

age += 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!") # use f string only if you want to insert variables
print(f"You are {age} years old")
