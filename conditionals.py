# Conditionals in Python are used to make decisions based on a condition.
# The if keyword is used to make a decision based on a condition.
# The else keyword is used to make a decision based on a condition.
# The elif keyword is used to make a decision based on multiple conditions.
# The pass keyword is used to avoid getting an error.
# The and keyword is used to combine two conditions.
# The or keyword is used to combine two conditions.
# The not keyword is used to reverse a condition.
# The in keyword is used to check if a value is present in a sequence.

a = int(input("Enter a number: "))

# if else statement
if(a>=18):
    print("You are eligible to vote.")
# the above space is called indentation
# if the indentation is not proper then it will give error
# if the condition is false then the code inside the else block will be executed
  
else:
    print("You are not eligible to vote.")
    
# if elif else ladder statement
if(a>0):
    print("The number is positive.")
elif(a<0):
    print("The number is negative.")
else:
    print("The number is zero.")

# nested if else statement
if(a>0):
    if(a%2==0):
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")
    
    
print("End of the program.")