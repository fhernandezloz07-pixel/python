# Example problem 3:
# String Concatenation:
    # using the addition modifier to combine two or more strings together
# Useful methods:
# .lower() -> Changes all of the letters to a lowercase verion of themselves. Good for "generalizing" varying input to some degree.
sample1 = "This is our first samle string for the day."
print(sample1.lower())


print("----------")
# .upper() -> This converts all letters in a string to their uppercase version. 
sample2 = "This is our second samle string for the day."
print(sample2.upper())

print("----------")
# .split() -> this is frequently used when parsing lage input texts, or in natural language processing related forms of AI. This
# allows users to converst a string into a list of the individual words, since it splits by space by default.
# you may provide specific characters or strings to "split" around (suck as punctuation or other parkers)
sample3 = "This is our third sample string fro the day. This is an additional sentence now."
print(sample3.split("."))

print("----------")
# .replace() ->
sample4 = "This is our sample forth sample string sample for the day"
print(sample4.replace("sample", "REPLACED"))

print("----------")
# string slicing -> Returns a snippet or portion of a string, based on the provided indices. Can provide either the beginning, the start, or the ending index
sample5 = "This is our fifth sample string for the day."
print(sample5[0:5]) # this tells me that the slice begins on index 0 and ends at index 5.
print(sample5[:5])
print(sample5[0:])
print(sample5[0:10:2]) # step size, every other character is take out
print(sample5[0:10:-1]) # return the first 10 letters but reversed, the second index is not inclusive
print(sample5[10::-1]) # How is this different, something is included

# pangram -> a sentence that cntains every letter of the english alphabet at least once, regardless of case. 

'''
U:
Write a function to determin if the following is a pangram, could be any casing, needs to return a boolean value of true or false

P:
1. We are going to be working with an unknown size string string
    we will clean up the string to know our expected format
2. want to check for all 26 letter using a dictionary
2.5 We need to use a for loop to iterate through each char
     -> key: letter, value: true or false
3. count number of keys or items in our dictionary, if == 26 (return value)
'''
# I:
def is_pangram(sentence): 
    lowercase_sentence = sentence.lower()
    letter_appearances = {}

    for char in lowercase_sentence:
        if char.isalpha() == False: # This will allow us
            continue
        if char not in letter_appearances:
            letter_appearances[char] = True

    if (len(letter_appearances)) == 26:
        return True
    else:
        return False
# lets test our function

# String Formatting allows you to create a tring "template" that dynamically fill in placeholders in the string.
# Lets compare string concatenation vs. two approaches of string formatting
userName = "Cory2026"
currentTime = "March 12th, 8:10pm"
# Old way, string concatenation (using + )
# print(userName + "has signed in at " + currentTime)

# f"" optioon 1
print(f"{userName} {currentTime}")




# Instructor Demo
# 1. Understand
def reverse_wordds():
