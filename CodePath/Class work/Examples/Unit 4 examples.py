# Two pointers demo
# valid Palindrome, we will use the U.M.P.I steps by today to implement our solution

# Given a string s, determine if it can become 
# a palindrome by removing at most one character. 
# A plaindrome is a word phrase or sequence that 
# reads the same backwards or forwards
    # Input = "aba"


# Understand:
'''
1. Input a string
1.5 set up our two pointers (left and right, front and final)
2. Output a boolean
3. palindrome is the same backwords and worwards
4. modifying that classic palindrome to allow for one incorrect character.
'''

# Match:
'''
Questions:
    - Does this seem familiar --> yes similar to palindrome
    - Are pointers useful here --> Yes because we are "navigating"t through data, step by step
                **** we need to be in multiple places at the same time
    - How mnay pointers do we need and where do they begin --> 2, one at 0, len(s) -1
    - Are there any simpler sonlutions that come to mind that we can work from? --> classic palindrome
'''

# Plan:
'''
1. we are given a string, 
2.will Implement the classic plaindrome solution first
2.5 we will "wrap" (wrapper) or "plug in" helper functions to add the complexity back in.
3. we need to allow for ONLY ONE invalid character. "aba" "abba" "abac" ...(Modification from our mathc)
    maybe this will use our helper function
    * scoot our pointers one to the right, and one to the left, but onnly one time. If either one is correct, the we will return true
    * only one of them has to be correct,
4. return final result
'''
# Implement:
'''
Given a string s, determine if it can become a palindrome by removing at most one character.
A plaindrome is a word, phrase, or sequence that needs the same backward and forward. 
'''

#   a b b a c
#  0->     <-4 (Which one do we do!?!)

def classic_palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
print(classic_palindrome("abba", 0, 3))
# We demonstrated that the classic plaindrome works


#   a b b a c
#   0       4
# 1) abba
# 2) bbac



def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    # we will iterate through the letters, if something is wrong, we do our scoot where only 1 of the two choices neeeds to be valid
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # we will allow for scooting only ONCE.
            # we will perform normal plaindrome checking on both segments.
            return (classic_palindrome(s, +1, right) or (classic_palindrome(s, left, right - 1)))
    return True
print(valid_palindrome())
