# Object Oriented Progg. (OOPs)

# Functional Programming --> We create functions to solve the problem
# Programming paradigm where we create classes and objects

# Class --> A template using which we create real-life entities called Objects
# Objects --> A real-life entity which is produced with the help of the class

class Animal:
    # Attributes related to the class

    # Constructors --> function which accepts arguments of the properties and create + initilaise the properties for you
    def __init__(self, kind, color, noOfLegs, isDomestic, isCarnivorous):
        # self.propertyName = parameter
        self.animalKind = kind
        self.animalColor = color
        self.animalNoOfLegs = noOfLegs
        self.animalIsDomestic = isDomestic
        self.animalIsCarnivorous = isCarnivorous

    # Functionalities (Methods) that your objects will perform


# How to create an Object
# objectName = className(parameters passed to the constructors)
dog = Animal("Dog", "black", 4, True, True)
print(dog) # Memory Address of the object -> <__main__.Animal object at 0x7fa2dbaf8e80>
# Access any property of the class --> obejctName.propertyName
print( dog.animalKind )
print( dog.animalColor )
print( dog.animalNoOfLegs )
print( dog.animalIsDomestic )
print( dog.animalIsCarnivorous )

cow = Animal("Cow", "white", 4, True, False)
print( cow )
print( cow.animalKind )
print( cow.animalColor )
print( cow.animalNoOfLegs )
print( cow.animalIsDomestic )
print( cow.animalIsCarnivorous )