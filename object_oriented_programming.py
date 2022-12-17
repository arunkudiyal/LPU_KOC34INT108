# Object Oriented Progg. (OOPs)

# Functional Programming --> We create functions to solve the problem
# Programming paradigm where we create classes and objects

# Class --> A template using which we create real-life entities called Objects
# Objects --> A real-life entity which is produced with the help of the class

# class Animal:
#     # Attributes related to the class

#     # Constructors --> function which accepts arguments of the properties and create + initilaise the properties for you
#     def __init__(self, kind, color, noOfLegs, isDomestic, isCarnivorous):
#         # self.propertyName = parameter
#         self.animalKind = kind
#         self.animalColor = color
#         self.animalNoOfLegs = noOfLegs
#         self.animalIsDomestic = isDomestic
#         self.animalIsCarnivorous = isCarnivorous

#     # Functionalities (Methods) that your objects will perform


# # How to create an Object
# # objectName = className(parameters passed to the constructors)
# dog = Animal("Dog", "black", 4, True, True)
# print(dog) # Memory Address of the object -> <__main__.Animal object at 0x7fa2dbaf8e80>
# # Access any property of the class --> obejctName.propertyName
# print( dog.animalKind )
# print( dog.animalColor )
# print( dog.animalNoOfLegs )
# print( dog.animalIsDomestic )
# print( dog.animalIsCarnivorous )

# cow = Animal("Cow", "white", 4, True, False)
# print( cow )
# print( cow.animalKind )
# print( cow.animalColor )
# print( cow.animalNoOfLegs )
# print( cow.animalIsDomestic )
# print( cow.animalIsCarnivorous )


# JS -> Number -> methods

# 1. Encapsulation --> You are supposed to create a single unit, a unit conatining the attributes and methods, which is called a class
class Number:
    # Attribute | Data Members | Properties
    # Constructor -> i. Default Constructors [Without arguments] ii. Parameterized Constructor
    # def __init__(self): ----
    def __init__(self, num1, num2):
        # 2. Abstraction --> A way to ony give user details which are necessary, and hide the implementation detail as much possible
        self.__sum = 0
        self.num1 = num1
        self.num2 = num2

    # Methods --> Functionalities which you want to provide to your objects
    # There should be no method with the same name but different arguments.
    def sum(self):
        self.__sum = self.num1 + self.num2
        return self.__sum

    def otherTypeOfSum(self, num3):
        return self.num1 + self.num2 + num3

    def difference(self):
        return self.num1 - self.num2

    def product(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2

    def power(self):
        return self.num1 ** self.num2

    def modulous(self):
        return self.num1 % self.num2

    def completeDivide(self):
        return self.num1 // self.num2

# Create the objects
# Access the attributes of the class
myNumbers = Number(100, 2)
print( myNumbers.num1 )
print( myNumbers.num2 )
print( myNumbers.sum() )

# myNumbers = Number(100, 2)
# print( 'The sum is - {}'.format(myNumbers.otherTypeOfSum(100)) )
# print( 'The sum is - {}'.format(myNumbers.sum()) )
# print( 'The difference is - {}'.format(myNumbers.difference()) )
# print( 'The product is - {}'.format(myNumbers.product()) )
# print( 'The division is - {}'.format(myNumbers.divide()) )
# print( 'The modulous is - {}'.format(myNumbers.modulous()) )
# print( 'The completeDivide is - {}'.format(myNumbers.completeDivide()) )
# print('---------- * ----------')
# myNumbersTwo = Number(20, 2)
# print( 'The sum is - {}'.format(myNumbersTwo.sum()) )
# print( 'The difference is - {}'.format(myNumbersTwo.difference()) )
# print( 'The product is - {}'.format(myNumbersTwo.product()) )
# print( 'The division is - {}'.format(myNumbersTwo.divide()) )
# print( 'The modulous is - {}'.format(myNumbersTwo.modulous()) )
# print( 'The completeDivide is - {}'.format(myNumbersTwo.completeDivide()) )


# 4 Pillars of OOPs
# 1. Encapsulation
# 2. Abstraction
# 3. Polymorphism
# 4. Inheritance