# Write a program to find the greatest of four numbers entered by the user

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: ")) 
# c = int(input("Enter the third number: ")) 
# d = int(input("Enter the fourth number: ")) 

# if(a>b and a>c and a>d):
#     print(a, "is the greatest number.")
# elif(b>a and b>c and b>d):
#     print(b, "is the greatest number.")
# elif(c>a and c>b and c>d):
#     print(c, "is the greatest number.")
# else:
#     print(d, "is the greatest number.")
    
# Without if elif else ladder
# greatest = max(a,b,c,d)
# print(greatest, "is the greatest number.")

# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33%, in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# sub1 = int(input("Enter the marks of the first subject: "))
# sub2 = int(input("Enter the marks of the second subject: "))
# sub3 = int(input("Enter the marks of the third subject: "))

# total = sub1+sub2+sub3
# total_percentage = (total/300)*100

# sub1_percentage = (sub1/100)*100
# sub2_percentage = (sub2/100)*100
# sub3_percentage = (sub3/100)*100

# if(sub1_percentage>=33 and sub2_percentage>=33 and sub3_percentage>=33 and total_percentage>=40):
#     print("The student is pass.")
#     print("Percentage is:", total_percentage)
#     print("Percentage is:", sub1_percentage)
#     print("Percentage is:", sub2_percentage)
#     print("Percentage is:", sub3_percentage)
# else:
#     print("The student is fail.")
#     print("Percentage is:", total_percentage)


# A spam comment is definded as a text containing follwoinf keywords:
# ,"buy now", "subscribe this", "click this".
# Write a program to detect these spams.

# p1 = "Make a lot of money"
# p2 = "click this"
# p3 = "subscribe this"
# p4 = "buy now"
    
# comment = input("Enter your comment: ")

# if((comment in p1) or (comment in p2) or (comment in p3) or (comment in p4)):
#     print("The comment is spam.")
# else:
#     print("The comment is not spam.")     
    
# Write a program to find whether a given username contains less than 10 characters or not

# username = input('Enter your username: ')

# if(len(username)<10):
#     print("The username contains less than 10 characters.")
# else:
#     print("The username contains more than 10 characters.")
    
# Write a program which finds out whether a given name is present in a list o rnot

# names = ['John', 'Doe', 'Alice', 'Bob', 'Charlie']

# name = input("Enter the name you want to search: ")

# if(name in names):
#     print("The name is present in the list.")
# else:
#     print("The name is not present in the list.")
    
# Write a program to calculate the grade of a student from this marks from the following schema:

marks = int(input("Enter your marks: "))

if(marks>=90 and marks<=100):
    print("Excellent")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
elif(marks>100):
    print("Invalid marks")
else:
    print("Fail")
    
# Write a program to find out whether a given post is talking about "Hasan" or not

post = "hasan is a good boy but he is little shy."

if("Hasan".lower() in post.lower()):
    print("The post is talking about Hasan.")
else:
    print("The post is not talking about Hasan.")
