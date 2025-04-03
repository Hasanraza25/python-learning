# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
my_list = ['John', 'Doe', 'Alice', 'Bob', 'Charlie']
for i in my_list:
    print(i)
    
# For loop with list
# Range function is used to generate a sequence of numbers.
# range(start, stop, step)

for i in range(0,5):
    print(my_list[i])
    
for i in range(0,5,2):
    print(my_list[i]) # 0,2,4

# The in keyword is used to check if a value is present in a sequence.

# for loop with tuples
my_tuple = (1,2,3,4,5)
for i in my_tuple:
    print(i)
    
    
# for loop with strings
my_string = "Hello World"
for i in my_string:
    print(i)


# for loop with dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(key, value)
    
# for loop with else statement
for i in range(5):
    print(i) # answer is 0,1,2,3,4 
else:
    print("The loop has ended.")
    
# the else statement will be executed after the for loop has completed its execution.

# for loop with break statement
for i in range(0,90):
    if(i==50):
        break # the loop will be terminated when i=50
    print(i)

# the else statement will not be executed if the loop is terminated by a break statement

for i in range(0,90):
    if(i==50):
        break # the loop will be terminated when i=50
    print(i)
else:
    print("The loop has ended.")
    
# for loop with continue statement
for i in range(0,90):
    if(i==50):
        continue
    print(i) # the loop will skip the iteration when i=50
# the continue statement will skip the current iteration and continue with the next iteration.

#  for loop with pass statement
for i in range(0,90):
        pass # the pass statement will do nothing and the loop will continue with the next iteration
# the pass statement will not skip the current iteration and continue with the next iteration.

