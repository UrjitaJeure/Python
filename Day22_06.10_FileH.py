# img
# binary
# text

#w
#r
#a
#w+
#r+
#a+


# f.seek(10,0)  # at the beginning
# f.seek(10,1)
# f.seek(-10,2)

#program  5

# f = open('myfile3.txt','a+')
# print('Enter the "@" to end the file')
#
# while str != '@':
#     str = input()
#     if(str != '@'):
#         f.write(str + '\n')
#
# f.seek(0,0)
#
# print('The file contents are :')
# print(f.read())
#
# f.close()
#
import os, sys

# str = input('Enter the filename:')
# if os.path.isfile(str):
#     f = open(str,'r')
#     print('The contents of the file are :')
#     print(f.read())
#     f.close()
# else:
#     print(str + " does not exist")
#     sys.exit()

# print('The contents of the file are :')
# print(f.read())


str = input('Enter the filename:')
if os.path.isfile(str):
    f = open(str,'r')
    print('The contents of the file are :')
    #print(f.read())
    cc = cw = cl = 0
    for line in f:
        #print(line)
        cl = cl +1
        cw = cw + len(line.split())
    f.seek(0,0)
    cc = len(f.read())

    print(cl)
    print(cw)
    print(cc)






    f.close()



















# class Person:
#     def _init_(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name,self.age)
#
# chinmay = Person("chinmay",90)
#
# chinmay.