# Reversing an array in-place exercise

# Reversing an array in-place exercise

# In this exercise, you have to reverse a list in O(N) linear time complexity and we want the algorithm to be in-place as well - so the algorithm can not use additional memory (it means you have to manipulate the input list and not create an independent list)!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

# Good luck!

def reverse(nums):
    startIndex = 0
    lastIndex = len(nums) - 1

    while startIndex < lastIndex:
        nums[startIndex], nums[lastIndex] = nums[lastIndex], nums[startIndex]

        startIndex = startIndex + 1
        lastIndex = lastIndex - 1
    
    return nums