# Objective 6: 
# How do argumented Assingments work? 
# Argumented assignments: Combine a binary operationd with and assignment in one step, taking a variable, applying an operation to it with another value, and storing the result back into the same variable
    # in other languages they are the addition and substraction assignment operators += or -=

# Simple Syntax: variable <operator>= value
    # adding assignment operator
my_var = 10
my_var += 5
print(my_var) # 15
    # subtracting assignment operator
count = 14
count -= 3
print(count) # 455
    # Multiplication assignment operator
product = 65
product *= 7
    # dividing assignment operator
price = 100
price /= 4
print(price) # 25.0
    # Floor division assignment operator
total_pages = 23
total_pages /= 5
print(total_pages) # 4
    # Modulus assignment operator
bits = 35
bits %= 2
print(bits) # 1
    # Exponentiation assignemtn operator
power = 2
power **= 3
print(power) # 8

# Unsing strings with argumented assignment operators:
    # addition assignment operator makes it easy to concatonate strings
greet = 'Hello'
greet += 'World'
print(greet) # Hello World
    # multiplication assignment operator can be used to repeat a string
greet = 'Hello'    
greet *= 3
print(greet) # helloHelloHello
    # Other argumented assignments throw a TypeError whe you use the with strings, like substraction and division
greet = 'Hello'
greet -= 'World'
print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'

greet = 'Hello'
greet /= 'World'
print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 

# Note that adding additional pluses like in C language doesn't work in python 
my_var = 5
# print(+++my_var) # 5 THIS DOES NOT WORK, it will NOT give you 8!
    # You have to manually do the assignment operator       
my_var += 1
print(my_var) # 6, THIS WORKS!

