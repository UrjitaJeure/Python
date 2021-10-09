#amazaon  method overloading

# search(a)
# search(a,b)
# search(a,b,c)
#
#
# class ClassMy:
#
#     def sum(self, a = None , b = None, c = None):
#         if(a != None and b != None and c != None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
#         else:
#             print('Please enter a valid input ')
#
# b = ClassMy()
#
# b.sum(1,3)
# b.sum(1,3,4)
# b.sum(1)

# Overiding

# different class,same method name ,same signature
# inheritance -- overide inheritance

#world- save(a)
#sbi - save(a)
#a = sbi()

class WorldBank():
    def Saving(self,amount):
        if(amount > 1000):
            print('Saving successful')

class SBIBank(WorldBank):
    def saving(self,amount):
        if(amount > 500):
            print('SBI Saving successful')
        else:
            print('Minimum bal should be 500')

class BOIBank(WorldBank):
    def saving(self,amount):
        if(amount > 500):
            print('SBI Saving successful')
        else:
            print('Minimum bal should be 500')

SBIBank().saving(499)

# same class , same method name , different signature - overload
# Different class have interitance , same method , same signature
# overriding

import math
class Square():
    def area(self,x):
        print(x*x)

class Circle(Square):
    def area(self,x):
        print(math.pi * x * x)

c = Circle()
c.area(23)

d = Square()
d.area(23)