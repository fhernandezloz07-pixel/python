# Problem 1: Choose Your Pokemon
    # For the following code call the function so that it prints
    # out the following to console:
def choose_pokemon(my_pokemon):
	for pokemon in my_pokemon:
		print(f"{pokemon} I choose you!")
		
my_pokemon = ["Pikachu", "Charizard", "Eevee"]
choose_pokemon(my_pokemon)

print("-------------------------------------------------------")
# problem 2: Rotate Left
    # Write a function rotate_left() that takes in 
    # a string s and an integer n and an integer n as parameters. 
	# The function reyurns a new string with the first n characters
	# moved to the end of the string where 1 <= n <= len(str)
'''
U:
    given a string s and an integer n as the stop position 
	where we will move the first letters of the string
P:
- Brainstorming: 
    Use stringindexing 

define a function with the appropiate parameters
for element in range(len(n)) # element is the index of the string
if element == n: 
    new_s = s[element + 1:] + s[:element]
return new_s
'''
# I: 
def rotate_left(s, n):
	for i in range(len(s)):
		if i == n:
			new_s = s[i:] + s[:i]
	return new_s

s = "rotation"
print(rotate_left(s, 2))
# What did you learn? String interpolation with indexing

print("-------------------------------------------------------")
# Problem 3: First Duplicate
    # Write a function first_repeated_char() that takes in a string s as a parameter and 
	# returns the index of the first repeated character in the string. 
	# Uppercases and lowercase letters are considered different characters,
	# and the function returns None if there are no repeated characters. 
'''
U:
Based on a string s return the index of the first repeated character in the string 
Return none if there are no repeated characters
P:
- brainstorm: 
    We will need a lot of loops here and I could possibly use a list but 
    with a list do you want to save the character of the index itself!?!

	define a function with the appropiate parameters 
	initialize a repetitions dictionary
	for character in s: 
	if s not in dictionary:
	add it and initialize to 1
	else: 
	add 1 
	
	for the first key in the dictionary: (I think here you have to use )
	
'''
# Example of ennumerates
s = "cat"
for thing in enumerate(s):
	print(thing)
print("----------------------------")

# Another example of enumerate
letters = ['a', 'b', 'c']
for letter in letters:
	print(letter)
'''
output: 
a
b
c
'''
	# But what if you also want the position of the index
for i, letter in enumerate(letters, start = 1):
	print(i, letter)
'''
output: notice we start the indexing at 1
1 a
2 b
3 c
'''
for i, letters in enumerate(letters):
	print(i, letter)
'''
output: notice we start with normal 
'''


print("----------------------------")
def first_repeated_char(s):
	seen = {}
	
	# we usually do for char in s, 
	# this time we want the character and its index!
	for i, char in enumerate(s):  
		
		if char in seen:
			return i
		else:
			seen[char] = i

s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))
		