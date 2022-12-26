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
# class Number:
#     # Attribute | Data Members | Properties
#     # Constructor -> i. Default Constructors [Without arguments] ii. Parameterized Constructor
#     # def __init__(self): ----
#     def __init__(self, num1, num2):
#         # 2. Abstraction --> A way to ony give user details which are necessary, and hide the implementation detail as much possible
        
#         # Private Attribute
#         self.__sum = 0
#         # Public Attributes
#         self.num1 = num1
#         self.num2 = num2

#     # Methods --> Functionalities which you want to provide to your objects
#     # There should be no method with the same name but different arguments.
#     def sum(self):
#         self.__sum = self.num1 + self.num2
#         return self.__sum

#     # Private Method
#     def __sample_function(self, name):
#         print(name)

#     def otherTypeOfSum(self, num3):
#         return self.num1 + self.num2 + num3

#     def difference(self):
#         return self.num1 - self.num2

#     def product(self):
#         return self.num1 * self.num2
    
#     def divide(self):
#         return self.num1 / self.num2

#     def power(self):
#         return self.num1 ** self.num2

#     def modulous(self):
#         return self.num1 % self.num2

#     def completeDivide(self):
#         return self.num1 // self.num2

# # Create the objects
# # Access the attributes of the class
# myNumbers = Number(100, 2)
# print( myNumbers.num1 )
# print( myNumbers.num2 )
# print( myNumbers.sum() )
# myNumbers.__sample_function('Arun')

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


# 4 Pillars of OOPs - 

# 1. Encapsulation
# 2. Abstraction
# 3. Polymorphism
# 4. Inheritance --> A mechanism in which you can inherit(adapt) all the attributes and methods from one class (Parent) to another class (Child).

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def getName(self):
#         return self.__name

#     def getAge(self):
#         return self.__age

#     def setName(self, newName):
#         self.__name = newName

#     def setAge(self, newAge):
#         self.__age = newAge

#     def getPersonDetails(self):
#         return 'Hi, my name is {} and I am {} years old'.format(self.__name, self.__age)

# # class ChildClass(ParentClass):
# class Student(Person):
#     def __init__(self, name, age, standard, rno, percentage):
#         # Parent Properties -> super().
#         super().__init__(name, age)
#         # Child Properties 
#         self.__standard = standard
#         self.__rno = rno
#         self.__percentage = percentage

#     # Getter & Setter Methods
#     # --> Getter methods helps you read the data; Setter methods helps you to update the data

#     # Getter
#     def getStandard(self):
#         return self.__standard
    
#     def getRno(self):
#         return self.__rno
    
#     def getPercentage(self):
#         return self.__percentage

#     # Setter
#     def setStandard(self, newStandard):
#         self.__standard = newStandard
    
#     def setRno(self, newRno):
#         self.__rno = newRno
    
#     def setPercentage(self, newPercentage):
#         self.__percentage = newPercentage

#     def getStudentsRecords(self):
#         return 'Hi, my name is {} . I am {} years old, with roll no {}. I scored {} in {}'.format(super().getName(), super().getAge(), self.__rno, self.__percentage, self.__standard)


# # Objects
# # studentOne = Student("Anurag", 19, 'BTech - 1st year', '12217365', 92)
# # print( studentOne.getStudentDetails() )
# # studentOne.setName("Anurag Chauhan")
# # print( studentOne.getStudentsRecords() )
# # print('------------ x -------------')
# # studentOne = Student("Noya", 19, 'BTech - 1st year', '12217365', 95)
# # print( studentOne.getStudentDetails() )
# # studentOne.setName("Noya Lasheen")
# # print( studentOne.getStudentsRecords() )

# studentOne = Student("Anurag", 19, 'BTech - 1st year', '12217365', 92)
# print( studentOne.getPersonDetails() )
# print( studentOne.getStudentsRecords() )

# Types of Inheritance -->

# Simple Inheritance
# Parent Class
# class A:
#     def __init__(self, prop1, prop2):
#         self.__prop1 = prop1
#         self.__prop2 = prop2

#     # Getter Methods --> Helper method which helps us access the private properties from the class (BUT not directly)
#     def getProp1(self):
#         return self.__prop1

#     def getProp2(self):
#         return self.__prop2

# # Child Class
# class B(A):
#     def __init__(self, prop1, prop2, prop3, prop4):
#         # Always call the parent constructor first before creating the new properties
#         # super() --> helps you to access all the public properties & public methods from the parent class [CONSTRUCTOR INCLUDED]
#         super().__init__(prop1, prop2)
#         # define the new properties
#         self.__prop3 = prop3
#         self.__prop4 = prop4

#     def getDetails(self):
#         return 'Prop1 --> {}, Prop2 --> {}, Prop3 --> {}, Prop4 --> {}'.format( super().__prop1, super().__prop2, self.__prop3, self.__prop4 )


