# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Variables
first_name = "Fatima"
food = "bananas"
email = "Fatima123@fake.com"

# Simply printing a variable
print(first_name)

# Another way to print by insering variables into sentences
print(f"Hello {first_name}") # f means format
print(f"You like {food}")
print(f"Your email is: {email}")


# Integers 
#        don't add quotes, then they would turn into strings
age = 25
quantity = 3
num_students = 30

print(f"Your are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_students} students")


# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")


# Boolean 
#       -> Either true or false
is_student = True
for_sale = False
is_online = True

print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a stundent")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")