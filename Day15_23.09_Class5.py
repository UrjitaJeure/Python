
class person:
    def _init_(self, name):
        self.name = name
        self.db = self.Dob()

    def display(self):
        print(self.name)

    class Dob:
        def _init_(self):
            self.dd = 7
            self.mm = 11
            self.yy = 1980

        def display(self):
            print(str(self.dd),str(self.mm),str(self.yy))

p = person('chinmay')
print(p.name)
p.db.display()
h = p.db
print(h.dd)

#Encapsulation
#polymorphism
#Inheritance
#Abstraction

# program 1

#
# class Teacher:
#     def setid(self,id):
#         self.id = id
#
#     def getid(self):
#         return self.id
#
#     def setname(self,name):
#         self.name = name
#
#     def getname(self):
#         return self.name
#
#     def setaddress(self, address):
#         self.address = address
#
#     def getaddress(self):
#         return self.address
#
# t = Teacher()
#
# # t.setid(12)
# # print(t.getid())
# #
# # t.setname("chinmay")
# # print(t.getname())
# #
# # t.setaddress("Hadapar pune")
# # print(t.getaddress())
# class Student(Teacher):
#     def setmarks(self,marks):
#         self.marks = marks
#
#     def getmarks(self):
#         return self.marks
#
# amol = Student()
# amol.setid(12)
# print(amol.getid())
#
# amol.setname("chinmay")
# print(amol.getname())
#
# amol.setaddress("Hadapar pune")
# print(amol.getaddress())
#
# amol.setmarks(900)
# print(amol.getmarks())
#



# class Teacher(object):
#
#     def _init_(self,name,address):
#         self.name = name
#         self.address = address
#
#     def display(self):
#         print(self.name)
#
# class Student(Teacher):
#     pass
#
# amol = Student("binay","pune ")
# amol.display()



class Teacher(object):

    def _init_(self,name,address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name)

class Student(Teacher):
    def _init_(self,name,address,marks):
        super()._init_(name,address)
        self.marks = marks

    def display(self):
        print(self.marks)
        super().display()



d = Student("chinmay","pune",900)
d.display()