from abc import ABC,abstractmethod
class worldBank(ABC):

    def _init_(self,country):
        self.country = country

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass


class SBI(worldBank):
    def save(self):
        print('SBI saving method')

    def loan(self):
        print('SBI loan saving method')

    def personalLoan(self):
        print('New values SBI')


class BOI(worldBank):
    def save(self):
        print('BOI saving method')

    def loan(self):
        print('BOI saving method')

    def personalLoan(self):
        print('New values BOI')


chinmay = SBI("India")
print(chinmay.country)

chinmay.save()
chinmay.loan()

#------------------------------------------->
#
#
# class Myclass(ABC):
#
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class Oracle(Myclass):
#     def connect(self):
#         print('connecting to the oracle database')
#
#     def disconnect(self):
#         print('Disconnecting from the oracle db')
#
#
# class Postgres(Myclass):
#     def connect(self):
#         print('connecting to the postgres database')
#
#     def disconnect(self):
#         print('Disconnecting from the postgres db')
#
# class MongoDb(Myclass):
#     def connect(self):
#         print('connecting to the MongoDb database')
#
#     def disconnect(self):
#         print('Disconnecting from the MongoDb db')
#
# class Database:
#     str = input('Enter the name of db you wish to connect') #oracle
#     # convert the string into the className
#     className = globals()[str]
#     h = className()
#     h.connect()
#     h.disconnect()
#
# class Hi:
#     print("hello")