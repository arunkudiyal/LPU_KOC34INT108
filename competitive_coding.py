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