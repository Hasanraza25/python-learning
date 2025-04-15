# Functions in Python

# A function is a group of statements that are used to perform a specific task.

# 1. Definition:
# Functions are defined using the `def` keyword followed by the function name and parentheses.
def my_function():
    print("Hello from a function")

# 2. Calling a Function:
# Functions are called by using their name followed by parentheses.
my_function()

# 3. Parameters:
# Functions can accept parameters to pass data into them.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 4. Return Statement:
# Functions can return values using the `return` keyword.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# 5. Default Parameters:
# Functions can have default parameter values.
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Bob")

# 6. Variable Scope:
# Variables defined inside a function are local to that function.
def scope_example():
    local_var = "I am local"
    print(local_var)

scope_example()
# print(local_var)  # This would raise an error.

# 7. *args and **kwargs:
# Functions can accept a variable number of arguments using *args and **kwargs.
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30)

# 8. Lambda Functions:
# Anonymous functions can be created using the `lambda` keyword.
square = lambda x: x ** 2
print(square(4))

# 9. Nested Functions:
# Functions can be defined inside other functions.
def outer_function():
    def inner_function():
        print("I am inner")
    inner_function()

outer_function()

# 10. Higher-Order Functions:
# Functions can accept other functions as arguments or return them.
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * 2, 5))

# 11. Recursion:
# Functions can call themselves (recursion).
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 12. Docstrings:
# Functions can have documentation strings to describe their purpose.
def documented_function():
    """This is a docstring. It describes the function."""
    pass

print(documented_function.__doc__)

# 13. Function Annotations:
# Functions can have type hints using annotations.
def add_with_annotations(a: int, b: int) -> int:
    return a + b

print(add_with_annotations(2, 3))