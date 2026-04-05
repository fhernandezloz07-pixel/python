# Problem 1: Perfect match
    # def match_made(dictionary):
    #     for key, value in dictionary.items():
    #         print( f"{key} and {value} are a perfect match.")
'''
U: add code to the following given code so that 
the program prints out the following to console:
    Peanut butter and Jelly are a perfect match.
    Spongebob and Patrick are a perfect match.
    Ash and Pikachu are a perfect match.
P:
- Brainstorm:
    there is a dictionary and our function name is match_made
    for each key in the dictionary 
    I am thinking of creating a dictionary 
        1. Peanut Butter , Jelly
        2. Spongebob , Patrick
        3. Ash , Pikachu

- Use string interpolation: the process of inserting values 
(like variables or expressions) directrly INTO a string
its called interpolation because it means filling in values between known points
In programming we are fillong in placeholders inside a stringwith actual values!

'''
# Example of string interpolation with f-string
name = "Fatima"
age = 19

print(f"My name is {name} and I am {age} years old.") 
# this is better than using + and converting age into str(age) inside the sentence.

print("-----------------------------")
# I:
def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")
    
dictionary = {"Peanut Butter":"Jelly", "Spongebob": "Patric", "Ash": "Pikachu"}
match_made(dictionary)
# What did you learn: 
# String interpolation and don't print again if we already have a print in the loop, then it will unnecesarily return None.

print("------------------------------")
# Problem 2: Remove Char
    # Write a function remove_char() that takes in a string s and an integer n as parameters, 
    # The function returns a new string with the n'th character removed where 0 < n < len(s).
'''
U: 
based on a string, our function is supposed to remove a character from that string 
by calling the string and then the index the character we want to extract is found in
P:
- brainstorming: 
    Use string indexing: A string is a sequence of characters, and each character has a position, called the index
    You acess a character by print(text[0]), here text would be the variable containing the stirng, the first character in the string is called!
        
define a function with the appropiate string and integer parameters

'''
# Example of SLICING!(grabbing parts of a string)
text = "hello"

print(text[1:4]) #ell
print(text[:3]) # hel
print(text[2:]) # llo
print(text[-3:]) # llo

# Example of LIST INDEXING
nums = [10, 20, 30, 40, 50]
print(nums[0]) # 10
print(nums[2]) # 30
print(nums[-1]) # 50
    # another example of slicing to extract numbers
print(nums[1:4]) # [20, 30, 40]
'''
The key difference of strings and lists are mutability
strings are immutable, you cannot change individual characters
lists are mutable, you can change individual elements

'''
# I:
def remove_char(s, n):
    fixed_s = "" # Creating an empty string that will be the fixed one
    for char in range(len(n)): # char is the index of the char
        .remove

        

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

print("-----------------------------------------------------------")