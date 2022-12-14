# PRIME PALINDROME
# lower = int( input('Enter the lower range: ') )
# upper = int( input('Enter the upper range: ') )

# while True:
#     for num in range(lower, upper+1):
#         count = 0
#         reversed = 0
#         temp = num
#         # checking if the number is prime or not
#         for i in range(1, temp+1):
#             if num%i == 0:
#                 count += 1

#         # if the number is prime
#         if count == 2:
#             # reverse the number
#             while temp > 0:
#                 reversed = reversed * 10 + (temp % 10)
#                 temp = temp // 10
#             # check for palindrome
#             if reversed == num:
#                 print(num, end=" ")

# print("\n")


# FUNCTIONS -> reusability of the code -> returns a value
# def function_name(parameters):
# def add(a, b):
#     return int(a) + int(b)

# # Q - Fumd the square of the addition of two numbers
# answer1 = add('100', True)
# print(answer1 * answer1)


# RECAP -> Functions, Loops - for, range(), while


# BITWISE OPERATORS

# 1. Bitwise AND
# 2. Bitwise OR
# 3. BItwise NOT
# 4. Bitwise XOR

# AND GATE -> both the conditions should always be True (a=1, b=1, o/p=1)
# a     b   o/p
# 0     0   0  
# 0     1   0
# 1     0   0
# 1     1   1

# Bitwise AND
# val1 = 4
# val2 = 7
# print('The Bitwise AND of', val1, 'and', val2, 'is: ',  val1 & val2)

# binary(val1) -> 0 1 0 0
#                   AND
# binary(val2) -> 0 1 1 1
# Bitwise AND ->  0 1 0 0 -> decimal(o/p) -> 4
#       8     4    2   1
# 1 ->  0     0    0   1
# 2 ->  0     0    1   0
# 3 ->  0     0    1   1
 
# OR GATE -> Either of the condition should be True
# a     b   o/p
# 0     0   0  
# 0     1   1
# 1     0   1
# 1     1   1

# Bitwise OR
# val3 = 15
# val4 = 12
# print('The Bitwise OR of', val3, 'and', val4, 'is: ', val3 | val4)

# binary(val3) -> 1 1 1 1
# binary(val4) -> 1 1 0 0
#                   OR
# O/P          -> 1  1  1  1 -> decimal -> 15

# NOT GATE -> Opposite of the input
# a     o/p
# 0     1 
# 1     0

# Bitwise NOT
# val5 = 9
# print('The Bitwise NOT of', val5, 'is', ~val5)
# binary(val5) -> 1 0 0 1
#                   NOT         -> - (binary + 1)
#                 (1 0 0 1)
#                        1
#                  1 0 1 0      -> decimal -10

# XOR Gate -> If either of the conditions is True, then output will also be True
# a     b   o/p
# 0     0   0  
# 0     1   1
# 1     0   1
# 1     1   0

# Bitwise XOR
# val6 = 14
# val7 = 13
# print('The Bitwise XOR of', val6, 'and', val7, 'is:', val6 ^ val7)

# binary(val6) -> 1 1 1 0
# binary(val7) -> 1 1 0 1
#                   XOR
#                  0 0 1 1      -> decimal -> 3 


# 16 8 4 2 1
#  1 1 0 0 0 -> 24
#  1 1 0 0 1 -> 25

# num = 5.0056789
# print("The number is - ", num)
# print("Number is %2d" %(num))       # 2d -> Integer
# import datetime

# name = 'Python'
# progg = 'Programming'

# print(name, "is a beautiful", progg, "language")
# print(f"{name} is a beautiful {progg} language")

# today = datetime.datetime.today()
# print(today)

# myStr = "This is {} and I am {} years old".format("Arun Kudiyal", 25)
# print(myStr)

# myStr = "I am {:>10} years old".format(20)
# myStr = "I am {:<10} years old".format(20)
# print(myStr)


# Breaks in Python
# myList = [2, 7, 19, 12, -5, -8, 13, 9 , 15]
# for val in myList:
#     if(val >= 0):
#         print(val, end=" ")
#     else:
#         break

# Q -> Count the number of alphabets in a name util you find a vowel
# name = input("Enter a name - ")
# vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
# counter = 0
# for alphabet in name:
#     if(alphabet not in vowels):
#         counter += 1
#     else:
#         break

# print('No of alphabets before vowels are - ', counter)


# datetime
# import datetime

# date = datetime.datetime.now()

# print("Today is", date.strftime("%d"), date.strftime("%B"), datetime.datetime.now().year )

# print("Today is", date.strftime("%a"), date.strftime("%d"), date.strftime("%b"), datetime.datetime.now().year )

# ARMSTRONG NUMBERS 
# number -> abcde
# digits = 5
# a^5 + b^5 + c^5 + d^5 + e^5 = numbers

