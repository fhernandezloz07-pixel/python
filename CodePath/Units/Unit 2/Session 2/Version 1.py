# Unit 2: Session 2: Version 1 problem sets
# Problem 1: Cast Vote
    # Write a function cast_vote() 
    # that records a vote for a candidate in an election. 
    # The function accepts a dictionary votes that maps candidates
    # to their current number of votes and a string candidate 
    # that represents the candidate the user would like to vote for. 
    # If the candidate doesn't exist, 
        # add them to the dictionary. 
    # The function should return the updated dictionary.

# understand: 
# 1. check if the candidate exists 
# 2. if they exist increase their vote by one
# 3. If they dont exist increase them  by one


def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

# example output: 
    # {'Alice': 6, 'Bob': 3}
    # {'Alice': 6, 'Bob': 3, 'Gina': 1}

print("--------------------------------------------------------------------")
# problem 2: Keys in common
    # Write a function that takes in two dictionaries,
    # dict1 and dict2 and finds all keys common to both dictionaries.
    # The function returns a list of common keys.

# U: find keys common to both dict 1 and dict 2 and return them

# P: Create an emty list to store keys in common, 
# loop through dict 1
# check if key matches dict 2
# add the matches to the common list

# I:
def common_keys(dict1, dict2):
    common_keys = [] # initialize to emtpy
    for key in dict1:
        if key in dict2:
            common_keys.append(key) # this append feature is used because we are using a list and not a dictionary
    return common_keys
    
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

print("----------------------------------")

# Problem 3: Frequency Count
    # Write a function that takes in a list of integers nums 
    # and counts the number of occurrences of each integer. 
    # The function returns the result as a dictionary
    # with integers as keys and their counts as values.
# Example code: 
def build_frequency_map(lst):
    freq = {} # initialize a dictionary that wil store
    # as key a number, and as value the number of times that number appears 
    # in a given list 
    for item in lst: # for an element or number in a given list
        if item not in freq: # if the element or number is not in the dictionary frequency 
            freq[item] = 0 # call the dictionary and append the key =that we found and set it to 0
        freq[item] += 1 # if the item is in the list tho =, simply add 1
    return freq # we know this 
nums = [1,2,2,3,3,4,4,6,6,6,6]
print(build_frequency_map(nums))

print("----------------------------------")
'''
Not: 
A frequency map is a dicionary that counts 
how many times each element appears in a collection 
(usually a list or string)

U:
Create a list of the number of occurences of a given number in a list

P:
define a fucntion and its appropiate list parameter
initialize a dictionary, that is where we will store all of our keys and values
run a loop:
for element in list 
    if the element is not in the dictionary 
        call the dictionary with the key you want which is the element and make it equal to 0 because we barely found it 
the element is found in the list so simply add 1 
return the dictionary
'''
# I: 
def count_occurences(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0 # call the empty dictionary and the element of the list and make it 0 because it's the first time we see it. 
        freq[num] += 1 # if this is not the first time we see it, do the same, call but add 1 each time we see it. 
    return freq # return the dictionary freq with each element in the list as a key and the value as the amount of times it has popped up!
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurences(nums))


print("--------------------------------------------------------------------")
# Problem 4: highest Priority Task
    # Given a dictionary tasks where keys are task names 
    # and values are priorities (1-10, where 10 is the highest priority),
    # write a function get_highest_priority_task() that 
    # removes the task with the highest priority from the dictionary and returns its name.
        # If two tasks have the same priority, return the task that comes first in the alphabet.
