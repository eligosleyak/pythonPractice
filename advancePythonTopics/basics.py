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
#Simple generator
def simple_generator():
    yield 'a'
    yield 'b'

#Approach 1 to get output from generator
for value in simple_generator():
    print (value)

print('--'*25)

#Approch 2
x = simple_generator()
print(next(x))
print(next(x))