# number = 1634
# digits = 4
# 1^4 + 6^4 + 3^4 + 4^4 = number
# 1 +  1294 + 81 + 256 = 1634

# print( range(100) ) # Always starts from number 0, but the end is exclusive
# for variable in range(10):
#     print(variable)

# Q -> Print the table of the given number
# number = int(input('Enter a number - '))
# for table_number in range(number, (number*10) + 1, number):
#     print(table_number) 

# Q -> you are given a range, print all the prime numbers in the given range
# lower_range = int(input("Enter the lower range - "))
# upper_range = int(input("Enter the upper range - "))
# prime_numbers = set()
# # number = 1 - 9
# # number = 1, 2, , 4, 5, 6, 7, 8, 9
# for number in range(lower_range, upper_range):
#     if(number > 1):
#         # variable = 2 - 3
#         # variable = 2 
#         for variable in range(2, number):
#             # print(variable, end="--")
#             if(number % variable == 0):
#                 break
#         else:
#             prime_numbers.add(number)

# for var in prime_numbers:
#     print(var, end=" ")
# print("\n")


# for Loop
# PATTERN PRINTING

# Q -> Write a python code to print the following pattern based on a given input 'n'
# n = 3
# *
# * *
# * * *

# n = 4
# *
# * *
# * * *
# * * * *

# n = 5
# *
# * *
# * * *
# * * * *
# * * * * *

# # Step 1 -> finding the no of rows and no of cols
# n = int(input('Enter the value of n - '))
# # Step 2 -> Identify the steps of rows in the pattern
# # row -> 1, 2, 3
# for row in range(1, n+1):
#     # Step 3 -> Idnetify the steps of cols in the pattern
#     # col -> 1, 2, 3
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print("\n")


# Q -> Write a python code to print the following pattern based on a given input 'n'
# n = 5
# * * * * *
# * * * *
# * * *
# * *
# *

# Step 1 - n(rows) = n; n(cols) = n
# n = int(input("Enter the input  n - "))
# for row in range(1, n+1):
#     for col in range(row, n+1):
#         print("*", end=" ")
#     print("\n")


# Q -> Write a python code to print the following pattern based on a given input 'n'
# n = 5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n(Rows) = 5, n(Cols) = 5
# N(spaces) -> row = 0; spaces = 4; stars = 1
# N(spaces) -> row = 1; spaces = 3; stars = 2
# N(spaces) -> row = 2; spaces = 2; stars = 3
# N(spaces) -> row = 3; spaces = 1; stars = 4
# N(spaces) -> row = 4; spaces = 0; stars = 5
# n = int(input('Enter the value of n - '))
# # number of spaces
# space = n - 1
# # n = 5; row = 0, 1, 2, 3, 4
# # 0, space = 4 -> 3
# # 1, space = 3 -> 2
# # 2, space = 2 -> 1
# # 3, space = 1 -> 0
# # 4, space = 0 -> -1

# for row in range(0, n):
#     # SPACE
#     for variable in range(0, space):
#         print(end=" ")
#     space = space - 1

#     # STARS
#     for col in range(0, row+1):
#         print("* ", end="")
#     print("\r")

# for i in range(0, 1):
#     print(i)


# Q -> Write a python code to print the following pattern based on a given input 'n'
# n = 5
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# Q -> Write a python code to print the following pattern based on a given input 'n'
# n = 5
#     1
#    2 3
#   4 5 6
#  7 8 9 10
# 11 12 13 14 15


# FUNCTIONS IN PYTHON ->
# A block of code to create and re-use any given logic

# def functionName(arguments):
# def functionName(parameters):

#   Function Body

# Q -> You are given with 2 numbers, add two numbers and print the sum - 
# def calculateSum(num1, num2):
#     sum = num1 + num2
#     print('The sum of', num1, 'and', num2, "is ", sum)

# return statemnents
# def calculateSum(num1, num2):
#     sum = num1 + num2
#     return sum

# # Calling the function
# # calculateSum(10, 60)
# # calculateSum(20, 50)
# # calculateSum(30, 40)

# # Q -> you are given with two numbers, sum the nos and square the result
# n1 = int(input('Enter a number - '))
# n2 = int(input('Enter a number - '))

# result = calculateSum(n1, n2)
# print('Square of', result, 'is', result * result)

# Return Types
# def funcName(para1: type1, para2: type2, ... ) -> returnType:
# def calculateSum(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# ans1 = calculateSum(10, 20)
# ans2 = calculateSum(101, 202)
# ans3 = calculateSum(True, 'Hello')

# print(ans1, ans2, ans3)

# Q -> Create a function which takes a number and it returns true if its even and false if odd
# def isEven(number: int) -> bool:
#     if(number % 2 == 0):
#         return True
#     else:
#         return False

