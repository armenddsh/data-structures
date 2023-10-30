# Anagram problem exercise

# Construct an algorithm to check whether two words (or phrases) are anagrams or not!

# "An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

# For example: restful and fluster

# Good luck!

def is_anagram(str1, str2):
    str1_array = list(str1)
    str2_array = list(str2)
    
    return all([x in str2_array for x in str1_array])
    