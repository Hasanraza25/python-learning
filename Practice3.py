# Write a Python program to display a user entered name followed by Good Aftermon using input function

# name = input("what is your name: ")
# print(f"Good Afternoon {name}")

# Write a program to fill in a letter template given below with name and date.
letter = '''Hello <|Name|> 
You're Selected! Come on <|Date|>
'''

# name = input("Enter your name: ")
# date = input("Enter Date: ")

# print(letter.replace('<|Name|>', name).replace('<|Date|>', date))

# Write a program to ditect double spaces in a String
text = "Hello! I'm Hasan   Raza."
print(text.find("  ")) # 16th index has double space

# Replace the double Spaces from Problem 3 with Single spaces
print(text.replace("  ", " 3")) # 16th index has double space

# write a progrom to format the following letter using esape sequence
letter = "Dear Harry,\nThis Python Course is nice. \nThanks!"
print(letter)

# 1️⃣ Extract the word "Python" from the string
text = "I am learning Python programming!"
print(text[14:20])

# 2️⃣ Reverse the string using slicing
text = "abcdef"
print(text[::-1]) #fedcba

# 3️⃣ Extract every alternate character from the string
text = "PythonIsAmazing" #PtoIAazn
print(text[0::2])

# 4️⃣ Extract only the last 5 characters from a string
text = "I love programming"
print(text[-5:])

# 5️⃣ Extract the substring "program" from "I love programming"
text = "I love programming"
print(text[7:14])

# 6️⃣ Reverse only the first half of the string
text = "abcdefghijklm" # fedcba ghijklm
print(text[0:6][::-1] , text[6:])

# 7️⃣ Extract every 3rd character from the string, starting from the second character
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
print(text[1::3])

# 8️⃣ Extract only the vowels from the string using slicing and in keyword
text = "Python is Beautiful"

# 9️⃣ Remove the first and last character from a string
text = "OpenAI"
print(text[1:-1])

# 🔟 Reverse every word in a sentence separately
text = "Python is fun"
print(" ".join([word[::-1] for word in text.split()]))
# 1️⃣1️⃣ Extract characters from the string that are at even indexes only
text = "abcdefghijk"
print(text[::2])

# 1️⃣2️⃣ Print only the first 3 and last 3 characters of a string together
text = "PythonProgramming"
print(text[0:3]+text[-3:])

# 1️⃣3️⃣ Extract characters at odd indexes from a given string
text = "0123456789"
print(text[1::2])


# 1️⃣4️⃣ Extract every alternate word from a sentence
text = "I love coding in Python and solving problems"
splittedText = text.split(' ')[::2]
print(" ".join(splittedText))

# 1️⃣5️⃣ Reverse a string, but keep the words in the same order
text = "Python is powerful"
print(" ".join([word[::-1] for word in text.split()]))

# 1️⃣6️⃣ Extract and reverse only the words of even length from a sentence
text = "Python is the best programming language"
print(" ".join([word[::-1] if len(word) % 2 == 0 else word for word in text.split()]))