# ans1 = isEven(4)
# if(ans1 == True):
#     print('Hey, its even!')
# else:
#     print('Hey, its odd!')

# ans2 = isEven(5)
# if(ans2 == True):
#     print('Hey, its even!')
# else:
#     print('Hey, its odd!')

# Default Arguments / Default Parametres
# def sayMyName(firstName: str = "Demo", lastName: str = "Text") -> str:
#     fullName = f"{firstName} {lastName}"
#     return fullName

# name1 = sayMyName("Python", "Programming")
# name2 = sayMyName()
# name3 = sayMyName("Hello")

# print(name1)
# print(name2)
# print(name3)

# KEYBOARD ARGUMENTS
# Variable Length Argument
# def someFunction(*args):
#     for val in args:
#         print(val)
# someFunction("Hello", "I", "am", "Python")
# someFunction("Hello", "I", "am", "Python", "this", "is", "an")
# someFunction("Hello", "I", "am", "Python", "this", "is", "an", "example")

# DOC-STRING in Python
# def calculateSquare(num: int) -> int:
#     ''' This is an utility function which returns the sqaure of the given number '''
#     return num * num

# print(calculateSquare.__doc__)

# Q:- WHAT IS THE DIFFENCE BETWEEN FUNCTIONS & ANYONOUMS FUNCTIONS
# def getSquare(num: int) -> int : return num * num
# # if i have a function whose definiation can be consluded in one line, you can make that function anoynomous
# getCube = lambda num2 : num2 * num2 * num2

# n1 = int(input('enter a value : '))
# n2 = int(input('enter a value : '))
# findSum = lambda n1, n2: n1 + n2
# print(findSum(10, 20))

# print(getSquare(5))
# print(getCube(7))


# Differnce b/w actual parameters and refence parameters
# def changeList(myList: list) -> list:
#     myList.append("/0")
#     return myList

# sampleList = [100, 150, 200, 250, 300]
# # MemLoc(sampleList) = #Ab0DCF
# print(sampleList)

# updatedList = changeList(sampleList)
# # changeLIst([])
# # changeList(#Ab0DCF)
# print(updatedList)

# print(sampleList)


# RECURSION -> 
# A process where you call the same function in the body for the repeated process of calculation

# Q :- given a number, find the sum of all the n natural numbers
# n * (n + 1) / 2
# n = 5 --> 5 + 4 + 3 + 2 + 1 = 15
# n = 5 --> 5 + sum(...4)
#       --> 5 + 4 + sum(...3)
#       ---> 5 + 4 + 3 + sum(...2)

# def sumOfNatNums(num):
#     # BASE CONDITION
#     if(num == 1):
#         return 1
#     return num + sumOfNatNums(num - 1)

# n = 5
# sum(5)
# 1st Itr --> sum(5) --> 5 + 10 --> 15
# 2nd Itr --> sum(4) --> 4 + 6 --> 10
# 3rd Itr --> sum(3) --> 3 + 3 --> 6
# 4th Itr --> sum(2) --> 2 + sum(1) --> 2 + 1 --> 3
# .
# .
# .
# -ve Infinte

# ans1 = sumOfNatNums(5)
# print(ans1)


# Q :- WAP to get the factorial of a given number
# def factorial(num):
#     # Base Condition
#     if(num == 0):
#         return 1
#     return num * factorial(num - 1)

# fact1 = factorial(6)
# print(fact1)


# Q :- To print a Fibonacci series upto n terms 
# fib(2) -> 0 1
# fib(5) -> 0 1 1 2 3
# fib(10) -> 0 1 1 2 3 5 8 13 21 34

# fib(1) = 0
# fib(2) = 1 
# fib(3) = 1
# fib(4) = 2
# fib(10) = 34
# .
# .
# fib(n) = fib(n-1) + fib(n-2)

# Giving each fib number at a given term -> o/p
# def fib_series(term):
#     # Base Condition
#     if(term == 1):
#         return 0
#     elif(term == 2):
#         return 1
#     else:
#         # check if the value exist in the dict or not
#         # if(value exist in the dic)
#         return( fib_series(term-1) + fib_series(term-2) )

# # Printing the whole series
# n = int(input('enter a number - '))
# if n <= 0:
#     print('enter a non-zero, +ve number')
# else:
#     for value in range(1, n+1):
#         print(fib_series(value), end=" ")
#     print("\n")


# EXPLAINATION
# n = 6
# value = 1, 2, 3, 4, 5, 6 | value = 5
# dict = { 1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5 }
# O/P -> 0 1 1 2 3

# value = 1
# fib(1) -> 0

# value = 2
# fib(2) -> 1

# value = 3
# fib(3) -> fib(2) + fib(1) -> 1 + 0 -> 1

