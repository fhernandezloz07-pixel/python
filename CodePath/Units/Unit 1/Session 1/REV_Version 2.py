# Problem 1: Hello User!
def greet_user(name):
    print(f"Hello {name}")

student_1 = "Michae# that crl"
greet_user(student_1)
print("__________________________________________________________")


# Problem 2: Calculate Difference
def difference(a, b):
    return a - b 

diff = difference(8, 3)
print(f"diff = {diff}")
print("__________________________________________________________")

# Problem 3: List Concatenation
    # Given an integer list nums of length n
    # create a function concatenate_list()
    # that creates and returns a list ans of length 2n
    # where ans[i] == nums[i] and ans[i + n] == nums[i]
    # for 0 <= i < n
    # specifically, ans is the concatenation of two nums lists

def concatenate_list(nums): # create a function concatenate_list()
    n = len(nums) 
    ans = [0] * (2 * n)
    for i in range(n):
        ans[i] = nums[i]  
        ans[i + n] = nums[i]
    return ans

print(concatenate_list([1,2,3,4]))
print("__________________________________________________________")

# Problem 4: Sleep Assingment
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >=8 and hours <= 10:
        print("You got a good night's rest!")
    elif hours > 10:
        print("You're a sleep prodigy!")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)
print("__________________________________________________________")

# Problem 5: Calculate Tip
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * .1
    elif service_quality == "average":
        return bill * .15
    elif service_quality == "excellent":
        return bill * .20
    else: 
        return None
    
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
print("__________________________________________________________")

# Problem 6: Rock, Paper, Scissors
def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "rock" and player1 == "scissors":
        print("Player 2 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "scissors" and player1 == "paper":
        print("Player 2 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "paper" and player1 == "rock":
        print("Player 2 wins!")
        
rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")
print("__________________________________________________________")

# Problem 7: unscramble and divide
def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        result.append(halved)
    return result

print(halve_lst([2,4,6,8]))
print("__________________________________________________________")

# Problem 8: Above the Threshold
def above_threshold(lst, threshold):
    new_lst = []
    for i in lst:
        if i > threshold:
            new_lst.append(i)
    return new_lst # remembrer this part, it is good practice to ALWAYS have a return astatement!

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)
print("__________________________________________________________")

# Problem 9: Countdown
def countdown(m, n):
    # range(start, stop, step)
    for i in range(m, n - 1, -1): # step is -1 because we are counting down, also use n - 1 for the reason that we are counting down 
        print(i)

countdown(5, 1)


