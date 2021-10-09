# # Example 4
#
# class Car:
#
#     # class variable
#     madeIn = "India"                #
#
#     def _init_(self,color,type,regNo):
#         # instance  variable
#         self.color = color
#         self.type = type
#         self.regNo = regNo
#
#
# audi = Car("black","SUV",213)       #object 1
# bmw = Car("red","Sedane",456)       #object 2
# jaqour = Car("green","MUV",4546)    #Object 3
#
# print(audi.madeIn)
# audi.madeIn = "US"
#
# print(audi.madeIn)
# print(jaqour.madeIn)
# print(bmw.madeIn)
#
#
# # program 5
#
# class Sample:
#     def _init_(self):
#         self.x = 10
#     def modify(self):
#         self.x = self.x + 1
#
# s1 = Sample()
# s2 = Sample()
#
# print(s1.x)
# print(s2.x)
#
# s1.modify()
# print(s1.x) # 11
# print(s2.x) # 10
#
#
# # program 6
#
# class Car:
#
#     # class variable
#     madeIn = "India"
#
#     @classmethod
#     def modify(cls):
#         cls.madeIn = "USA"
#
#     def modifyI(self):
#         self.madeIn = "USA"
#
#
#     def _init_(self,color,type,regNo):
#         # instance  variable
#         self.color = color
#         self.type = type
#         self.regNo = regNo
#
#
# audi = Car("black","SUV",213)
# bmw = Car("red","Sedane",456)
# jaqour = Car("green","MUV",4546)
#
# audi.modifyI()
# Car.modify()
#
# print(audi.madeIn)
# print(audi.madeIn)
# print(audi.madeIn)
#
#
#
#
#
# # print(audi.madeIn)
# # audi.madeIn = "US"
# #
# # print(audi.madeIn)
# # print(jaqour.madeIn)
# # print(bmw.madeIn)
#
# #program 7
#
# class Student:
#     # constructor
#     def _init_(self , n = '',m=0):
#         self.name= n
#         self.marks =m
#
#     def display(self):
#         print(self.name)
#         print(self.marks)
#
#     def calculate(self):
#         if self.marks >= 60:
#             print('Division A')
#         elif  self.marks > 50 and  self.marks < 60:
#             print('Division B')
#         else:
#             print('Division C')
# #
# # Student('chinmay',40)
# # Student('amol',59)
# # Student('poorva',80)
#
# h = [Student('chinmay',40),
# Student('amol',59),
# Student('poorva',80)]
#
#
# for item in h :
#     item.calculate()

print('*****************************************************************************************************')

class birds:

    country = 'india'

    @classmethod
    def modify(cls):
        cls.country = 'USA'

    def __init__(self, state='null', bname='null', count=0):
        self.state = state
        self.bname = bname
        self.count = count

    def display1(self):
        print(self.state, self.bname, self.count)

KA = birds('KA','parrot',100)
MH = birds('MH', 'peacock',1000)

KA.display1()
MH.display1()

#KA.country = 'india2'
#print(KA.country)

birds.modify()
print(KA.country)
print(MH.country)






