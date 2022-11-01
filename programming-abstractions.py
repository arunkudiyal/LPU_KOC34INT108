# PROGRAMMING ABSTRACTIONS

# 1. Conditional Stataments

# Logical Gates - AND, OR, NOT

# AND - 
# F F     F
# T F     F
# F T     F
# T T     T
# if( 8 < 10  and 10 > 15 ):
#     print('Yes! 8 is less than 10')
# else:
#     print('Else part!')

# # OR - 
# # F F     F
# # T F     T
# # F T     T
# # T T     T
# if( 8 < 10  or 10 > 15 ):
#     print('Yes! 8 is less than 10')
# else:
#     print('Else part!')

# # NOT - 
# # F     T
# # T     F
# myValue = False
# notMyValue = not(myValue)
# print(myValue, notMyValue)


# Assignment Question - 
# Problem Statemnet -   gender = 'M' and age > 21 --> Then He can Vote
#                       gender = 'F' and age > 18 --> Then She Can Vote 
#                       gender = 'M'/ 'F' > 18 --> Then He/She cannot vote

# gender = 'A'
# age = 30
# # Nested Conditional Statements
# if age < 0:
#     print('enter the correct values of age!')
# elif gender == 'M':
#     # Expression - 1
#     if age > 21:
#         print('He can Vote!')
#     else:
#         print('He cannot Vote!')
# elif gender == 'F':
#     # Expression 2
#     if age > 18:
#         print('She can Vote!')
#     else:
#         print('She cannot Vote!')
# else:
#     print('enter the correct values of gender')


# Using Logical Gates

# gender = 'M'
# age = 22
# if age < 0:
#     print('Enter the correct value for the age')
# elif gender == 'M' and age > 21:
#     print('He can Vote!')
# elif gender == 'M' and age < 18:
#     print('He cannot Vote')
# elif gender == 'F' and age > 18:
#     print('She can Vote')
# elif gender == 'F' and age < 18:
#     print('She cannot Vote')
# else:
#     print('Enter correct values of the gender')


# range() Function
# print(range(10))

# Loops --> Do an operation serveral number of times as a repitition
# 1. for loop
# for variableName in range(noOfTimesYouWantToPerformOperations)
# for count in range(1, 16, 2):
#     print('LPU', count)

# for count in range(16, -1, -2):
#     print('LPU', count)

# Q- Print all the odd numbers from 1 to 100
# Q- Print all the even numbers from 1 to 100

# fruits = ['Apple', 'Orange', 'Banana', 'Pears', 'Grapes']
# for fruit in fruits:
#     print(fruit, end="\n")
#     # print(fruit, end=", ")


# 2 - while Loop
# you donot know where the ends

# Infinite while loop
# while True:

# myList = [10, 20, 0, 30, 40, 50, 60]
# print('Start of the Loop')
# index = 0
# # while(condition):
# while myList[index] != 0:
#     print(myList[index])
#     index = index + 1
# print('End of the Loop')


# Question - You are given with a number, you need to print the reverse of the number
# Eg --> 12349298 ; O/P - 89294321

# number = 12349298

# Q - Find the cube of a user input number
# input() -> Takes the input in Strings

# dataType(input()) --> TYPECASTING --> Cast / Convert one DT into another DT
# number = int(input("Enter any number - "))
# print(number + 2)

# WAP to reverse the number
# num = 12345         # num / 10 --> Rem - 4
# num = int(input('Enter a number value - '))
# num_rev = 0

# # Step 4 - Do the following in a loop, till the number doesn't become 0
# while num > 0:
#     # Step 1 - Take the last digit from the number
#     last_digit = num % 10                         # last_digit = 5 -> 4 --> 3 --> 2 --> 1
#     # Step 2 - Add that digit in the reverse_number
#     num_rev = (num_rev * 10) + last_digit         # num_rev = 5 --> 54 --> 543 --> 5432 --> 54321
#     # Step 3 - Remove the digit from the number
#     num = num // 10                               # num = 1234 --> 123 --> 12 --> 1 --> 0

# print('Reversed number is - ', num_rev)


# Q: -> Given a no, count the number of digits in the number
# number = int(input('Enter any number - '))
# count = 0
# num = number
# while(number > 0):
#     digit = number % 10
#     count = count + 1
#     number = number // 10

# print('Number of digits in', num, 'is', count)

# Data Structires with Problem Solving
# TUPLES - ( )
# 1. Order is important
# 2. Tuples are immutable
# 3. Tuples elemets are indexed

myTuple = ("Apple", "Banana", "Pear", "Watermelon")
myList = [10, 20, 'Hello', True, (2+3j)]

# print(myTuple)
# print(type(myTuple))
# print(len(myTuple))

# print(myTuple[0])

# for values in myTuple:
#     print(values) 

# for val in myList:
#     print(val)


