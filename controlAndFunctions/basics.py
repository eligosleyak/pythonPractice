'''
Conditional statement
    - Statements where a certain part of code is executed when a condition is satisfies
    -Syntax
        if (condition1.1) and (condition1.2) or (condition2):
            satisfied function()
        else:
            Unsatisfied funtion()
'''

# Even or Odd
# x = 10
# if (x%2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# x = 10
# print(x,type(x))
# if x%3==0:
#     print(f'{x} is odd number')
# elif x!=10:
#     print(f'{x} is 10')
# else:
#     print(f'{x} is an even number')

# Task 1: Take username and password from user check if password is same as the one set by admin
database_password = 'admin123'
database_username = 'admin'
username = input("Enter username: ")
if database_username == username:
    print(f'Welcome {username}')
    password = input("Enter password: ")
    if password == database_password:
        print(f'Logged in suucessfully')
    else:
        print(f'Wrong password')
else:
    print(f'Username not found')

    
