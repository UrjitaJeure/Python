
# Single inheritance , single parent multiple child
class Bank(object):

    cash = 10000

    @classmethod
    def available_bal(cls):
        print(cls.cash)

class SBI(Bank):
    cash = 20000
    @classmethod
    def available_bal(cls):
        print(cls.cash + Bank.cash)

class PNB(Bank):
    pass
pnb = PNB()
pnb.available_bal()

sbi = SBI()
sbi.available_bal()

#Multi-level inheritance,  class inherit class

class GrandFather(object):

    lastName = "Deshpande"
    def _init_(self,firstName):
        self.firstName = firstName

    def display(self):
        print(self.firstName +" "+self.lastName)

class Father(GrandFather):

    def _init_(self,firstName,ffirstName):
        super()._init_(firstName)
        self.ffirstName = ffirstName

    def display(self):
        print(self.ffirstName +" "+self.lastName)
        super().display()

class Son(Father):

    def _init_(self,firstName,ffirstName,sfirstName):
        super()._init_(firstName,ffirstName)
        self.sfirstName = sfirstName

    def display(self):
        print(self.sfirstName+" "+self.ffirstName +" "+self.lastName)
        super().display()



chinmay = Son("manohar","shirsh","chinmay")
chinmay.display()


# Multiple Inheritance , multiple parent, single child


class Father:

    def height(self):
        print('6 feet tall')

class Mother:
    def color(self):
        print('Color is brown')

class Son(Father,Mother):
    pass


chinmay = Son()
chinmay.color()
chinmay.height()

# ---------
class Father:

    def name(self):
        print('name called from father')

class Mother:
    def name(self):
        print('name called from mother')

class Son(Mother,Father):                   ## if the method names are same , 1st mentioned class will be called first
    pass


chinmay = Son()
chinmay.name()

# ------------------

# Method resolution order

class A(object):
    def method(self):
        print('A class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')

class X(A,B):
    def method(self):
        print('X class method')
        super().method()
class Y(B,C):
    def method(self):
        print('Y class method')
        super().method()
class P(X,Y):
    def method(self):
        print('P class method')
        super().method()

p = P()
p.method()