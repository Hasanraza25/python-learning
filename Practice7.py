# Write a program to print multiplication table of a given number using for loop.

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")
    

# # Write a program to greet all the person names in a list l1 and which starts with s.
# l1 = ['John', 'Doe', 'Alice', 'Bob', 'Charlie', 'Sam', 'Sophie']
# for name in l1:
#     if(name.startswith('S')):
#         print(f"Hello {name}!")
        
# # Attempt problem 1 with while loop.

# i = 1
# while(i<=10):
#     print(f"{num} x {i} = {num * i}")
#     i += 1
    
# Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))

# if n < 2:
#     print(f"{n} is not prime.")
# else:
#     for i in range(2, int(n ** 0.5) + 1):  
#         if n % i == 0:
#             print(f"{n} is not prime.")
#             break
#     else:
#         print(f"{n} is prime.")

# Write a program to find the sm of first n natural numbers using while loop.

i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {sum}")

# Write a program to find the factorial of a given number using for loop.

factorial = 1
for i in range(1,n+1):
    factorial *= i
    i += 1
print(f"The factorial of {n} is: {factorial}")

# Write a program to print the following star pattern:
#   *
#  ***
# ***** for n = 3

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))
    
# Write a program to print the following star pattern:
# *
# ***
# ***** for n = 3

for i in range(1,n+1):
    print("*" * (2 * i - 1))


# Write a program to print the following star pattern:
# ***
# * *
# ***


for i in range(1,n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")


# Write a program to print multiplication table of n using for loop in reverse order.

for i in range(1, 11):
    print(f"{n} x {11 - i} = {n*(11-i)}")    
    