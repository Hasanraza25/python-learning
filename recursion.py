# Recursion in Python

# Recursion is a programming technique where a function calls itself to solve smaller instances of a problem.
# It is commonly used to solve problems that can be broken down into smaller, similar sub-problems.

# Example 1: Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
print("Factorial of 5:", factorial(5))  # Output: 120

'''

factorial(5)  => 5 * factorial(4)
factorial(4) => 4 * factorial(3)
factorial(3) => 3 * factorial(2)
factorial(2) => 2 * factorial(1)
factorial(1) => 1

factorial(5)  => 5 * 24 = 120
factorial(4) => 4 * 6 = 24
factorial(3) => 3 * 2 = 6
factorial(2) => 2 * 1 = 2
factorial(1) => 1

'''


# Example 2: Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
#                        6 - 1  +           6 - 2
#                        5     x +          4  = 9
# Example usage
print("Fibonacci of 6:", fibonacci(6))  # Output: 8

'''
fibonnci(6) => fibonci(5) + fibonnci(4)
fibonnci(5) => fibonnci(4) + fibonnci(3)
fibonnci(4) => fibonnci(3) + fibonnci(2)
fibonnci(3) => fibonci(2) + fibonnci(1)
fibonnci(2) => fibonnci(1) + fibonnci(0)
fibonnci(1) => fibonnci(0) + 0


fibonnci(6) => 5 + 3 = 8
fibonnci(5) => 3 + 2
fibonnci(4) => 2 + 1 = 3
fibonnci(3) => 1 + 1 = 2
fibonnci(2) => 1 + 0
fibonnci(1) => 0 + 0

'''

# Example 3: Sum of a list using recursion
def sum_list(lst):
    if len(lst) == 0:  # Base case
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # Recursive case

# Example usage
print("Sum of list [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))  # Output: 10

'''

sum_list(1,2,3,4) = 1 + sum_list(2,3,4)
sum_list(2,3,4) = 2 + sum_list(3,4)
sum_list(3,4) = 3 + sum_list(4)
sum_list(4) = 4 + sum_list()

sum_list(1,2,3,4) = 1 + 9 = 10
sum_list(2,3,4) = 2 + 7 = 9
sum_list(3,4) = 3 + 4 = 7
sum_list(4) = 4 + 0 = 4

'''

# Key Concepts of Recursion:
# 1. Base Case: The condition under which the recursion stops.
# 2. Recursive Case: The part of the function where it calls itself.
# 3. Stack Overflow: If the base case is not defined or reached, recursion can go into an infinite loop, causing a stack overflow error.
# 4. Tail Recursion: A special case of recursion where the recursive call is the last operation in the function.

# Example 4: Tail recursion (Python does not optimize tail recursion)
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, accumulator * n)

# Example usage
print("Tail Recursive Factorial of 5:", tail_recursive_factorial(5))  # Output: 120


# Advantages of Recursion:
# - Simplifies code for problems that have a natural recursive structure (e.g., tree traversal, divide-and-conquer algorithms).
# - Makes code easier to read and understand for certain problems.

# Disadvantages of Recursion:
# - Can lead to high memory usage due to function call stack.
# - May be less efficient than iterative solutions for some problems.

# Example 5: Binary search using recursion
def binary_search(arr, target, low, high):
    if low > high:  # Base case: target not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:  # Base case: target found
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Recursive case: search left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Recursive case: search right half

# Example usage
sorted_list = [1, 3, 5, 7, 9]
target = 5
print("Index of target 5:", binary_search(sorted_list, target, 0, len(sorted_list) - 1))  # Output: 2
