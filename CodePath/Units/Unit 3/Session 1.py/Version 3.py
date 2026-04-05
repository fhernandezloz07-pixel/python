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
# What did you lea