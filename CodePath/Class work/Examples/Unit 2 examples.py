# PROBLEM 1
# Given a list of strings words, 
# group the strings that are anagrams of each other.
    # An anagram is defined 
    # as a word formed by rearranging 
    # the letters of another, s
    # uch as "eat" and "tea".

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Expected output: 
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Plan (Logica steps and using related data structures)
'''
1. takes in a list of words
2. we will make a new dictionary (starting empty)
3. iterate through our original list (for loop)
4. check if the current word is an anagram of something else
    4b. figure how to assess anagrams
5. keep track / update our dicitonary with new desicions. (dictionary values)
6. return a list of grouped words
'''

# Implement
def groups_anagrams(words):
    anagram_dictionary = {} # tracking aet to a list of  words that fit that category
    # aet -> [tea, eat, ate]

    for word in words:
        sorted_word = str(sorted(word)) # eat -> aet, tea -> aet, ate -> aet
   
    # if thing is in dictionary
    # else if thing is not in dictionary
        if sorted_word not in anagram_dictionary:
            anagram_dictionary[sorted_word] = [word] # then add it to anagram dictionary if not in it!
        else: 
            anagram_dictionary[sorted_word].append(word) # access that list 

    return list(anagram_dictionary.values())

# Test run
print(groups_anagrams(words))

# What did I learn? 

print("-------------------------------------------------------------------------------")
# PROBLEM 2
# understand (inputs, outputs, datatypes, core logic)
'''
input: tuples, always same size, 0 category,1 value(item)
Output: dictionary, keys categories, values will be the count
logic: want to group and count by category
'''

# - Input: items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
# - Output: {"fruits": 2, "vegetables": 1}
    # This is because there are 2 fruit categories and only one vegetable category
'''

'''
# Plan (Hint: how do we use dictionaries to grouo things together?)

# Implement
def count_by_category(items):
    count_dictionary = {} # starts emty dictionary: key = category, values = count 

    for item in items: # Each item becomes a tuple like ("fruits", "apple")
    # item is a tuple, 0, 1
        current_category = item[0] # extract the category only!!!
    
    # Count the Categories
        if current_category not in count_dictionary:
            # its the 1st time we are seeing it
            count_dictionary[current_category] = 1
        else:
            # we have seen it before
            count_dictionary[current_category] += 1

    return count_dictionary

# Test it
test_items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
# Tuple is like a small container that keeps related information grouped: 
# something like ("fruits", "apple")
    # in thi example tuple has two pieces of info
        # index 0 -> "fruits"
        # index 1 -> "apple"
print(count_by_category())
