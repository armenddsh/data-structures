import numpy as np

# Create a 1D array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Print the array
print(array)

# Print the first element of the array
print(array[0])

# Print the last element of the array
print(array[-1])

# Print the first 3 elements of the array
print(array[:3])

# Print the last 3 elements of the array
print(array[-3:])

# Print the elements of the array from index 3 to index 6
print(array[3:6])

# Print the elements of the array from index 3 to index 6, skipping 2 elements
print(array[3:6:2])

# Print the elements of the array from index 3 to index 6, skipping 2 elements, in reverse order
print(array[6:3:-2])

# Print the elements of the array in reverse order
print(array[::-1])

# Print the elements of the array in reverse order, skipping 2 elements
print(array[::-2])