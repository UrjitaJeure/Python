from abc import ABC, abstractmethod
class myClass(ABC):
    @abstractmethod
    def calulate(self,x):
        pass

class Square(myClass):

    def display(self):
        print('hello')
    def calulate(self,x):
        print(x*x)

class Cube(myClass):
    def calulate(self,x):
        print(x*x*x)

    def display2(self):
        print('hello2')

# a = Cube()
# a.display2()
# a.calulate(12)
#
# b= Square()
# b.display()
# b.calulate(2)
c = myClass()


#if abstarct method is present in parent class , then child should have
#abstract method implemation (body)

# If a class contains abtract method , we cannot create object of same class


from abc import ABC, abstractmethod

class Car(ABC):

    def _init_(self,regno):
        self.regno = regno

    def OpenTank(self):
        print('print fuel tank ')

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass

class Audi(Car):
    def steering(self):
        print('audi steering')
    def braking(self):
        print('audi braking')

class BMW(Car):
    def steering(self):
        print('BWM steering')
    def braking(self):
        print('BWM braking')


a = Audi("123")
a.OpenTank()
a.braking()
a.steering()


b = BMW("567")
b.OpenTank()
b.braking()
b.steering()