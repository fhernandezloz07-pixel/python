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