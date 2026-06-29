# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Fatima Jesabel"
age = 25
gpa = 3.2
is_student = True

print(type(is_student)) # Checking the data type of a variable

gpa = int(gpa) # truncating the decimal point and just replacing with integer
print(gpa)

age = float(age) 
print(age)

age = str(age)
print(type(age))

age += "1" # string concatenation
print(age)

name = bool(name) # when there is anything in there it prints True, if empty, False
print(name)