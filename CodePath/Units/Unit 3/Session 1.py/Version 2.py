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
us string slicing to output all except for n which is the index of the character we want to remove
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
    for char in range(len(s)): # n is the index of the character in the string
        if char == n: # if the index of thecharacter we are testing is the same as n we want to remove it!
            fixed_s = s[:n] + s[n + 1:len(s)] # this if the full thingie

    return fixed_s

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
# Run 1: Something wrong with range(len(n)) -> changing it to range(len(s))
# Run 2: something wrong with s.remove(n) -> changing to for n in range(len(s)), wait I cant use remove I have to use slicing!
# Run 3: Fixed all of it using slicing yay!
# What did you leanr? about slicing and that start is included but stop is not so I have to accomodate for that

print("-----------------------------------------------------------")
# Problem 3: Count Vowels
    # Write a function vowel_count() that takes in a string s
    # as a parameter and returns the number of vowels in the given string
'''
U:
Cound the number of vowels in a string
P:
- Note: We do Not care about capitalization so accomodate for that
define a function with parameter as the string
initialize a counter variable that counts the amount of vowels in a string
initialize a vowel variable and set it equal to aeiouAEIOU, to account for under and lowercase
for a character in a string 
if the character is in vowel variable 
counter += 1
return counter

'''
# I: 
def vowel_count(s):
    counter = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            counter += 1
    return counter

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# Problem 4: Reverse Sentence: 
    # Write a function reverse_sentence() that takes in a string sentence as a parameter
    # and returns the string with the sentence but with the order of the words reversed 
    # The sentence will only contain alphabetic characters and spaces to separate the words
    # if there is only one word in the sentence, the function returns the original string. (duh)
'''
U:
Based on a string sentence, reverse not the characters in the string but the words themselves
P:
- Brainstorm: 
    there is a built in I can use to split words based on the spaces they have!
    then I can have a list of all the individual words
    and then I can recerse those words
    I can also use the .join thingie
define a function with the appropiate parameter as the string 
define a list and make it equal to the action of splitting the sentence
print list reversed with the :-1 feature see if it works...
'''
print("-----------------------------")

# Example problem:

splitting = "I love magic".split()
print(splitting) # splitting a sentence by its spaces, python automatically puts it in a list!

print(" ".join(["hello", "world"])) # Taking words and joining them with a space 

print("-----------------------------")
# I:
def reverse_sentence(sentence):
    list = sentence.split() # a list containing each word as an element
    reversed_list = list[::-1] # reverses each element in the list which is the words
    print(" ".join(reversed_list))
   
sentence = "I solemnly swear I am up to no good"
reverse_sentence(sentence)
# What did you learn? 
# The join built in lets you join the elmements of a list with a space!
# reversing is ::-1
# the split() built-in not only splits a string but each split is made by a space ad turns into elements of a list
print("----------------------------------------------------------")


