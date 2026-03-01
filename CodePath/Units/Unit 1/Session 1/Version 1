# Problem Set version 1
# Problem 1: hello World!
def hello_world(): 
    print("Hello world!")

hello_world() # Prints 'Hello world!'

print("-------------------------------------------------------------------")
# Problem 2: Today's Mood
def todays_mood():
    mood = "😎"
    print("Today's mood: " +  mood)

todays_mood()

print("-------------------------------------------------------------------")
# Problem 3: Lunch Menus
def print_menu(menu):
    print("Lunch menu to day is: " + menu)

menu = "🍕"
print_menu(menu) # Prints the menu item to console
# The variable listed between the () of a function definition is known as a parameter. 

print("-------------------------------------------------------------------")
# Problem 4: Sum of Two Integers
def sum(a, b): # here we are sort of declaring sum() to know what it will do for all cases
    return a + b
num_sum = sum(13, 27) # use sum() to calculate the sum of 13 and 27
result_sum = sum(num_sum, num_sum) # use sum() to double the calculated sum

print(result_sum)# Print the result to the console

print("-------------------------------------------------------------------")
# Problem 5: Product of two integers
def product(a, b): # Writing the function Product() that returns the product of two integers a and b
    return a * b
result_product = product(22, 7) # Example product of 22 times 7
print(result_product) # Printing the product of two numbers a and b to console

print("-------------------------------------------------------------------")
# Problem 6: Classify Age
def classify_age(age): 
    if age < 18:
       return "child"
    elif age >= 18:
        return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
print("-----------------")
    # Another way to do this with print statements inside the if elif statement: 
def classify_age(age): 
    if age < 18:
       print("child")
    elif age >= 18:
        print("adult")

classify_age(18)
classify_age(7)
classify_age(50)

print("-------------------------------------------------------------------")
# Problem 7: What time is it? 
def what_time_is_it(hour): # hour is the parameter of the function what_time_is_it
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

print("-------------------------------------------------------------------")
# Problem 8: Blackjack
def blackjack(score): 
    if score == 21:
        print("Blackjack!")
    elif score > 21: 
        print("Bust!")
    elif score >= 17 and score <= 21: # in python use the built-in and for connecting inside the if statement!
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")

blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)

print("-------------------------------------------------------------------")
# Problem 9: First Item
def get_first(lst): 
    if lst == []:  # add the empty condition first before you check for the first item in the list 
        return None
    return lst[0]

print(get_first([3,1,6,7,5]))

# Problem 10: Last Item 
def get_last(lst): 
    if lst == []:
        return None
    return lst[-1]

print(get_last([3,1,6,7,5])) # printing the fuction properties we just coded for the specified list!

print("-------------------------------------------------------------------")
# Problem 11: Counter
    # write a function counter() that uses the built-in range function to: 
def counter(stop):
    # print numbers between 1 and a given stop value (inclusive)
    for i in range(1, stop + 1): # The plus includes the last indez instead of excluding it!
        print(i) #???
counter(7) # Example code 

print("-------------------------------------------------------------------")
# Problem 12: Sum of 1 to 10
    # Accumulator variable is a variable that keeps running total while you program loops, so it grows step-by-step
def sum_ten():
    accumulator_sum = 0 # start the accumulator at 0
    for i in range(1, 11): # sum from 1 to 11
        accumulator_sum += i # add the current number to the accumulator
    return accumulator_sum 
print(sum_ten()) # Print your code!

print("-------------------------------------------------------------------")
# Problem 13: Total sum 
def sum_positive_range(stop):
    accumulator_sum = 0 # start total at 0
    for i in range(1, stop + 1): 
        accumulator_sum += i
    return accumulator_sum

print(sum_positive_range(6)) # 1 + 2 + 3 + 4 + 5 + 6 = 21
# what did you learn? when you put 6 in the pring its basically telling the code that the stop parameter that is built in should stop at 6

print("-------------------------------------------------------------------")
# Problem 14: Total sum in range
    # Write a function sum_range()
    # returns the sum of numbres from a given start value
    # to a given stop value, inclusive
