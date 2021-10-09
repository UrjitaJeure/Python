#-------------------------->

# Define a class  ---

# name
# age
# language
# adharNo


# 4 Objects --->
# Reference variable only one
# loop ---
# # name
# # age
# # language
# # adharNo

# use constructor to set the values - 4 min


class person:

    def __init__(self, nm="null", age=0, lang="null", adno=0):
        self.name = nm
        self.age = age
        self.language = lang
        self.aadhar = adno

    def display(self):
        print('Hi! My name is ' + self.name)
        print('Age ' + str(self.age))
        print('Language ' + self.language)
        print('Aadhar no. ' + str(self.aadhar))


name = [person('Raj', 20, "English", 37453646437664546),person('Mohan', 20, "Hindi", 37453646437664546),person('Neel', 50, "Marathi", 37453646437664546)]
# name = person()
# name.display()

for item in name:
#    print(item)
    item.display()


#static method
class myclass:
    def __init__(self, a=0, b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        self.s =a+b+c
        myclass.update(self.s)


    def display(self):
        print(self.s)

    @classmethod
    def update(cls,s):
        cls.s = s

    @staticmethod
    def display1():
        return myclass.s > 10

z = myclass(10,10,10)
z.display()
print(myclass.display1())


#Inheritance

class parent:

    def __init__(self,sname):
        self.sname = sname

    def display(self):
        print(self.sname)


class child(parent):

    def __init__(self,sname, name):
        super().__init__(sname)
        self.name = name

    def display(self):
        print(self.name)
        super().display()


xyz = child('jeure','urjita')
xyz.display()


## Type of inhertance

#Single inhertance
# single parent, Multiple child

class india(object):

    capital = 'delhi'

    @classmethod
    def default(cls):
        print(cls.capital)

class karnataka(india):
    capital = 'banglore'

    @classmethod
    def default(cls):
        print(cls.capital +' '+ india.capital)

class maharashtra(india):
    pass

new = maharashtra()
new.default()

old = karnataka()
old.default()


##multi level inhertance

class school(object):

    sname = 'SIRS'

    def __init__(self, class1):
        self.class1 = class1

    def display(self):
        print(self.class1 + ' '+ self.sname)

class division(school):

    def __init__(self, class1, section):
        super().__init__(class1)
        self.section =section

    def display(self):
        print(self.section +' '+ self.sname)
        super().display()

class studentname(division):

    def __init__(self, class1, section, ssname):
        super().__init__(section, ssname)
        self.ssname = ssname

    def display(self):
        print(self.section + ' ' + self.sname+ ' ' + self.ssname)
        super().display()

abc = studentname(10, 'A', 'dinesh')
abc.display()


##multiple inheritance

class div(object):

    def call(self):
        print('Im belong to div A')

class grade(object):

    def call1(self):
        print('Im study in 10th')

class std(grade,div):
    pass

nmo = std()
nmo.call1()
nmo.call()
