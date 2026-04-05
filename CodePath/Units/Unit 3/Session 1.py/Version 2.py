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

print("-----------------------------------------------------------")
# Problem 2: Remove Char