# TUPLE CONCATENATION
# myTuple1 = (10, 20, 30, 40, 50)
# myTuple2 = ('Sam', 'John', 'Anna', 'Tom', 'Hugh')
# myTuple3 = myTuple1 + myTuple2                    # (10, 20, 30,.. , 50, 'Sam', ... 'Hugh')

# print(myTuple3)


# NESTED TUPLES
# myTuple1 = (10, 20, 30, 40, 50)
# myTuple2 = ('Sam', 'John', 'Anna', 'Tom', 'Hugh')
# myTuple3 = ( myTuple1, myTuple2 )
# print(myTuple3)               # ( (10, 20, 30, 40, 50),('Sam', 'John', 'Anna', 'Tom', 'Hugh') )

# DONOT DO THIS --> myTuple1[0] = 100 --> Re-assignment is not allowed

# myTuple = ( "My Tuple", )
# print( type(myTuple) )

# Repetive Tuples
# pythonTuple = ('Python',) * 5
# print(pythonTuple)
# del pythonTuple
# print(pythonTuple)


# Convert a list into a Tuple
# myList = [ 'Apple', 101, True, (2+3j) ]
# print(myList)
# print(type(myList))

# myListToTuple = tuple(myList)
# print(myListToTuple)
# print(type(myListToTuple))

# Convert a tuple into List
# myTuple2 = ('Sam', 'John', 'Anna', 'Tom', 'Hugh')
# print(myTuple2)
# print(type(myTuple2))

# myList2 = list(myTuple2)
# print(myList2)
# print(type(myList2))


# SETS --> { ... }
# 1. Sets do not follow ordering
# 2. Sets elements cannot be accessed using index
# 3. Sets are immutable
# 4. Duplicate values are not supported in Sets

# mySet = { "Apple", "Banana", "Pear", "Peach" }
# print(mySet)
# print(type(mySet))

# print(mySet[1]) --> DONOT DO THIS

# mySet = { "Apple", "Banana", "Pear", "Pear", "Peach", "Banana" }
# print(mySet)

# II -> using set constuctor
# mySet2 = set( (100, "Hello", True, (2+5j), 200) )
# print(mySet2)

# setToList = list(mySet2)
# print(setToList)

# setToTuple = tuple(mySet2)
# print(setToTuple)


# SET METHODS
# numbers = {100, 67, 98, 47, 32, 49, 89, 2000}
# print(numbers)

# # 1. add elt to set
# numbers.add(1001)
# print(numbers)

# # 2. remove elt from the set
# numbers.remove(89)
# print(numbers)

# # 3. discard an elt from the set
# numbers.discard(100)
# print(numbers)

# # 4. pop an elt from the set --> random value from the set
# numbers.pop()
# print(numbers)

# # 5. clear the whole set at once
# # numbers.clear()
# # print(numbers)

# # 6. sorted() --> 
# print( sorted(numbers) )

# set1 = {100, 200, 300}
# set2 = {"Arun", "Python"}
# print( set1 + set2 )


# DICTIONARY --> key: value
# 1. DS which contains value in the form of "key": value
#2. Duplicates are not allowed, values will be overwritten


# myDict = { "username": "User Name", "age": 21, "isAdult": True, "occupation": "Student" }
# print(myDict)

# myDict = { "username": "User Name", "age": 18, "age": 21, "isAdult": True, "occupation": "Student" }
# print(myDict)


person = { 
    "name": "Person - 1", 
    "age": 45,
    "address": {"street": 21, "city": "Chandigarh"}, 
    "hobbies": ["dancing", "painting", "gaming"], 
    "marks": {98, 76, 58, 55, 91}  
}
# print(type(person))

# Acccess values from a dictonary
# print("The address of the person is - ", person["address"])
# print("The last hobby of the person is - ", person.get("hobbies")[-1])
# print("The address of the person is", person.get("address").get("city"))

# print(person)

# # Q- Add a new marks to mraks key
# print(type(person.get("marks")))
# myMarks = list(person.get("marks"))
# myMarks.append(100)
# myMarksSet = set(myMarks)
# person.update({"marks": myMarksSet})

# print(person)

# METHODS IN DICT - 
# 1. get() -> Gives the value of the specified item
# 2. update() -> Updates the specifies values in the item

# 3. items()
# print(person.items())
# print(type(person.items()))

# 4. keys()
# print(person.keys())
# print(type(person.keys()))

# myFruits = ["Apple", "Pear", "Guava", "Peach"]
# if "Watermelon" in myFruits:
#     print("Watermelon is a fruit in List")
# else:
#     print("Watermelon is not a fruit in List")

# Q -> If in the dict, you have a age then display the age else add a new age of 50

# if "age" in person:
#     print('Yes, age is a key of the dict & the age is', person.get("age"))
#     # Remove a value / key from the dict.
#     person.pop("age")
#     print(person)
# else:
#     print('No, age is a not key of the dict')
#     age = int(input('Enter the age to insert in the dictonary - '))
#     # person.setdefault("age")
#     # person.update( {"age": age} )

#     # Add a new key with a default item
#     person.setdefault("age", age)
#     print(person)