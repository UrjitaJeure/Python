# user defined data type
# instance variable  (constructor variable)
# class variable

#@classMethod
#cls

#instance
#self

# outside the class
# using set get function
# using constructor


# class ?

# average
# percentage
# grade
class Student:
    country = "India"
    #[89,99,78,88,56]
    def _init_(self,name,lang):
        self.name = name
        self.lang = lang
    # total marks
    def totalMarks(self):
        self.sum = 0
        for x in self.lang:
            self.sum = self.sum + x
        return self.sum

    def percentage(self):
        self.percentage = 0
        self.percentage = (self.sum/len(self.lang)*100) * 100
        return self.percentage

    @classmethod
    def updateCountry(cls,Cname):
        cls.country = Cname



amol = Student("chinmay",[77,78,79,80,81])
chinmay = Student("chinmay",[73,74,79,86,89])

s = amol.totalMarks()
y = chinmay.totalMarks()
xa = amol.percentage()
ya = chinmay.percentage()
average = xa+ya
print(average/2)

#--------------------------------------->

class Student():
    count =0
    def _init_(self,name,rollNum):
        self.name  = name
        self.roll = rollNum
        Student.updateCount()

    def display(self):
        print('hello')

    @classmethod
    def updateCount(cls):
        cls.count = cls.count + 1


    @staticmethod                   #staic method does not need an object to be called. We can use class to call static method.
    def coutnOnObjects():           #static method can’t access or modify the class state
        return Student.count        #static methods know nothing about the class state


a = Student('chinmay',12)
b = Student('chinmay',12)
a.display()

print(Student.coutnOnObjects())