def sum_range(start, stop):
    accumulator_sum = 0 # think of this as an empty bucket that is filled with each number from start to stop. So istead of assigning it to start simply assign to 0. ALWAYS!
    for i in range(start, stop + 1):
        accumulator_sum += i
    return accumulator_sum

print(sum_range(3, 9))
# What did you learn? Always start the accumulator at 0 for good pracice. Return the accumulator sum for for that you first need to create it!

print("-------------------------------------------------------------------")
# Problem 15: Negative numbers 
    # Write a function print_negatives() that takes a list of integers lst 
    # and prints all negative numbers in the list.
def print_negatives(lst):
    found_negative = False # checks if there are even any negatives in a given list
    if lst == []: # accounting for the fact that a list might be empty
        return None
    for num in lst: # num or i as we use it in the for loops is just a variable name I choose. They are placeholders that represent "each element of the list as we loop..." 
        if num < 0: # check if there is a negative number
            print(num) # print that number then!
            found_negative = True # Because finding negative numbers makes found_negative true, the opposite would be that if we didn't find negative numbers found_negative would be false 
    if not found_negative: # if this were to be inside the nested if statement, it would print out EACH time there was a positive number found in any list. 
        print("None")
        
print_negatives([1,2,3,4,5]) # sample list without negative numbers
print_negatives([3,-2,2,1,-5]) # sample list with negative numbers 
# What did you learn? i and num are placeholder variables to help me in my code, they don't need to be initialzed
# A for loop and an if loop never require a return.
    # A for loop is a way to repeat actions
    # An if loop is a way to make desicions
    # it matters where we put the loops, whether inside or outside.
        # if inside, the code runs once PER element, so it prints out something on one number, then it goes back to the beginning and cheks the same condition for the next number.
        # if ourside the loop, the program has already examined every element. Only then can it correctly decide whether a negative number was ever found, thus if none were found then the conclusion may be one thing!!
            # think of it as python covering the list and only incovering one number at a time for a given condition you set. It chcks each one! Then it repeats the same steps for another calling and so on. 

print("-------------------------------------------------------------------")
# Problem Set version 2
# Problem 1: Hello user!
    # Write a function greet_user() 
    # that takes in a string name as a parameter 
    # and prints "Hello <name>".
def greet_user(name):
    print("Hello " + name)

student_1 = "Michael"
greet_user(student_1)

print("-------------------------------------------------------------------")
# Problem 2: Calculate Difference!
    # Write a function difference() 
    # that returns the difference between two integers a and b 
    # (b should be subtracted from a).
def difference(a, b):
    return a - b

diff = difference(8, 3)
print("diff =", diff) # istead of simply printing out 5, it prints out diff = 5.
# What did you learn? if we want to return a string as well as a number, the number should be imputted into a variable, and then that variable into the print statement with the + value. 

print("-------------------------------------------------------------------")
# Problem 3: List Concatenation
    # Given an integer list nums of length n, 
    # create a function concatenate_list() 
    # that creates and returns a list ans of length 2n 
    # where ans[i] == nums[i] and ans[i + n] == nums[i] 
    # for 0 <= i < n (0-indexed).
    # Specifically, ans is the concatenation of two nums lists.

def concatenate_list(nums): # Create a fucntion concatenate_list() 
    n = len(nums) # given an integer list nums of length n 
    ans = [0] * (2 * n) # that creates a list ans of length 2n
    for i in range(n): # for 0 <= i < n (0-indexed).
        ans[i] = nums[i] # where ans[i] == nums[i] 
        ans[i + n] = nums[i] # and ans[i + n] == nums[i] 
        return ans # also returns a list ans 
    
# What did you learn? 
# Concatenation is joining two pieces of data end-to-end, like sticking them together to form one longer sentence. 
    # in lists it can be [1, 2] + [3, 4] = [1, 2, 3, 4]
    # in strings it can be "hello" + "world" = "helloworld"