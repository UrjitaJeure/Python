##File handiling

#writing to a file
# o = open("textfile.txt",'w')           # reference variable o, open can open a existing file or create a new file if not present
# k = input('Please enter your name')        # userinput
# o.write(k)                                 # write on the file
# o.close()                                  # closing the file, if not closed the files gets corruppted



#Reading a file
# ok = open('textfile.txt','r')           # r -- reading a file
# str = ok.read()
# print(str)
# ok.close()
#
# ok = open('textfile.txt','r')
# str = ok.read(4)                        #reading till 4 characters
# print(str)
# ok.close()
#
#
# #Append to file
# ok = open('textfile.txt','a')             #a -- append
# i = input('please enter one random string')
# ok.write(i)
# ok.close()
#
#
#
# ok = open('textfile.txt','w')
# print('Enter the END to exit')
# while(str != 'END'):
#     str = input()
#     if(str != 'END'):
#         ok.write(str + '\n')
# ok.close()

#
# ok = open('textfile.txt','r')
# str = ok.read()
# print(len(str))                     #length of char
# ok.close()

# ok = open('textfile.txt','r')
#
# #print(ok.read(1))
# str = ok.readlines()
# print(str)
#
# lines = ok.readlines().splitlines()
# #print(lines)
# for item in lines:
#     print(len(item))
# ok.close()


#Append + Read