'''
U:
Given a dictionary with a task and its priority 
return the task name with the highest priority 
while also remiving it from the list

P:
define a function with the appropiate dictionary parameter as tasks 
write a for loop:
for i in tasks (for every key in the dictionary):
initialize a variable highest priority task and set it equal to to i
if the value of the current key i is greater than the value of the highest priority task value 
highest priority variable  = value of the current key i
return hgihest priority variable
'''
# I:
def get_highest_priority_task(tasks):
    highest_task = None # initialize highest priority task to none for now (key)
    highest_priority = 0 # initialize highest priority representing the value of the highest priority key task to 0

    for task in tasks: # for a key in the dictionary tasks
        if tasks[task] > highest_priority: # if the value of that key is greater than the highest_priority task we just initialized ... 
            highest_priority = tasks[task] # set the hgihest priority number is set to the value of the task we are checking 
            highest_task = task # and we also se the highest priority task equal to the one we are checking that passes the conditions 
        
        elif tasks[task] == highest_priority and task < highest_task: # python conpares strings alpahbetically
            # if the value of the key we are ckecking is not greater than the vaue of the current highest priority value
            # and instead the value is equal to it and the key is also less than the current highest task key
            highest_task = task # we set the highest task equal to the current task
    
    tasks.pop(highest_task) # the pop removes it from the dictionary as we are told to do, it will now not show up if we print the dictionary
    return highest_task

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)
print(tasks)
# What did you learn? 
# The pop feature allows for us to remove a key and its value from a dictionary entirely!

print("--------------------------------------------------------------------")
# Problem 5: Find Majority Element 
    # Write a function find_majority_element() that 
    # takes in a list of integers elements 
    # and finds the majority element in the list. 
    # A majority element is an element that appears 
    # more than n/2 times where n is the size of the list. 
    # If there is no majority element, return None.
'''
U:
Given a list, return the majority number element in the list. 
A majority number element in the list is one that satisfies the property;
    the element appears more than n/2 times where n is the size of the list
this basically means that the number element makes up more than half of the list
P:
define a function with the appropiate parameter as the list of integers; elements
initialize an empty dictionary where I will store the keys as a number in the list and the value as the amount of times the muber appeared in the list
initialize a counter_n and set it equal to 0 i inside the for loop, each time the for loop runs this will add 1, by the end we should know the amoun of numbers there were in the list! (we can use this to divide later so we can actually set it to n)
for element in elements 
set the counter_n to += 1
if element not in dictionary
call the dictionary and the key as the element and make it equal to 1 
if element in dictionary 
call the dictionary and the key as the element and make it += 1 (adding one each time!)
In the end we ideally already have our full dictionary with the appropiate keys and values so ...
for every key in dictionary
if the value of the key is greater than the length of the list elements all over 2 
make variable majority_element equal to that key (do I have to initialize majority_element = None?)
return majority_element
'''
# I: 
def find_majority_element(elements):
    dictionary = {}
    counter_n = 0

    for element in elements:
        counter_n += 1

        if element not in dictionary:
            dictionary[element] = 1

        else: # none of that fancy stuff needed just an else and your code!
            dictionary[element] += 1
    
    majority_element = None # I was supposed to initialize this outside the for loop i am using it in

    for i in dictionary: 
        if dictionary[i] > counter_n / 2: # length of the list elements all over 2 
            majority_element = i

    return majority_element # you technically dont even need this variable you can simply return i but ok ... 
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
# Test run 1: I anticipate some errors with the returns and the way I used my counter but lets see... 
    # Output: {2: 2}, Expected output: 2
    # fixes made it work, you were right I returned too early and i only needed an else statement to make it true
    # also remember to initialize a valriable before you use it if its inse a loop if statement

print("--------------------------------------------------------------------")
# Problem 6: Has duplicates 
    # Write a function has_duplicates() that 
    # takes in a list of integers nums and a positive number k as parameters. 
    # The function returns True if the list contains any duplicate elements within k 
    # (inclusive) indices of each other. 
    # In other words, return True if nums[i] 
    # has the same value as any of the k neighboring elements to its left or right. 
    # If k is greater than the list's length, 
        # the solution should check for duplicates in the complete list. 
    # The function should return False otherwise.
'''
U:
Given a list of numbers nums and a given number k
check; do any two equal numbers appear within k positions of eachother in the list?
if yes -> return True
if no -> return False
Note: 
This means that the distance between their positions in the list is k or less 
 nums = [5,take the following list as an example: nums = [5, 6, 8, 2, 6, 4, 9]
 notice that the number 6 is repeating in the list, first at index 0 and then at index 4
 4 - 1 = 3, therefore the distance = 3
Case 1: k = 2
    3 > 2 so print false
Case 2: k = 5
    3 <= 5 so print true
Case 3: k = 3
    3 = 3 so print true

P:
define a function with appropiate parameters as the list nums
Check if there are any repeating numbers in the list:
for num in nums (for a number element in the list of number ...)

'''