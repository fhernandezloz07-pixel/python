# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 20 # in Celsius
is_raining = True # boolean

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")
