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
lis4 = []
for an_element in range(1,100):
    if an_element%2==0:
     lis4.append(an_element)

print(lis4)