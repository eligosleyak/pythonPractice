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
# database_password = 'admin123'
# database_username = 'admin'
# username = input("Enter username: ")
# if database_username == username:
#     print(f'Welcome {username}')
#     password = input("Enter password: ")
#     if password == database_password:
#         print(f'Logged in suucessfully')
#     else:
#         print(f'Wrong password')
# else:
#     print(f'Username not found')

# Task 2: Create a KBC / quiz where 5 questions are asked and 5 answers need to be provided after each correct answer score increases by 100
# score = 0
# ans = input('What country has the highest life expectancy?')
# if ans.lower() == 'hong kong':
#     score+=100
#     ans = input('Where would you be if you were standing on the Spanish Steps?')
#     if ans.lower() == 'rome':
#         score+=100
#         ans = input('Which language has the more native speakers: English or Spanish? ')
#         if ans.lower() == 'spanish':
#             score+=100
#             ans = input('What is the most common surname in the United States?')
#             if ans.lower() == 'smith':
#                 score+=100
#                 ans = input('What disease commonly spread on pirate ships? ')
#                 if ans.lower() == 'scurvy':
#                     score+=100
#                     print(f'Successfully answered all questions score is {score}')
#                 else:
#                     print(f'You got {score}')
#             else:
#                 print(f'You got {score}')
#         else:
#             print(f'You got {score}')
#     else:
#      print(f'You got {score}')
# else:
#     print(f'You got {score}')

'''
Looop and iterations:
    -Repeat same task over and over again
    -Can be used for various usecases like asking multiple queries, running program indefinetly and so on.

    -for loop and while loop
        -for loop used whrn we know the starting point and we know the ending point of the loop
        -while loop used when we don't know the ending point
'''
"""
For Loop
"""

# for vara in range(1,10):
#     print(vara)

# print odd number from 1 to 100
#Approach 1
# for vara in range(1,100):
#     if(vara%2 != 0):
#         print(vara)

#Approach 2
# for vara in range(1,100,2):
#     print(vara)

"""
While Loop

while alive:
    if death;
        break
"""
# Task 4: Continuosly take input from user until they give a number divisible by 5
# while True:
#     ans = int(input("Enter a number: "))
#     if ans %5 == 0:
#         break

"""
Functions:
    -definition: Define the function and what it will do
    -calling: Invoke or call that specific function

    -definition of function:
        def function_name(parameters):
            print(parameters)

    -calling of function:
        function_name(5)
"""
#Function to check even or odd number
# def evenNumberChecker(x):
#     if x%2 == 0:
#         print('Even')
#     else:
#         print('Odd')

# evenNumberChecker(5)
# evenNumberChecker(12)
# evenNumberChecker(7)
# evenNumberChecker(69)

# Task 6: Create a function that takes input x and prints us if its a multiple of 10 or not
# a = int(input("Enter a number: "))


# def multipleOfTen(a):
#     if a%10 == 0:
#         print(f'{a} is a multiple of 10')
#     else:
#         print(f'{a} is not a multiple of 10')

# multipleOfTen(a)

"""
Return type function;
    -function that can return output to the main flow of the code
"""

# def evenOddChecker(x):
#     if x%2 == 0:
#         return 'even',x
#     else:
#         return 'odd',x
# op = evenOddChecker(10)
# print(op)

# # Recursive Function
# def factorial(n):
#     #Base Case: if n is 0 or 1, return 1
#     if n==0 or n==1:
#         return 1
#     #Recursive Case: n * factorial of (n-1)
#     else:
#         return n*factorial(n-1)

# #Example usage:
# print(factorial(5)) #Output will be 120

# Task 7: Sum of n numbers
# def suma(n):
#     if n==0:
#         return 0
#     else:
#         return n+suma(n-1)

# print(suma(int(input('Enter a number: '))))

# Task 8 Reverse a string using recursive function

# Global variable and local variable