# HIERACHICHAL INHERITANCE
# # Parent Class - 1
# class A:
#     def __init__(self, prop1, prop2):
#         self.__prop1 = prop1
#         self.__prop2 = prop2

#     # Getter Methods --> Helper method which helps us access the private properties from the class (BUT not directly)
#     def getProp1(self):
#         return self.__prop1

#     def getProp2(self):
#         return self.__prop2

# # Parent Class - 2
# # Child Class - 1
# class B(A):
#     def __init__(self, prop1, prop2, prop3, prop4):
#         # Always call the parent constructor first before creating the new properties
#         # super() --> helps you to access all the public properties & public methods from the parent class [CONSTRUCTOR INCLUDED]
#         super().__init__(prop1, prop2)
#         # define the new properties
#         self.__prop3 = prop3
#         self.__prop4 = prop4

#     def getProp3(self):
#         return self.__prop3

#     def getProp4(self):
#         return self.__prop4

# # Child Class
# class C(B):
#     def __init__(self, prop1, prop2, prop3, prop4, prop5, prop6):
#         super().__init__(prop1, prop2, prop3, prop4)
#         self.__prop5 = prop5
#         self.__prop6 = prop6

#     def getDetails(self):
#         return 'Prop1 --> {}, Prop2 --> {}, Prop3 --> {}, Prop4 --> {}, Prop5 --> {}, Prop6 --> {}'.format(super().getProp1(), super().getProp2(), super().getProp3(), super().getProp4(), self.__prop5, self.__prop6)

# cObj = C(100, 150, 200, 250, 300, 360)
# print( cObj.getDetails() )


# MULTIPLE INHERITANCE

# Parent Class - 1
# class A:
#     def __init__(self, prop1, prop2):
#         self.__prop1 = prop1
#         self.__prop2 = prop2

#     # Getter Methods --> Helper method which helps us access the private properties from the class (BUT not directly)
#     def getProp1(self):
#         return self.__prop1

#     def getProp2(self):
#         return self.__prop2

# # Parent Class - 2
# class B:
#     def __init__(self, prop3, prop4):
#         # define the new properties
#         self.__prop3 = prop3
#         self.__prop4 = prop4

#     def getProp3(self):
#         return self.__prop3

#     def getProp4(self):
#         return self.__prop4

# # Child Class
# class C(B, A):
#     def __init__(self, prop1, prop2, prop3, prop4, prop5, prop6):
#         # Supposed to call the parent(s) constructor
#         # nameOfTheParent.__init__(self)
#         A.__init__(self, prop1, prop2)
#         B.__init__(self, prop3, prop4)
#         self.__prop5 = prop5
#         self.__prop6 = prop6

#     def getDetails(self):
#         return 'Prop1 --> {}, Prop2 --> {}, Prop3 --> {}, Prop4 --> {}, Prop5 --> {}, Prop6 --> {}'.format(super().getProp1(), super().getProp2(), super().getProp3(), super().getProp4(), self.__prop5, self.__prop6)

#     # def getDetails(self):
#     #     return 'Prop1 --> {}, Prop2 --> {}, Prop5 --> {}, Prop6 --> {}'.format(super().getProp1(), super().getProp2(), self.__prop5, self.__prop6)

# # Object
# cObj = C(100, 200, 300, 400, 500, 600)
# print( cObj.getDetails() )


# HYBRID INHERITANCE
class F:
    def __init__(self, prop5, prop6):
        self.__prop5 = prop5
        self.__prop6 = prop6

    def getProp5(self):
        return self.__prop5

    def getProp6(self):
        return self.__prop6

class E(F):
    def __init__(self, prop5, prop6, prop7, prop8):
        super().__init__(prop5, prop6)
        self.__prop7 = prop7
        self.__prop8 = prop8

    def getProp7(self):
        return self.__prop7

    def getProp8(self):
        return self.__prop8

class B(F):
    def __init__(self, prop5, prop6, prop0, prop00):
        super().__init__(prop5, prop6)
        self.__prop0 = prop0
        self.__prop00 = prop00

    def getProp0(self):
        return self.__prop0

    def getProp00(self):
        return self.__prop00

class A(B):
    def __init__(self, prop5, prop6, prop0, prop00, prop1, prop2):
        super().__init__(prop5, prop6, prop0, prop00)
        self.__prop1 = prop1
        self.__prop2 = prop2

    def getProp1(self):
        return self.__prop1

    def getProp2(self):
        return self.__prop2

class C(B):
    def __init__(self, prop5, prop6, prop0, prop00, prop3, prop4):
        super().__init__(prop5, prop6, prop0, prop00)
        self.__prop3 = prop3
        self.__prop4 = prop4

    def getProp3(self):
        return self.__prop3

    def getProp4(self):
        return self.__prop4