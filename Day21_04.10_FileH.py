# img
# binary
# text

#w
#r
#a
#w+
#r+
#a+

# program -1

# reference variable
# f = open("myfile.txt",'w')
# # userinput
# k = input('Please enter the name you wish to write')
# # write on the file
# f.write(k)
# # closing the file
# f.close()



#--------------------------

# f = open("myfile.txt",'w')
# # userinput
# k = input('Please enter the name you wish to write')
# # write on the file
# f.write(k)
# # closing the file
# f.close()


# fa = open('myfile.txt','r')
# str = fa.read()
# print(str)
# fa.close()
#

# fa = open('myfile.txt','r')
# str = fa.read(2)
# print(str)
# fa.close()


# fab = open('myfile.txt','a')
# r = input('please enter one random string')
# fab.write(r)
# fab.close()



# f = open('myfile2.txt','w')
# print('Enter the @ to exist')
# while(str != '@'):
#     str = input()
#     if(str != '@'):
#         f.write(str + '\n')
#
# f.close()



# f = open('myfile2.txt','r')
# str = f.read()
# print(len(str))
# f.close()

f = open('myfile2.txt','r')

print(f.read(1))
#str = f.readlines()
#lines  = f.read().splitlines()

# for item in lines:
#     print(len(item))

#f.close()


# f.seek(10,0)  # at the beginning
# f.seek(10,1)
# f.seek(-10,2)