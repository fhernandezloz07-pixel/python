# function = a block of organized, reusable code that is used to perform
#            a single, related action. 
# Problem 1: Hello World!
def hello_world():
    print("Hello world!")

hello_world()
print("__________________________________________________________")
# Problem 2: Today's Mood
def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)


todays_mood()
print("__________________________________________________________")
# Problem 3: Lunch menu
def print_menu(menu):
    print("Lunch today is: " + menu)

menu = '🍕'
print_menu(menu)
print("__________________________________________________________")
# Problem 4: Sum of Two integers
def sum(a, b):
    return a + b

num_sum = sum(13, 27)
double_sum = sum(num_sum, num_sum)

print(double_sum)
print("__________________________________________________________")
# Problem 5: Product of Two Integers
def product(a, b):
    return a * b

print(product(22, 7))
print("__________________________________________________________")

# Problem 6: Classify Age
def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
    
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
print("__________________________________________________________")

# Problem 7: What time is it? 
def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else: 
        return "nap time 😴"
    
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
print("__________________________________________________________")

# Porblem 8: Black jack
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score <= 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")
    
blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)
print("__________________________________________________________")

# Problem 9: First Item
def get_first(lst):
    if lst == []:
        return None
    else:
        return lst[0]
    
print(get_first([3,1,6,7,5]))
print("__________________________________________________________")

# Problem 10: Last item
def get_last(lst):
    if lst == []:
        return None
    else:
        return lst[-1]
    
print(get_last([3,1,6,7,5]))
print("__________________________________________________________")

# Problem 11: Counter
def counter(stop):
    for num in range(1, stop + 1):
        print(num)

counter(7) # this is actually the index per se
print("__________________________________________________________")

# Problem 12: Sum of 1 ot 10
def sum_ten():
    accumulator_sum = 0 # initialize the accumulator sum to 0
    for i in range(1, 11): # the 11 is excluded
        accumulator_sum += i
    return accumulator_sum

output = sum_ten()
print(output)
print("__________________________________________________________")

# Problem 13: Total Sum
def sum_positive_range(stop):
    accumulator_sum = 0
    for i in range(1, stop + 1):
        accumulator_sum += i
    return accumulator_sum

sum = sum_positive_range(6)
print(sum)
print("__________________________________________________________")

# Problem 14: Total Sum in Range
def sum_range(start, stop):
    accumulator_sum = 0
    for i in range(start, stop + 1):
        accumulator_sum += i
    return accumulator_sum

sum = sum_range(3, 9)
print(sum)
print("__________________________________________________________")

# Problem 15: negative Numbers
def print_negatives(lst):
    found_negative = False
    if lst == []:
        return None
    for i in lst:
        if i < 0:
            print(i)
            found_negative = True
    if not found_negative:
        print("None")

print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])






