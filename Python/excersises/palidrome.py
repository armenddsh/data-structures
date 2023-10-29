# Palindrome exercise

# "A palindrome is a string that reads the same forward and backward"

# For example: radar or madam

# Our task is to design an algorithm for checking whether a given string is palindrome or not! The aim is to achieve O(N) linear running time.

# Good luck!

# you can define helper methods if needed
def is_palindrome(s):
    if len(s) < 3:
        raise Exception("Sorry, not enough characters") 
        
    startIndex = 0
    lastIndex = len(s) - 1
    
    while startIndex != lastIndex:
        if s[startIndex] != s[lastIndex]:
            return False
        
        startIndex = startIndex + 1
        lastIndex = lastIndex - 1
    
    return True