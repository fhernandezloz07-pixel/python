# Objective 3
# What is string slicing and how does it work?
# String slicing: Lets you extract a portion of a string or work with only a specific part of it with basic syntax of string[start:stop]
my_str = 'Hello world'
print(my_str[1:4]) # ell, note that the stop index is non-inclusive 
    # You can omit the start indice
my_str = 'Hello world'
print(my_str[:7]) # Hello w, this extracts everything from index 0 and up to but not including index 7
    # You can ommit the stop indice
my_str = 'Hello world'
print(my_str[8:]) # rld, this extracts everything from the last indice up to but not including 8
    # You can also ommit the start and stop indices, which will exttact the whole string
my_str = 'Hello World'
print(my_str[:]) # hello world
        # These modifications do not affect the original variable, if we print my_str it will still equal Hello world 
    # step parameter is used to specify the increment between each index in the slice, with sintax string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2]) # Hlowrd, the slicing starts at index 0, stops before 11, and extreacts every second character
        # with the step parameter you can also reverse a string by setting step to -1 and leaving start and stop blank: 
my_str = 'Hello world'
print(my_str[::-1]) # dlrow 
