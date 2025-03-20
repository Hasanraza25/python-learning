# Given the string "hello world", convert it to uppercase using a string method.
text = "hello world"
print(text.upper())

# Remove leading and trailing spaces from the string " Learn Python ".
text = " Learn Python "
print(text.strip())

# Replace "Java" with "Python" in the string "I love Java".
text = "I love Java"
print(text.replace('Java','Python'))  # original string will not change

# Find the index of "world" in "Hello world!".
text = "Hello world!"
print(text.find("world"))

# Count the number of times 'a' appears in "banana".
text = 'banana'
print(text.count('a'))

# Check if "Python is awesome" starts with "Python".
text = "Python is awesome"
print(text.startswith('Python'))

# Split the string "apple,banana,orange" into a list using , as a delimiter.
text = "apple,banana,orange"
print(text.split(','))

# Convert ['Hello', 'World'] into "Hello World" using a built-in method.
arr = ['Hello', 'World']
print(" ".join(arr))

# Swap uppercase and lowercase letters in "PyThOn".
text = "PyThOn"
print(text.swapcase())

# Check if "Hello" contains only letters.
text = "Hello"
print(text.isalpha())

# Check if "12345" contains only digits.
text = "12345"
print(text.isdigit())

# Check if "Python123" contains only letters and numbers.
text = "abcd123"
print(text.isalnum())

# Find "fun" in "Python is fun!" and replace it with "awesome".
text = "Python is fun!"
print(text.replace('fun', 'awesome'))

# Center the string "Hello" inside a field of 10 characters, using - as a filler.
text = 'helloo'
print(text.center(10, '-'))

# Right-align "Hello" within 10 spaces, filling with *.
text = 'Hello'
print(text.rjust(10,'*'))

# Convert "42" into "00042" using zfill() to make it 5 characters long.
text = '42'
print(text.zfill(5))