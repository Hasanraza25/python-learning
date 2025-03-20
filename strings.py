# Three ways of writing strings
name = "Hasan"
name = '''Haram''' # Multi-line string
name = 'Hussain'


# slicing
print(name[1:5]) # 5 excluded
print(name[-4:-1]) # negative slicing
print(name[:5]) # blank means 0
print(name[2:]) # blank means after 2nd index all indices

# slicing with skip value
num = "0123456789"
print(num[1:7:2])
# break in two parts first 
# num[1:7] = 123456 (7 excluded)
# now, skip number by 2 step: 135 will be the answer
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[2:9:3])
# cdefghi => c , f , i =>cfi

# Escape sequences are a special characters to format strings in a specific way, aalways starts with backslah (\)

# Print the following output using one string and an escape sequence:
text = "Hello, World! \nWelcome to Python Programming."
print(text)

# Add a Tab Space
text = "Python\t is\tfun!"
print(text)

# Print a Sentence with Quotes
text = "He said, \"Python is amazing!\""
print(text)

# Print a File Path Correctly
text = "C:\\Users\\John\\Documents" # or r"C:\Users\John\Documents"
print(text)

# Overwrite Text Using Carriage Return (\r)
text = "Hello\rworld man"
print(text)

# Remove the Last Letter from a Word Using Backspace (\b)
text = "Hello\b world"
print(text)

# Print a Formatted Table
text = '''Name\tAge\tCountry
Alice\t25\tPakistan
Bob\t30\tUK
'''
print(text)
print("Hello\b\b\bWorld!")