# f1 = open('acb.png','rb')
# f2 = open('cde.png','wb')
#
# bytes = f1.read()
# f2.write(bytes)
#
#
# f1.close()
# f2.close()


# with open('myfile.txt','w') as g:
#     g.write("hello")
#     g.write("new")
#
# with open('myfile.txt','r') as g:
#     print(g.read())
#
# # read ---- > read()
# # write ----> write()
# # lines -----> readLines()
# # lines -----> splitLines(
#
# import  pickle
#
# class Emp:
#     def _init_(self,id,name,sal):
#         self.id = id
#         self.name = name
#         self.salary = sal
#
#     def display(self):
#         print(self.id,self.name,self.salary)
#
# #f = Emp(2,"chinmay",23333)
# #g = Emp(2,"chinmay2",233)
# #f = Emp(3,"chinmay2",233)
#
# f = open('emp.dat','wb')
# num = input('How many employees you need to add') #3
#
# for i in range(int(num)):
#     id = int(input('Enter id'))
#     name = input('Enter name')
#     salary = float(input('Enter salary'))
#     e = Emp(id,name,salary)
#     pickle.dump(e,f)
#
# f.close()
#
# f = open('emp.dat','rb')
# while True:
#     try :
#         obj = pickle.load(f)
#         print(obj.id)
#         print(obj.salary)
#         print(obj.name)
#         obj.display()
#         i = i + 1
#     except EOFError:
#         print('End of objects ')
#         break


#---------------------------

#"nagpur    " # 10
#"pune      " # 10
#"mumbai    " # 10


h = 10
with open('cities.bin','wb') as g:
    num = int(input('Please number of cities'))
    for i in range(num):
        city = input('Enter city name') # pune
        city = city + (h-len(city))*" " # "pune      "
        city = city.encode()
        g.write(city)

# f.seek(0,0)
#f.read(10)
#f.read(10)