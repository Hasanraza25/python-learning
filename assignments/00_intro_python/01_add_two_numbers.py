# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))

sum = f"The sum of {num1} and {num2} is {num1 + num2}"
print(sum)