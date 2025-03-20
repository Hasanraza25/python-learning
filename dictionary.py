# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python, dictionaries are written with curly brackets, and they have keys and values.

marks = {
    "ALice": 90,
    "Bob": 80,
    "Charlie": 70,
    "David": 60,
    "list": [1,2,3,4,5],    
    0: "HArry",
}

marks = {} # empty dictionary

# Accessing Items
# print(marks["list"])
# print(marks["ALice1"]) # If not found, it will throw an error
# print(marks.get("ALice1")) # If not found, it will return None
# print(marks.get("Bob"))

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# Create a dictionary of five countries and their capital cities.
countries = {
    "India": "New Delhi",
    "USA": "Washington",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
}

print(countries.get("India"))
countries.update({"USA": "Washington DC", "China": "Beijing"})
print(countries)

# Create a dictionary where student names are keys and their scores are values.
marks = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 70,
    "David": 60,
}
marks.update({"Hasan": 50})
print(marks.get("John", 50))

# Create a dictionary with information about a book (title, author, year, and genre).
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "genre": "Fiction",
}
print(book.keys())
print(book.values())
print(book)

student = {"name": "Alice", "age": 22, "grade": "B"}
other_dict = {"age": 23, "university": "XYZ University"}
student.update({"grade": "A", "major": "Computer Science"})
student.update(other_dict)
print(student)

employee = {"name": "John", "salary": 5000, "position": "Manager", "department": "HR"}
# Remove the "salary" key using pop() and store its value.
employee.pop("salary")
employee.popitem()
print(employee)

user_profile = {"username": "jdoe", "email": "jdoe@example.com"}
user_profile.setdefault("age", 30)
print(user_profile)
print(user_profile.setdefault("age"))

# Use fromkeys() to create a dictionary with keys ["name", "age", "gender"] and set all values to "Unknown".
user = dict.fromkeys(["name", "age", "gender"], "Unknown")
print(user)
user = dict.fromkeys(["name", "age", "gender"], "Known")
print(user)

country = {"name": "Japan", "capital": "Tokyo", "population": 126_000_000}
# Remove the "population" key using del.
del country["population"]   
print(country)
# print(country["population"]) # It will throw an error

fruit_prices = {"apple": 3, "banana": 1, "cherry": 2, "date": 5, "almond": 4}
print(sorted(fruit_prices.keys()))
print(sorted(fruit_prices.values(), reverse=True))
# Print the dictionary items sorted by values in ascending order.
print(sorted(fruit_prices.items(), key=lambda x: x[1]))

scores = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 88}
# Find the student with the highest score.
print(max(scores, key=scores.get))

