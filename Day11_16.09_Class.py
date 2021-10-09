class Student:
    age=10
    language="Hindi"
    fullName ="default"

    def display(self):
        print(self.fullName)

amol = Student()
amol.display()

# print(amol.age)
# print(amol.language)
# print(amol.fullName)

archit = Student()
amol.age = 34

archit.display()


print(amol.age)
print(archit.age)

class Student:
    def _init_(self ,nm=0 , ag=0 ,gr=0):
        self.name = nm
        self.age= ag
        self.gender = gr

    def display(self):
        print(self.name)


amol = Student(ag=23,nm="amol", gr="Male")
mayuri = Student("mayuri","24","Female")

mayuri.display()
amol.display()
#------------------------------------------->
class Bank:
    def _init_(self,accNo,accName,bal):
        self.accountNumber = accNo
        self.accName = accName
        self.balance = bal

    def depoist(self,amount):
            self.balance = self.balance+ amount

    def withDrawl(self,amount):
        if(amount < self.balance):
            self.balance = self.balance - amount
        else:
            print('Insufficient Balance')

chinmay = Bank(123,"chinmay deshpande",1000)
chinmay.withDrawl(500)
print(chinmay.balance)
chinmay.depoist(100000)
print(chinmay.balance)