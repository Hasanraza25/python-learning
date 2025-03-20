# A set in python is:
# - An unordered collection of unique elements.
# - Defined using curly braces {} or the set() function and are unindexed(can't access by index)
# - There is no way to change items in sets, but you can remove and then add items.
# - Cannot contain duplicate elements.
# - Mutable types (like lists) cannot be elements in a set.
# - Immutable types (like tuples) can be elements in a set.
# - Useful for membership testing and eliminating duplicate entries.
# - Supports set operations like union, intersection, difference, and symmetric difference.

my_set = {6, 1, 22, 31, 41, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# my_set = set() # empty set

duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# my_set = {1, 2, [3, 4]}  # ❌ Error: Lists are mutable, they cannot be stored inside a set.
my_set = {1, 2, (3, 4)} # ✅ Since tuples are immutable, they can be inside a set.
print(my_set)  


# my_set.add(4)
# print(my_set)

# my_set.update([21,22,23,24,25])
# print(my_set)

# Basic Set Operations
numbers = {10, 20, 30, 40, 50}
numbers.add(60)
numbers.remove(10)
# numbers.remove(100) # error occurs bcz 100 not exists
numbers.discard(110) # No error, but nothing happens
numbers.update([70, 80, 90] )
print(numbers)

# Removing Duplicates Using a Set
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 5, 7, 8, 8]
numbers_sets = set(numbers)
print(list(numbers_sets))

vowels = {'a', 'e', 'i', 'o', 'u'}
print("e" in vowels)
print("z" in vowels) 

# Set Union, Intersection, and Difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)   
print(A.union(B))   
print(A & B)
print(A.intersection(B))   
print(A - B)
print(A.difference(B))
print(A.symmetric_difference(B))

# 5. Subset and Superset Checks
X = {1, 2, 3}
Y = {1, 2, 3, 4, 5, 6}

print(X.issubset(Y))
print(Y.issuperset(X))
print(X.isdisjoint(Y)) # checks if two sets have NO common elements.

# Finding Common Elements Between Two Lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

set1 = set(list1)
set2 = set(list2)
print(set1 & set2)

# Removing All Elements from a Set
cities = {"Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"}
cities.clear()
print(cities)

# Pop an Element from a Set
numbers = {1, 2, 3, 4, 5, 6}
print(numbers.pop())
print(numbers)

# Find Unique Words in a Sentence
sentence = "Python is fun and Python is powerful"
words = sentence.split()
converted_set = set(words)
print(converted_set)

# Removing Duplicates from a List of Tuples
data = [(1, 2), (2, 3), (1, 2), (4, 5), (2, 3)]
set_data = set(data)
print(sorted(list(set_data)))

# Count Unique Elements in a List Using a Set
numbers = [10, 20, 30, 10, 20, 40, 50, 30, 60]
set_nums = set(numbers)
print(len(set_nums))

# Find Elements Present in One Set but Not Another
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 - set2)

values = [5, 1, 3, 2, 5, 4, 1, 3]
set_values = set(values)
# Convert a List into a Set and Sort It
print(sorted(set_values))

# Finding Missing Numbers Using Sets
full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
partial_set = {2, 4, 6, 8, 10}
print(full_set - partial_set)

# Find Common Letters in Two Words
word1 = "computer"
word2 = "communication"
set1 = set(word1)
set2 = set(word2)
print(set1 & set2)

# Merge Multiple Sets
A = {1, 2, 3}
B = {4, 5, 6}
C = {7, 8, 9}
A |= B | C
print(A)
