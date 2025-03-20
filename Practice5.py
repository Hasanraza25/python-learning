# Write a program to create a dictionary of urdu words with values as their english translation. 
# Provide user with an option to look it up.

translations = {
    "Aam" : "Mango",
    "phal" : "Fruit",
    "papita" : "Papaya",
    "badam" : "Almond",
    "tarbooza": "Watermelon"
}

# word = input("Enter Urdu word: ")
# print(translations.get(word))

# Write a program to input 8 numbers from the user and display all unique numbers once.
# my_set = set()
# input1 = input("Enter number 1: ")
# my_set.add(int(input1))
# input2 = input("Enter number 2: ")
# my_set.add(int(input2))
# input3 = input("Enter number 3: ")
# my_set.add(int(input3))
# input4 = input("Enter number 4: ")
# my_set.add(int(input4))
# input5 = input("Enter number 5: ")
# my_set.add(int(input5))
# input6 = input("Enter number 6: ")
# my_set.add(int(input6))
# input7 = input("Enter number 7: ")
# my_set.add(int(input7))
# input8 = input("Enter number 8: ")
# my_set.add(int(input8))

# print(my_set)

# Can we have a set with 18(int) and "18"(str) as a values in it ?
myset = {18, "18"}
print(myset)

# What will be the length of following set s: 
s = set()
s.add (20)
s.add (20.0)
s.add ("20")
print(s) 
# = length of s after these opeestion ?

s = {}
print(type(s))
# what is the type of s?

# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and
# use keys as their names. Assume that names are unique 

d = {}

name = input("Enter friend name: ")
lang = input("Enter language name: ")

d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")

d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")

d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")

d.update({name: lang})

print(d)

# Can you change the values inside a list which is Contained in Set?
s = {8,7, 12,"Harry", [1,2]}