# value = 4
# fib(4) -> fib(3) + fib(2) -> fib(2) + fib(1) + fib(2) -> 1 + 0 + 1 -> 2

# value = 5
# fib(5) -> fib(4) + fib(3) -> fib(3) + fib(2) + fib(3) -> fib(2) + fib(1) + fib(2) + fib(3) -> 1 + 0 + 1 + fib(3) -> 1 + 0 + 1 + fib(2) + fib(1) -> 1 + 0 + 1 + 1 + 0 -> 3

# Strong numbers
# 145 = 1! + 4! + 5! = n -> STRONG

# function finds the factorial of a given number -
# def fact(n) -> int:
#     # Recursion -> ?
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# # function to find a string number -
# def is_strong_number(n) -> bool:
#     # convert the number into a string
#     num = str(n)
#     # temp variable to store the sum
#     sum = 0

#     for i in range(len(num)):
#         sum += fact( int(num[i]) )
    
#     if sum == n:
#         return True
#     else:
#         return False

# # Main Code
# n = int(input('enter any +ve number - '))
# if n <= 0:
#     print('Enter a non-zero, positive number')
# else:
#     for i in range(1, n+1):
#         if is_strong_number(i):
#             print(i, end=" ")
#     print('\n')


# MATH MODULE 

# import math

# Q:- Find out the area of the circle
# PI = 3.14

# MATH CONSTANTS

# newPI = math.pi
# radius = int(input('enter a +ve radius - '))
# print( PI * radius * radius )
# print( newPI * radius * radius )

# print( math.tau )
# print(math.e)
# print(math.inf)
# print(-math.inf)

# MATH METHODS

# 1. isInf()
# math.isinf(0 / 0)

# 2. ceil() , floor()
# n = 2.5
# print( math.ceil(n) )
# print( math.floor(n) )

# 3. factorial(n)
# n = 5   # 120
# print( math.factorial(n) )

# 4. gcd()
# n1 = 16
# n2 = 8
# print( math.gcd(n1, n2) )

# Absolute values -> fabs() -> float
# num = -10
# print(math.fabs(num))

# # Logarithmc Functions -> e^x | e^y
# x = 10
# print('e^x is - ', math.e**x)

# a = 10  # log10 # loge
# print(math.log(a))
# print(math.log2(a))
# print(math.log10(a))

# Square Roots
# n = 25  # float
# print( math.sqrt(n) )

# Trignomeritic Expression
# a = 25
# print( math.sin(a) )


# TOWER OF HANOI - TOH

# n(Towers) = 3 | A, B, C
# n(Disc) = n

# Objective - Take n discs from A and place them in C with the help of an aux rod called B

# Constraints -
# 1. Move one disc at a time
# 2. Move -> Take the topmost disc, and place it either on a empty rod or an another stack
# 3. No disc will be placed above a disc which is smaller than it.

# Explaination :-

# n = 1 | D1
# D1 -> A --> C
# Total of Step = n = 1; steps = 1

# n = 2 | D1 & D2 - D1 -> Smaller; D2 -> Larger
# D1 -> A --> B
# [C -> empty, A -> largest, stack was created in B]
# D2 -> A --> C
# D1 -> B --> C
# Total of Step = n = 2; steps = 3

# n = 3
# D1 -> A --> C
# D2 -> A --> B
# D1 -> C --> B
# [C -> empty, A -> largest, stack was created in B]
# D3 -> A --> C
# [ n(A) = 0, n(B) = 2, n(C) = 1 ]
# D1 -> B --> A
# [ A --> Smallest, B --> Second Largest, C --> Largest Disc ]
# D2 --> B --> C
# D1 --> A --> C
# Total of Step = n = 3; steps = 7

# n = 4; steps = 15

# [ Formula -> n; steps -> 2^n - 1 ]

def tower_of_hanoi(n, start_rod, aux_rod, end_rod):
    # BASE CASE :-
    if n == 1:
        print('Move disc 1 from {} to {}'.format(start_rod, end_rod))
        return

    # Plan A:-
    # Find the largest disc, and place it from A to C
    # --> C is will be empty
    # --> A will have the largest disc
    # --> Intermediate stack will be in B
    tower_of_hanoi(n-1, start_rod, end_rod, aux_rod)
    print('Move disc {} from {} to {}'.format(n, start_rod, end_rod))

    # Plan - B:-
    # --> Intermediate Stack at B -> C --> A is empty -> B -> C by using A as an aux
    tower_of_hanoi(n-1, aux_rod, start_rod, end_rod)

n = int( input('enter any positive number - ') )
if n <= 0:
    print('enter only +ve non-zeo number!')
else:
    tower_of_hanoi(n, 'A', 'B', 'C')

# ASSIGNMENT ->
# 1. Analysing the recursive calls
# 2. Iterative solution alternative for the recursive code.