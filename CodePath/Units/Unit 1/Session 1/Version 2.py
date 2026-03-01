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

print("-------------------------------------------------------------------")
# Problem 4: Sleep Assesment
    # Write a function sleep_assessment() 
    # that takes in an integer parameter hours 
    # indicating the number of hours the user slept.
    # If hours is less than 8, 
        # print "Oof, go back to bed!".
    # If hours is greater than or equal to 8 and less than or equal to 10, 
        # print "You got a good night's rest!".
    # If hours is greater than 10, 
        # print "You're a sleep prodigy!".
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    if hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    if hours > 10:
        print("You're a sleep prodigy!")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)
# What did you learn? Usually the way something is written in plain english is the way to write it in code.

print("-------------------------------------------------------------------")
# Problem 5: Calculate tip
    # Write a function calculate_tip() 
    # that takes in a float bill a
    # nd a string service_quality as parameters.
    # If service_quality is "poor", 
        # the function should return 10% of the bill value.
    # If service_quality is "average", 
        # the function should return 15% of the bill value.
    # If service_quality is "excellent", 
        # the function should return 20% of the bill value.
    # If service_quality is any other value, 
        # the function should return None.



