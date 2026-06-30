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
print("__________________________________________________________")

# Problem 10: Calculate Power
def power(base, exponent):
    accumulator = 1 # start the accumulator at 1 because we are essentially multiplying
    for i in range(exponent):
        accumulator *= base 
    return accumulator

pow1 = power(2,5)
print(pow1)
pow2 = power(3,3)
print(pow2)
print("__________________________________________________________")

# Problem 11: Length of list 
def list_length(lst):
    accumulator = 0
    for i in lst:
        accumulator += 1
    return accumulator

lst = [2, 4, 6, 8, 10]
length = list_length(lst)
print(length)
print("__________________________________________________________")

# Problem 12: Calculate Factorial
def factorial(n):
    accumulator = 1 # initialize to 1 because we are multiplying 
    for i in range(n, 1, -1): # we are counting down!
        accumulator *= i
    return accumulator

print(factorial(3))
print("__________________________________________________________")

# Problem 13: Calculate the squares
def squares(nums):
    new_lst = [] # initialize a new empty list
    for i in nums:
        new_lst.append(i * i)
    return new_lst # new list containing the swuare of each number in the og list

lst = [1,2,3,4]
print(squares(lst))
print("__________________________________________________________")

# Problem 14: Multiply List
def multiply_list(lst, multiplier):
    lst2 = []
    for i in lst:
        lst2.append(i * multiplier)
    return lst2

lst = [1,2,3]
new_lst = multiply_list(lst, 3) 
print(new_lst)
print("__________________________________________________________")

# Problem 15: Count Evens
def count_evens(lst):
    even_counter = 0
    for i in lst:
        if i % 2 == 0: # check if i is even
            even_counter += 1
    return even_counter # The number of even numbers in the list

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)
