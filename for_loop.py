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


# for loop with tuples
my_tuple = (1,2,3,4,5)
for i in my_tuple:
    print(i)