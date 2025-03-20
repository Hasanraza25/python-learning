# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# It is defined using parentheses () and elements are separated by commas.
# It is similar to a list but it is immutable.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple without parentheses (comma-separated values)
tuple2 = 10, 20, 30
print(tuple2)  # Output: (10, 20, 30)

single_element_tuple = (10,)
print(single_element_tuple)  # Output: (10,)

# Create a tuple with numbers (1, 2, 3, 4, 5) and print its length.
numbers = (1, 2, 3, 4, 5)
print(len(numbers))

# Use the count() method to find how many times 3 appears in (3, 5, 3, 7, 3, 8).
numbers = (3, 5, 3, 7, 3, 8)
print(numbers.count(3))

# Find the index of 40 in the tuple (10, 20, 30, 40, 50).
numbers = (10, 20, 30, 40, 50)
print(numbers.index(40))

# Convert a list [5, 10, 15, 20] into a tuple.
numbers = [5, 10, 15, 20]
print(tuple(numbers))

# Find the maximum and minimum values in (100, 50, 300, 200).
numbers = (100, 50, 300, 200)
print(max(numbers))
print(min(numbers))

# Given a tuple (10, 20, 30, 40, 50), sort it in ascending order using sorted().
numbers = (10, 20, 30, 40, 50)
print(sorted(numbers))

# Reverse a tuple (1, 2, 3, 4, 5) without using reversed().
numbers = (1, 2, 3, 4, 5)
print(numbers[::-1])

# Use any() to check if at least one non-zero element is present in (0, 0, 0, 5, 0).
numbers = (0, 0, 0, 5, 0)
print(any(numbers))

# Use all() to check if all elements in (1, 2, 3, 4, 5) are non-zero.
numbers = (1, 2, 3, 4)
print(all(numbers))

# Write a function that returns the sum of all elements in a tuple.
numbers = (1,2,3,4,5)
print(sum(numbers))

# Merge two tuples (1, 2, 3) and (4, 5, 6), and then sort the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(sorted(result))

# Remove duplicates from a tuple (5, 10, 5, 20, 5, 30), keeping only unique values.
numbers = (5, 10, 5, 20, 5, 30)
unique_numbers = tuple(set(numbers))
print(unique_numbers)

# Convert a tuple ("apple", "banana", "cherry") into a string "apple, banana, cherry".
fruits = ("apple", "banana", "cherry")
print(", ".join(fruits))

# Given a tuple of numbers (10, 20, 30, 40), find their average.
numbers = (10, 20, 30, 40)
average = sum(numbers) / len(numbers)
print(average)

# Given a tuple (1, 2, (3, 4), 5), access the number 4.
numbers = (1, 2, (3, 4), 5)
print(numbers[2][1])