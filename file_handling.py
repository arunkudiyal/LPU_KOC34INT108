# open()

# open --> A method that opens the file & takes the path and the mode as paramter.
# open methods returns a stream. A stream which consist of the refernce, and details related to the file (name='./demo.txt' mode='r' encoding='UTF-8')

# mode ==> 'r'
# fileRef = open('C:\Program_Files\myFile.txt', 'r', 'charset')
# fileRef = open('./demo.txt', 'r')
# print( fileRef )

# for word in fileRef:
#     print(word)

# read() --> Reads the entire content of the file and you can print the content
# print( fileRef.read() )
# read(size) --> size is the number of character --> read(10) -> Hello, my n
# print( fileRef.read(5) )


# mode ==> 'w' --> It will write the data provided using the write() method. But re-execution will not add more lines to the file, until any change occurs.
# fileRef = open('./demo2.txt', 'w')
# fileRef.write('Hey, this is a Demo text.')
# fileRef.write('This demo text is for demo2.txt.')
# fileRef.write('This is a change!')
# # close() --> close de-allocated resoirces/ memory allocated to the fileRef
# fileRef.close()

# fileRef = open('./demo2.txt', 'r')
# print( fileRef.read() )

# mode ==> 'a' --> It will write the data provided using the write() method. But re-execution will add more lines to the file.
# fileRef = open('./demo2.txt', 'a')
# fileRef.write('This is something new')
# fileRef.close()
# fileRef = open('./demo2.txt', 'r')
# print( fileRef.read() )

# Q :- You are given with a file containing names of the animal `, ` seperated. Print each name of the animal
# Syntax --> with open('path', 'mode') as fileRef:

# with open('./demo2.txt', 'r') as f:
#     # readline() --> reads the entire line and returns a string back
#     # type(myData) --> 
#     myData = f.readline()
#     print(myData)
#     # split returns a list
#     animals = myData.split(', ')
#     print(animals)
#     for word in animals:
#         print(word)

# READ MODE

# fileRef = open('./demo.txt', 'r')
# # print( fileRef.read() )

# # myFileData = fileRef.readline()
# myFileData = fileRef.read()
# print(type(myFileData))


# WRITE MODE
# charList = [ 'This is Line - 1\n', 'This is Line - 2\n', 'This is Line - 3\n' ]

# f = open('./demo2.txt', 'w')
# # f.write('This is Line - 1.')
# # f.write('\nThis is Line - 2.')

# f.writelines(charList)


# APPEND MODE 
# charList = [ 'This is Line - 1\n', 'This is Line - 2\n', 'This is Line - 3\n' ]
# f = open('./demo2.txt', 'a')
# f.writelines(charList)


# SYNTAX --> with open('location', 'mode') as f1

# with open('./demo.txt', 'r') as f1:
#     print(f1.read())

# with open('./demo.txt', 'r') as f1, open('./demo2.txt', 'r') as f2:
#     print('CONTENT OF FILE - 1 is - ')
#     print(f1.read())
#     print('\n')
#     print('CONTENT OF FILE - 2 is - ')
#     print(f2.read())


# with open('./demo2.txt', 'r') as f1:
#     myFileText = f1.readline()
#     listOfAnimals = myFileText.split(', ')
#     for animal in listOfAnimals:
#         print(animal)


# Q:- You are given with two text files (demo.txt & demo2.txt), you need to copy all the content from demo.txt to demo2.txt
with open('./demo.txt', 'r') as file1, open('./demo2.txt', 'w') as file2:
    contentOfFileOne = file1.read()
    file2.write(contentOfFileOne)


# SAMPLE QUESTIONS ON FILE HANDLING IN PYTHON