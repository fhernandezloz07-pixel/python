# indexing = acessing elements of a sequence using [] (indexing operator)
#            [start: end: step]

credit_number = "1234-5678-9012-3456"

# first character within the string
print(credit_number[4])

# what if we want the first 4 digits of a string
print(credit_number[:4])

# the next set of digits
print(credit_number[5:9])

# the last twelve digits, assumes you need everything up to the end of the string
print(credit_number[5:])

# last character in a string, going backwards
print(credit_number[-1])


# using the step function
# every second character within the string
print(credit_number[::3])