# Problem 1: Calling Mississippi
    # based on the following code, call the function so that
    # it prints out the following to the console (without calling the function more than once)

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi") 

count_mississippi(6) # calling and assigning value
# What did you learn? 
# I don't always need to print at the end, especially if there is already a print in 
# the loops! I can simply call.

print("------------------------------------------------------------------------")
# Problem 2: Swap ends
    # Write a function swap_ends() that 
    # accepts a string my_str as a parameter 
    # and returns a new string where the first 
    # and last characters from my_str are swapped.
'''
U:
Write code that swaps the first and the last letters in a string without chanigng the rest
P:
define a function with appropiate parameter string
create a variable swapped that is initialized to an empty string
for element in range(len(lst)):
    call the variable and .join(last index[-1], and the middle ones, then the first one[0])
return the created variable 
Note: I need to know about string indexing and the .join feature
'''
def swap_ends(my_str):
    swapped = my_str[-1] + my_str[1:-1] + my_str[0] # the last, the middle not including the last, and the first
    # swapped = "".join(swapped(my_str)) # if we use a .join, it only takes in ONE iterable, like alist or stirng, not multiple arguments
    # return swapped # do I need a return statement if there is no loop?
    return swapped
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
# What did you learn? 
# You don't always need to use the .join feature, you can concatenate strings like normal +
# think about the indexing and what -1 means

print("------------------------------------------------------------------------")
# Problem 3: Is Pangram
    # Write a function is_pangram() that 
    # takes in a string my_str as a parameter 
    # and returns True if the string is a pangram and False if not. 
    # A pangram is a sentence containing every letter in the English alphabet.
'''
U:
we need to write a fucntion that returns true if in a string we 
find every single letter of the english alpabet, false if it doesn't
P:
define a function with the appropiate parameter string
initialize a variabe alphabet with each letter in the alphabet
if my_str not in alphabet:
    return False
else: 
    return True

Note: Think about capitalization! Do we use a .toLower or something or ignorecase like in java

Note: .isalpha() is a string method in python that checks whether all 
characters in a string are letters only (no numbers, no spaces, no symbols.)
'''
def is_pangram(my_str):
    lowercase_sentence = my_str.lower() # this allows for the string sentence to be turned into a lowercase
    letter_appearances = {} # Why do we need to create a dictionary?

    for char in lowercase_sentence: # for a given character in the modified string 
        if char.isalpha() == False: # if the character is not a letter
            continue # sort of igrore it and move on to the next char
        if char not in letter_appearances: # if the character is not in our dictionary
            letter_appearances[char] = True # call the dictionary and make the alphabet character a key with value true because its there
    
        # Now we have to ckeck that there are exactly 26 keys in the 
        # dictionary because only then will we know we found all the letters. 

    if len(letter_appearances) == 26:
        return True
    else: 
        return False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

print("------------------------------------------------------------------------")
# Problem 4: Reverse String
    # Write a function reverse_string() that takes a string my_str 
    # as a parameter and returns the stirng reversed.
'''
U:
reverse all the letters in a string
P:
define a function with appropiate parameter string
create an empty string variable reversed_string 
for every element in the range(len(my_str)):
    call reversed_string and print the original with [::-1]
return the string you created 

return 
Note: maybe use slicing, as long as you dont use the reverse feature
'''
def reverse_string(my_str):
    reversed_string = ""
    for letter in range(len(my_str)):
        reversed_string = my_str[::-1]
    return reversed_string

my_str = "live"
print(reverse_string(my_str))
# What did you learn? 
# how to reverse all the letters by using the -1

print("------------------------------------------------------------------------")
# Problem 5: First Unique
    # Write a function first_unique_char() that 
    # given a string my_str as a parameter,
    # if finds the first non-repeating character in it and returns its index.
    # If it does not exist, then return -1
'''
U:
given a string, we have to find the characters that are not 
repeating and maybe store them in a dictionary
the first one that is not repeating shoul dbe printed out. 
if there isn't a character that doesn't repeat print out -1

P:
define a function with the appropiate parameter string
for char in my_str:
create an empty dictionary
    if char not in empty dicitonary:
        empty dictionasry[char] = 1 <- Does not repeat
    else: 
        empty dictionary[char] += 1 <- adding one each time of appearance

for key in our dictionary:
    if dictionary[key] == 1:
        return key
    else:
        return -1
'''
def first_unique_char(my_str):
    repeating_dictionary = {}


    for i in my_str:
        if i not in repeating_dictionary:
            repeating_dictionary[i] = 1
        else:
            repeating_dictionary[i] += 1

    for i in range(len(my_str)):
        index_location = my_str[i] # character!!! i is the index and my_str[i] is the character at that indez
        if repeating_dictionary[index_location] == 1:
            return i
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

print("--------------------------------------------------")
# Problem 6: Minimum Distance
'''
U:
return min distance between word 1 and word 2 based on a list of string words
we have to subtract the indexes of word1 and word2
P:
define a function with appropiate parameters
for i in list:

'''

def min_distance(words, word1, word2):
    for word1 in range(len(words)):
        for word2 in range(len(words)):
                sub_indexes = word2 - word1
    
    return sub_indexes 

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
            

