'''
1. List Comprehensions and Generator Expressions
    List Comprehensions are a concise way to create lists in Python
    They are faster than using a for loop to create a list
'''
# #Creating a list
# li = [1,2,3,4,5]#static way of creating list
# ci = []
# ci.append(1)#Dynamic way
# odd_number = [i for i in range (1,100,2)]#It can loop inside the list creation itself

'''
List comprehension works best when we are working with  very simple data modification or conmditions 
when complex condition arisies list comprehesion is difficult to code
'''
# Mini Task. You have lis a=[1,2,3,4,5] create alist b which has each element of a squared. b=[1,4,9,16,25]
# a=[1,2,3,4,5]
# # b = []
# # for i in a:
# #     b.append(i**2)

# #Using list comprehension
# b = [element**2 for element in a]
# print(b)

#even off using if
# even = [i for i in range(1,100) if i%2 == 0]
# print(even)

#squared and cube
# snq = [i**2 if i%2 == 0 else i**3 for i in range (1,100) ]
# print (snq)

'''
Generator in pyhton
    -Special type of function that returns multiple value for multiple different instraces using yield
    -def function_name()
        yield statement
'''
# #Simple generator
# def simple_generator():
#     yield 'a'
#     yield 'b'

# #Approach 1 to get output from generator
# for value in simple_generator():
#     print (value)

# print('--'*25)

# #Approch 2
# x = simple_generator()
# print(next(x))
# print(next(x))

#GEnerator Expressions
'''
Create generator object very similar to list comprehension
'''
# squareGen = (x**2 for x in range(10))
# print(squareGen)
# print(list(squareGen))

'''
Create a generator operator that yields all the even numbers using generator expression
Create infinite loop where user is asked to type something
if user types next
display the next value of the generator operator
when the iteration is over the loop must exit {Hint: Using try exceot to handle the situation}
'''
# evennum = (x for x in range(10) if x%2 == 0)
# while True:
#     try:
#         ans = input("Enter: ")
#         if ans == 'next':
#             print(next(evennum))
#         else:
#             ans = input("Enter: ")
#     except:
#         print('Bye Bye')

'''
Lambda:
    -Lambda are orften refered as anonymous function
    -for very short and sweet operation
    -Thesew function are used in conjunction with higher level functions like map, filter and so on.
'''
# x = lambda parameter: parameter**2
# print(x(5))

# sum = lambda x,y: x+y
# print(sum(2,3))

'''
Task 2: Given a list = [1,2,3,4,5,6,7,8,9,10] create a lambda function that returns half of that value and pass each element
of this list to that function and save everything in new list(using list comprehension)
list_2 = [0,5,1,1.5,....]
'''
# list_1 = [i for i in range (1,11) ]
# halflist = lambda list_1: list_1/2
# list_2 = [halflist(i) for i in list_1]
# print (list_2)

#using if else inside lambda
# greater_num = lambda x,y:x if x>y else y
# print(greater_num(2,3))

'''
WAP to take in N(n = number of element on a list)
Loop till n lines and get different numbers
put all the numbers in a list named list_variable
create a lambda function that takes in parameter_1, return 'even' if even number and returns 'odd' if the number is odd
using list comprehension create another list named odd_even if should contain all the output of lambda function
passed over each element of list_variable
Finally crate a dataframe with 2 columns, nmber, even/odd
number of column should have list_variable on it even/odd column should have odd_eveen_list
display the final dataframe
'''
# import pandas as pd
# def main():
#     n = int(input('Number of elements?: '))
#     list_variable = [int(input('Enter a numnber: ')) for i in range(n)]
#     even_odd = lambda parameter_1: 'even' if parameter_1%2 == 0 else 'odd'
#     odd_even = [even_odd(i) for i in list_variable ]
#     ogg = {'Number': list_variable, 'odd/even': odd_even}
#     dataFrame = pd.DataFrame(ogg)
#     print(dataFrame)

# main()

'''
map,filter and reduce
    -map takes in function and collection and iterates all elements one by one over that function
    -map can also be used to map out 2 different parameters from 2 different collections over a function
'''

# list_of_numbers = [i for i in range(11)]
# output_of_map = list(map(lambda x:x**2, list_of_numbers))#Syntax map(function,list/iterable)
# print(output_of_map)

'''
1. Take N from user (Number of elements)
2. Create a lit of length N asking number from user (ask numbers and put in list)
3. Create another list of length N asking number from user (2nd list created with first list)
4. using map figure out which from both list add upto 10. Concat the 2 numbers and display the result in list
'''
# n = int(input('Enter number of elements: '))
# list1 = [int(input('Enter the elements for list 1: ')) for i in range(n)]
# list2 = [int(input('Enter the elements for list 2: ')) for i in range(n)]
# result = list(map(lambda x,y: str(x)+str(y) if x+y == 10 else False,list1,list2))
# print(result)

'''
filter:
    -Filter works very similar to map
    -It takes function and iterable as input
    -Retruns output whenever its true
'''
# numbers = [1,2,3,4,5]
# evens = list(filter(lambda x:x%2 == 0,numbers))

'''
given a list = ['apple','ball','cat','dog','elephant']
create another list of words which have length>3
from the given list
'''
# list1 = ['apple','ball','cat','dog','elephant']
# result = list(filter(lambda x:len(x)>3,list1))
# print(result)

'''
reduce
    -[1,2,3,4,5]
    -multiply(x,y)->x*y
    -reduce(function,iterable,initial_value)
    -It runs the function one by one in cumulative way from left to right
'''
# from functools import reduce
# list_of_numbers = [1,2,3,4,5]
# output = reduce(lambda x,y: x*y,list_of_numbers)
# print(output)

"""
Create a list taking n like done previously
create a function square_and_add_4
return x**2+4
using map create transition_list_1 passing over the function
using filter create another transition_list_2 which accepts only those numbers divisible by 5
finally create a sum of all the numbers of transition_list_2 using reduce
"""
# from functools import reduce
# n = int(input('Enter number of elements: '))
# list1 = [int(input('Enter the elements: ')) for i in range(n)]
# def square_and_add_4(x):
#     return (x**2+4)
# transition_list_1 = list(map(square_and_add_4,list1))
# transition_list_2 = list(filter(lambda x:x%5==0,transition_list_1))
# sum = reduce(lambda x,y:x+y,transition_list_2)
# print(sum)

'''
Decorators:
    -Decorators are special functions that takes in other functions as parameter
    -Decorators are unsderstood by the code editors with @
'''

# def smart_conversion(func):
#     def wrapper(x,y):
#         return func(int(x),int(y))
#     return wrapper

# @smart_conversion
# def division(x,y):
#     return x/y

# @smart_conversion
# def addition(x,y):
#     return x+y

# print(addition('4','2'))
# print(division('4','2'))

'''
Create a function named
division
addition
subtraction
multiplication
create a decorator named identify function and parameters thatr should display which function is running and what are the parameters
'''
def smart_conversion(func):
    def wrapper(x,y):
        print(f"{func.__name__} between {x} and {y}")
    return wrapper
@smart_conversion
def division(x,y):
    return x/y

@smart_conversion
def addition(x,y):
    return x+y

@smart_conversion
def subtraction(x,y):
    return x-y

@smart_conversion
def multiplication(x,y):
    return x*y

print(addition(1,2))