# # Add 2 numbers

# # Varibales - Namaspace for a data
# # 
# var_one = "Arun Kudiyal"
# # print( type(var_one) )

# # Data Types
# # 1. int
# var_zero = 100
# var_one = 10 + (2 * 3) + (4 / 8)    # BODMAS
# print("Variable One is -", var_one)
# print("Type of the Variable One is -", type(var_one))

# # float
# # division always give results as float
# var_five = 100 / 10
# print("Variable Five is -", var_five)
# print("Type of the Variable Five is -", type(var_five))

# # floor-division always give results as int
# var_six = 100 // 9
# print("Variable six is -", var_six)
# print("Type of the Variable six is -", type(var_six))

# # string
# var_two = "String"
# print("Variable Two is -", var_two)
# print("Type of the Variable Two is -", type(var_two))

# # boolean
# var_three = False
# print("Variable Three is -", var_three)
# print("Type of the Variable Three is -", type(var_three))

# #complex
# var_four = -10 + 10j
# print("Variable Four is -", var_four)
# print("Type of the Variable Four is -", type(var_four))


# STRINGS

# my_string = 'This is String One'
# my_string_two = "This is String Two"

# print(my_string + my_string_two)    # String Concatenation

# print(my_string + "\n" + my_string_two)

# specialString = "Hello\nWorld"
# print(specialString)

# word = "I won't\n"
# print( 5 * word )

# print('Hello' 'How are you?') # String Concatenation --> NOT WITH VARIABLES, ONLY LITERALS

# print( word[17] )
# print( word[-1] )

# print( word[-18] )
# print( len(word) )


# STRING SLICING --> [ : ]

# word = "python programming"
# word[start:end] --> start(included); end(excluded)
# print( word[1:10] )

# print( word[:12] )  # String will strt from 0
# print( word[5:] )  # String will end to the length

# print( word[-1:] )  # g
# print( word[:-3] )  # python programm

# newWord = word[:2] + word[5:15] # pyn programm
# print(newWord)


# STRING METHODS

# word = "python programming is cool"
# nameOfTheMethod(  )
# lengthOfString = len(word) 
# print(lengthOfString)

# 1. Upper Case
# uppeRString = word.upper()
# print(uppeRString)

# 2. Lower Case
# lowerString = uppeRString.lower()
# print(lowerString)

# 3. Capitilize Case
# capilizeString = word.capitalize()
# print(capilizeString) 

# 4. Title Case
# titleString = word.title()
# print(titleString) 


# LISTS - 
# 1. Data Structure which helps you contain multiple values inside a single varibale
# 2. Lists contain data inside it but in each elemnt comma seperated

# Lists = [ elt1, elt2, elt3, .... ]

# 1. Create a list using [ ... ]
# alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
# print(alphabets)
# print(type(alphabets))

# # 2. Create a list by using list( ) constructor
# # list() -> An empty list
# # list(number) -> Error
# # list(num1, num2, num3) -> Error
# # list("stringValue") --> Break each alphabet contained in the string
# myPython = list("PYTHON")
# print(myPython)           # [ 'P', 'Y', 'T', 'H', 'O', 'N' ]
# print(len(myPython))
# # numbers = list("Python Programming")
# # print(numbers)
# # print(type(numbers))

# # Note -> you can contain multiple diff data types in one single list
# values = [ 100, "String", True, 3+2j ]
# print(values)
# print(type(values))

# # List is managed by an indices
# print( alphabets[3] )   # d
# print( alphabets[-5] )  # c


# Slicing in Lists - Access a particular part of the list

# alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
# print( alphabets[1:4] ) # ['b', 'c', 'd'] -> return a list
# # print( alphabets[1] )
# # print( alphabets[2] )
# # print( alphabets[3] )

# # print(alphabets[-1: -4])    # Returns empty list -> [  ] --> Alawys work in the forward direction
# # print(alphabets[-4: -1])
# # print(alphabets[0:10000])   # If end is a large number, returns the whole list
# # print(alphabets[0:])        # Returns a list containing all the values

# numbers = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# # print(numbers[1])   # [4, 5, 6]
# # print(numbers[1][1])   # 5
# # print(numbers[2][2])   # 9

# Manipulating Lists
# # Replacement Mechanism in Lists

# # alphabets[1] = ['x', 'y', 'z']
# # print(alphabets)

# alphabets[1:4] = ['x', 'y', 'z']
# numbers[1][0] = 'x'
# print(numbers)

# alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]

# print(alphabets)

# # Removing a certain part of the list
# alphabets[4:] = []
# print(alphabets)


# BUILT-IN METHOD FOR LISTS

# alphabets = [ 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
# # 0. find the length of the list - len()
# print( len(alphabets) )

# # 1. add an element at the end of the list - append()
# alphabets.append('z')
# print(alphabets)

# # 2. add an element at a specified index - insert()
# alphabets.insert(-1, 'x')
# print(alphabets)

# alphabets.insert(2, 'C')
# print(alphabets)

# 3. Add a collection of values at the end of the list
# alphabets.extend(['w', 'x', 'y', 'z'])
# print(alphabets)

# # Removing a certain part of the list
# alphabets[4:] = []
# print(alphabets)

# 4. Remove an element from the end of the list - pop()
# pop() -> Remove the end indexed value
# pop(index) -> Remove the element from the specified index
# alphabets.pop(-1)
# print(alphabets)

# 5. Remove an element but you don't know the index -> first occurance
# alphabets.remove('a')
# print(alphabets)

# 6. Reverse the list - reverse()
# print(alphabets)
# alphabets.reverse()
# print(alphabets)