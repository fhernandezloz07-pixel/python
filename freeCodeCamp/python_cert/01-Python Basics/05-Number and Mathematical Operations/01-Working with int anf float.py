# Objective 5
# How do you work with integers and floating point Numbers?
# Integers and floats are the primary numeric data types in python. You can store numeric data and perform mathematical operations with them

# Integers: Whole numbers without decimal points, either positive or negative:
my_int_1 = 56
my_int_2 = -4
print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>
    # Performing an operation with integers (addition)
my_int_1 = 56
my_int_2 = 12
sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68
    # Performing an operation with integers (subtraction)
my_int_1 = 56
my_int_2 = 12
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44
    # Performing an operation with integers (multiplication)
my_int_1 = 12
my_int_2 = 4
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48
    # Performing an operation with integers (division)
my_int_1 = 56
my_int_2 = 12
div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667

# Floats: Positive or negative numbers with decimal points like 3.14, -0.5, or 0.0
my_float_1 = -12.0
my_float_2 = 4.9
print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
    # Performing an operation with float (addition)
my_float_1 = 5.4
my_float_2 = 12.0
float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4
    # Performing an operation with float (subtraction)
my_float_1 = 5.4
my_float_2 = 12.0
float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6
    # Performing an operation with float (division)
my_float_1 = 5.4
my_float_2 = 12.0
float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001
    # Performing an operation with float (division)
my_float_1 = 5.4
my_float_2 = 12.0
float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222

# If you add an integer and a float, the result is automatically converted to a float: 
my_int = 56
my_float = 5.4
sum_int_and_float = my_int + my_float # 61.4
print(sum_int_and_float) # <class 'float'>
    # This is true for other arithmetic operations like subtraction, multiplication, and division. Always a float reult. 

# Modulo operator: returns the remainder when the value on the left is divided by the value on the right, and it is represented by %
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1
print('Integer Modulus:', mod_ints) # Integer Modulus: 8
print('Float Modulus:', mod_floats) # Float Modulus: 1.1999999999999993

# Floor division divides two numbers and returns the greatest integer less than or equal to the result, done with //
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1
print('Integer Floor Division:', floor_div_ints) #Integer Floor Division: 4, because 56/12 = 4.6666666667
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0, because 12/5.4 = 2.2222222222

# Exponentiation: Raises a number to the power of antother, and is done with **
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2
print('integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation;', exp_floats) # Float Exponentiation: 614787626.1765089

# float() : Function that returns a foationg-point number constructed from the givern number (convreting either numberic data or strings into integer or floats)
my_int_1 = 56
my_float_1 = float(my_int_1)
print(my_float_1) # 56.0
print(type(my_float_1)) # <class 'float>

# int() : function that returns an integer constructed from the given number: 
my_float = 12.92563
my_int = int(my_float)
print(my_int) # 12
print(type(my_int)) # <class 'int'>
    # You can use the same logic to convert a stirng into either a float or an integer
my_str_int = '45'
my_str_float = '7.8'
converted_int = int(my_str_int)
converted_float = float(my_str_float)
print(converted_int, type(converted_int)) # 45 <class 'int'>
print(converted_float, type(converted_float)) # 7.8 <class 'float'>

# round() : Rounds a number to the specified number of decimal places. By default this function rounds the nearest integer, and returns a whole number with no decimal places:
my_int_1 = 4.798
my_int_2 = 4.256
rounded_int_1 = round(my_int_1) # This is the default that will round it to the nearest whole number
rounded_int_2 = round(my_int_2, 1) # the 1 after indicates how many deciamal places you actually want to keep when rounding 
print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# abs() : returns the absolute value of a number 
num = -15
absolute_value = abs(num)
print(absolute_value) # 15

# pow() : raises a number to the nearest power of another or performs modular exponentiation.
result_1 = pow(2, 3) # Equivalent to 2 ** 3
print(result_1) # 8
result_2 = pow(2, 3, 5) # (2 ** 3) % 5
print(result_2) # 3

