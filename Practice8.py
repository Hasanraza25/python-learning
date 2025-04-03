# Write a program using function to find the greatest of three numbers.

def greatest(a,b,c):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    elif(c>a or c>b):
        return c

print(greatest(90,12,78))

# Write a program using function to convert celsius into fahrenheit

def celToFahreheit(celsius):
    formula = (celsius * 9/5) + 32
    return formula

print(celToFahreheit(100)) 

# fahrenheit to celsius

def fToC(fahrenheit):
    formula = (5/9 * (fahrenheit - 32))
    return formula

print(round(fToC(100)))

# How do you prevent a python print() function to print new line at the end?

print("Prevent new line!", end="")
print(" Prevent new line!", end="")

# Write a recursive function to calculate the sum of first n natural numbers.

'''
1
2
3
4
5
6
7
8

sum(n) + sum(n+1)

'''

def sum(n):
    if(n == 0):
        return 0
    return n + sum(n - 1)

n = int(input("Enter number: "))
print(sum(n))

# Write a python function to print first n lines of the following pattern:
# ***
# **     for n = 3
# * 

def printStars(n):
    if n <= 0: # base case is important to define
        return
    print("*" * n)
    return printStars(n-1)

print(printStars(n))

# Write a python function that converts inches to cms.

def inchToCm(i):
    return i * 2.54

print(inchToCm(n))

def cmToInch(cm):
    return cm/2.54

print(cmToInch(n))

# Write a function to remove a given word from a list and strip it at the same time.

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
    
l = ['Hasan', 'Hussain', 'Haram','an']
print(remove(l,'an'))

# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")  # Print instead of return

# Example usage
table(n)  # Prints the table of 5
