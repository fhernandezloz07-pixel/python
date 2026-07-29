# Problem 1: Print list
#            go through the list with a for loop and print each item in the list
#            you dont have to use the print function bc you already used a print in the for loop
def print_list(lst):
    for item in lst:
        print(item)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

print("---------------------------------------------------------------")
# Problem 2: Print Double List Items
def double(lst):
    for num in lst:
        num *= 2
        print(num)

lst = [1, 2, 3]
double(lst)

print("---------------------------------------------------------------")
# problem 3: Return Double List
def doubled(lst):
    list = [] # initialize a new empty list
    for num in lst:
        num *= 2
        list.append(num)
    return list

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

print("---------------------------------------------------------------")
# Problem 4: Flip Signs
def flip_sign(lst):
    list = []
    for num in lst:
        num *= -1
        list.append(num)
    return list

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

print("---------------------------------------------------------------")
# Problem 5: Max Difference
def max_difference(lst):
    # Find Max number
    max_num = lst[0] # lets just say the max number in the list is the first one so we can start the comparison
    for num in lst:
        if num > max_num:
            max_num = num

    # Find min num
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num

    num_diff = max_num - min_num
    return num_diff

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

print("---------------------------------------------------------------")
# Problem 6: Below Threshold
def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

print("---------------------------------------------------------------")
# Problem 7: Evens List
def get_evens(lst):
    evens_lst = []
    for num in lst:
        if num % 2 == 0:
            evens_lst.append(num)
    return evens_lst

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

print("---------------------------------------------------------------")
# Problem 8: Multiples of five
def multiples_of_five():
    for num in range(5, 101, 5): # you have to use a for loop bc it will literally print out "range(---)"
        print(num)

multiples_of_five()

print("---------------------------------------------------------------")
# Problem 9: Divisors
def find_divisors(n):
    div_lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            div_lst.append(i)
    return div_lst

lst = find_divisors(6)
print(lst)

print("---------------------------------------------------------------")
# Problem 10: FizzBuzz
def fizzbuzz(n):
    for num in range(1, n + 1): # we are inclusive
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz(13)

print("---------------------------------------------------------------")
# Problem 11: Print the Index
def print_indices(lst):
    for num in range(len(lst)): # inclusive
        print(num)

lst = [5,1,3,8,2]
print_indices(lst)

print("---------------------------------------------------------------")
# Problem 12: Linear Search
def linear_search(lst, target):
    for i in range(len(lst)): # range(len(lst)) is for returning the index!!
        if lst[i] == target: # lst[i] represents the number in the given index
            return i
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)

