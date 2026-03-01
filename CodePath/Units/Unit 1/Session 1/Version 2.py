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
    # that takes in a float bill 
    # and a string service_quality as parameters.
    # If service_quality is "poor", 
        # the function should return 10% of the bill value.
    # If service_quality is "average", 
        # the function should return 15% of the bill value.
    # If service_quality is "excellent", 
        # the function should return 20% of the bill value.
    # If service_quality is any other value, 
        # the function should return None.
def calculate_tip(bill, service_quality): 
    if service_quality =="poor":
        return bill * 0.1
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.2
    else:
        return None
        # the function should return None.
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
# What did you learn? I do not need to initialize the variables bill and service quality to indicate that they are integers or floats
    # When you do need to initialize is when you create a counter, a running total of some values, a list I am building, a temorary variable, a default value I plan to update etc. 

print("-------------------------------------------------------------------")
# Problem 6: Rock, Paper, Scissors
    # Write a function rock_paper_scissors() 
    # that determines the winner of a game of Rock, Paper, Scissors. 
    # The function accepts two strings as parameters: 
        # player1 and player2. 
    # Each parameter can have a value of "rock", "paper", or "scissors".
    # Print either "Player 1 wins!" or "Player 2 wins!" 
    # according to the following rules:
        # Rock wins against scissors.
        # Scissors wins against paper.
        # Paper wins against rock.
    # If both player1 and player2 have the same value,
        # print "It's a tie!".
def rock_paper_scissors(player1, player2):
    # Check if the inputs are valid (This is optional for this program but it's good practice!)
    if player1 not in ["rock", "paper", "scissors"]:
        return "Invalid input for player1"
    if player2 not in ["rock", "paper", "scissors"]:
        return "Invalid input for player2"
    # If both player1 and player2 have the same value,
    if player1 == player2:
        print("It's a tie!")
        return
    # Rock wins against scissors.
    if player1 == "rock" and player2 == "scissors" :
        print("Player 1 wins!")
        return
    if player2 == "rock" and player1 == "scissors" :
        print("Player 2 wins!")
        return
    # Scissors wins against paper.
    if player1 == "scissors" and player2 == "paper" :
        print("Player 1 wins!")
        return
    if player2 == "scissors" and player1 == "paper" :
        print("Player 2 wins!")
        return
    # Paper wins against rock.
    if player1 == "paper" and player2 == "rock" :
        print("Player 1 wins!")
        return
    if player2 == "paper" and player1 == "rock" :
        print("Player 2 wins!")
        return
    
rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")
print("---------------------------------")

# another even simpler way of doing it!
    # This one takes all the possible scenarios of only one player winning 
    # and then it prints the other player winning 
    # if none of these prove to be the case. 
def rock_paper_scissors(player1, player2):
    if player1 not in ["rock", "paper", "scissors"]:
        return "Invalid input for player1"
    if player2 not in ["rock", "paper", "scissors"]:
        return "Invalid input for player2"

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")

print("-------------------------------------------------------------------")
# Problem 7: Unscramble and Divide

    
    

