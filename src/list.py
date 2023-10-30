

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

# Print the elements of the array in reverse order, skipping 2 elements, from index 6 to index 3
print(array[6:3:-2])

# Append an element to the array
array.append(10)

# Print the array
print(array)

# Insert an element at index 3
array.insert(3, 11)

# Print the array
print(array)

# Remove the first element of the array
array.pop(0)

# Print the array
print(array)

# Remove the last element of the array
array.pop()

# Print the array
print(array)

# Remove the element at index 3
array.pop(3)

# Print the array
print(array)

# Remove the element 11
array.remove(11)

# Print the array
print(array)

# Remove the elements from index 3 to index 6
del array[3:6]

# Print the array
print(array)

# Length of the array
print(len(array))

# Minimum value of the array
print(min(array))

# Maximum value of the array
print(max(array))

# Sum of the elements of the array
print(sum(array))

# Sort the array
array.sort()

# Print the array
print(array)
