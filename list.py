# Python lists are container to store a set of values of any data type
friends = ["Hasan", "AHmed", "Ali", 0.34, 1, True]

print(friends[0])
print(friends[1:6])

# Create a list with five numbers and append a new number to it.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# add values in list without using built in method
numbers = [1,2,3,4,5]
values = [6,7]
index = 2
          #     [1,2 ]    +  [6,7] +   [3,4,5]
numbers = numbers[:index] + values + numbers[index:]
print("New nums",numbers)

# Create two lists and merge them into one using the extend() method.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Insert the number 100 at index 2 in a list [10, 20, 30, 40].
numbers = [10, 20, 30, 40]
numbers.insert(2, 100)
print(numbers)

# Remove the first occurrence of 3 from [1, 2, 3, 4, 3, 5].
numbers = [1, 2, 3, 4, 3, 5]
numbers.remove(3)
print(numbers)

# Find the index of 50 in [10, 20, 30, 40, 50].
numbers = [10, 20, 30, 40, 50]
print(numbers.index(50))

# Create a list with some duplicate elements and count the occurrences of any number.
numbers = [1, 2, 3, 4, 3, 5]
print(numbers.count(3))

# Sort the list [5, 2, 8, 1, 3] in ascending and then in descending order.
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Reverse a list [100, 200, 300, 400] using the reverse() method.
numbers = [100, 200, 300, 400]
numbers.reverse()
print(numbers)

# Copy a list and modify the original list. Check if the copied list is affected.
original = [1, 2, 3]
original_copy = original.copy()
original.append(4)
print(original)
print(original_copy)

# Remove and return the last element of the list [10, 20, 30, 40, 50] using pop().
numbers = [10, 20, 30, 40, 50]
print(numbers.pop())

# Remove all elements from a list using clear(), then try appending an element to it.
numbers = [1, 2, 3]
numbers.clear()
print(numbers)
numbers.append(4)
print(numbers)

# Find the second occurrence of 5 in [5, 10, 5, 20, 5, 30] and remove it.
numbers = [5, 10, 5, 20, 5, 30]
first_index = numbers.index(5)
second_index = numbers.index(5, first_index + 1)
numbers.pop(second_index)
print(numbers)

# Sort a list of strings ["apple", "banana", "cherry", "date"] in reverse alphabetical order.
fruits = ["apple", "banana", "cherry", "date"]
fruits.sort(reverse=True)
print(fruits)

# Merge two lists and remove duplicates while maintaining order.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list1.extend(list2)
result = []
[result.append(x) for x in list1 if x not in result]
print(result)

# Given a list of numbers, separate them into even and odd lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print(even)
print(odd)
