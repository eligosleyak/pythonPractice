'''
List
    - List is a collection datatype that is capable of holding more than 1 variable
    - Its very similar to Array but has 1 fundamental difference
    - It is hetertogeneous for these you can put in any type of values (any datatype)
    - It is demoted with '[' brackets
    - Each value has index or location associated
'''
# #address = [0,1,2,3,4]
# list_var = [1,2,3,4,5]
# print(list_var, type(list_var),list_var[0])
# print(len(list_var))
# print('--'*25)
# #Iterating over list using index value
# for i in range(0,len(list_var)):
#     # i basically has the index value
#     print(list_var[i])
# print('--'*25)
# # Iterating over each value itself
# for list_element in list_var:
#     print(list_element)
# print('--'*25)
# #For finding out index and value in list:
# for list_index, list_element in enumerate(list_var):
#     print(list_index,list_element)

# Task 1: Loop over each element of this list and show only even number
# li = [1,2,3,4,5]
# for i in range(0,len(li)):
#     if li[i]%2==0:
#         print(li[i])

#How to add elements to list
# lis = []
# print(lis,len(lis))

# print('--'*25)

# #staticly add element to list, this is worst possible approach
# lis = [1]
# print(lis)

# print('--'*25)

# #Dynamically adding element to the list
# lis.append(2)
# lis.append(3)
# print(lis)

# print('--'*25)

# lis4 = []
# for an_element in range(1,10):
#     lis4.append(an_element)

# print(lis4)

# Task 2: Create a list that should contain all even numbers from 1 to 100
# lis4 = []
# for an_element in range(1,100):
#     if an_element%2==0:
#      lis4.append(an_element)

# print(lis4)

#Slicing in list

# lis5 = [1,2,3,4,5]
# print(lis5[1:])
# print(lis5[1:4])

# # Removing element from list
# lis = [1,2,3,4,5,6,7,8]

# #easiest way is to use pop
# lis.pop(2)
# print(lis)

#Task 3: Create a list of numbers from 0-100 using append. remove all the odd numbers from that list
# lis = []
# for a in range(0,101):
#     lis.append(a)
# print(lis)

# for a,b in enumerate(lis):
#     if b%2 != 0:
#         lis.pop(a)

# print(lis)

'''
Dictionary
    - It is a collection datatype with key and value pair
    - Works on similar concept as hash mapping
    - key holds the address of element
    - Classic dictionary is example
        word: meaning
    - It is demoted by '{' bracket
'''

# dictionary_list = {
#     'key_1': 10,
#     'key_2': 20,
# }

# print(dictionary_list['key_1'])

# print(dictionary_list.keys(),dictionary_list.values())

# Adding to dictionary

# Using list

# lis = ['apple','ball','cat']
# val = ['red color fruit','something to play with','animal that makes meow sound']
# dic = dict(zip(lis,val))
# print(dic)

# Task 4: Create LBC quiz question ans dictionary using zip function
# ques = [
#     'What country has the highest life expectancy',
#     'Where would you be if you were standing on the Spanish Steps?',
#     'Which language has the more native speakers: English or Spanish? ',
#     'What is the most common surname in the United States?',
#     'What disease commonly spread on pirate ships? ',
# ]
# ans = [
#     'hong kong',
#     'rome',
#     'spanish',
#     'smith',
#     'scurvy'
# ]
# kbc = dict(zip(ques,ans))

# print(kbc)

# Task 4: Create LBC quiz question ans dictionary using zip function, take user input
# qn = []
# ans = []
# for i in range(1,5): 
#     qn.append(input('Enter question: '))
#     ans.append( input('Enter ans: '))

# kbc = dict(zip(qn,ans))

# print(kbc)

# Approach 2 using update
# dic = {
#     'key1': 10,
#     'key2': 20,
# }

# print(dic)

# dic.update({'key3': 30, 'key4': 40})

# print(dic)

#Approach 3 using append
def reverse(s):
    if s=='':
        return s
    else:
        return reverse(s[1:])+s[0]

output = reverse('apple')
print(output)