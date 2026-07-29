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
    for num in lst: 
        if num - 1 

