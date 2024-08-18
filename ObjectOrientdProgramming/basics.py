'''
Class:
    -Collection of functions and variables , which can work individually on its own.
    -Example in real world scenario is animal
'''
'''
Object:
    -Its just an instance of class (Its a part of class that has its own independent identity)
    -Dog from animal can be an object, car in vehicles
    -Each object has its own set of attributes/fearures and also act differently
    -Dog has four legs and it barks
'''
class Animal:
    def whatSoundDoesItMake(self,flag):
        if flag.lower() == 'bark':
            print('Hey its a dog!')
        elif flag.lower() == 'meow':
            print('Hey its a cat!')
        else:
            print('Hey its a human!')

species1 = Animal()
species1.whatSoundDoesItMake('Bark')

species2 = Animal()
species2.whatSoundDoesItMake('meow')

species2 = Animal()
species2.whatSoundDoesItMake('lol')

print('--'*50)

'''
Create a class named calculator, That must have following methods
add_2_numbers(), subract_2_numbers(), multiply_2_numbers(), divide_2_numbers()
create 2 different instances of calculator (create 2 methods) and run those methods
'''
class calculator:
    def add_2_numbers(self,x,y):
        print(f'The sum is {x+y}')

    def subract_2_numbers(self,x,y):
        print(f'The subtraction is {x-y}')
        
    def multiply_2_numbers(self,x,y):
        print(f'The multiplication is {x*y}')

    def divide_2_numbers(self,x,y):
        print(f'The division is {x/y}')

sumNsub = calculator()
mulNdiv = calculator()

sumNsub.add_2_numbers(2,5)
sumNsub.subract_2_numbers(5,4)

mulNdiv.multiply_2_numbers(3,7)
mulNdiv.divide_2_numbers(4,2)

print('--'*50)

'''
Constructor:
    -Constructor is used during initialization, such that as soon as an object is created it jumps to conclusion part
    -Syntax for python
        def __init__(self):
            Constructor_code_here()
'''

class KBC:
    def __init__(self,user):
        print(f'Welcome to KBC {user}')

GameForSiddhant = KBC('Sidhannt')
GameForLego = KBC('Lego')

print('--'*50)

