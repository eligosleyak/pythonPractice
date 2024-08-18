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

