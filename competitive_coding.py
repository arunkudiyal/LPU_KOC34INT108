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
val1 = 4
val2 = 7
print('The Bitwise AND of', val1, 'and', val2, 'is: ',  val1 & val2)

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
val3 = 15
val4 = 12
print('The Bitwise OR of', val3, 'and', val4, 'is: ', val3 | val4)

# binary(val3) -> 1 1 1 1
# binary(val4) -> 1 1 0 0
#                   OR
# O/P          -> 1  1  1  1 -> decimal -> 15

# NOT GATE -> Opposite of the input
# a     o/p
# 0     1 
# 1     0

# Bitwise NOT
val5 = 9
print('The Bitwise NOT of', val5, 'is', ~val5)
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
val6 = 14
val7 = 13
print('The Bitwise XOR of', val6, 'and', val7, 'is:', val6 ^ val7)

# binary(val6) -> 1 1 1 0
# binary(val7) -> 1 1 0 1
#                   XOR
#                  0 0 1 1      -> decimal -> 3 