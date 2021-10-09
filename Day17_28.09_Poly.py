# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
# x = Duck()
# y = Human()
# call_talk(x)
# call_talk(y)

# class Dog:
#     def bark(self):
#         print('Bow Bow')
#
# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
#
# x = Dog()
# y = Duck()
# z = Human()
#
# call_talk(x)
# call_talk(y)
# call_talk(z)


class Dog:
    def bark(self):
        print('Bow Bow')

class Duck(object):
    def talk(self):
        print('quack quack')

class Human(object):
    def talk(self):
        print('Hello hi ')

def call_talk(obj):
    if(hasattr(obj,'talk')):
        obj.talk()
    elif(hasattr(obj,'bark')):
        obj.bark()
    else:
        print("Incorrect object passed")


x = Dog()
y = Duck()
z = Human()

call_talk(x)
call_talk(y)
call_talk(z)

#operator overloading

print(6+6)
print("chinmay "+"deshpande")


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages
#
# class Booky():
#     def _init_(self,pages):
#         self.pages = pages
#
#
# b1 = Bookx(100)
# b2 = Bookx(200)
#
# print(b1+b2)
#----------------------------------->
class Bookx():
    def _init_(self,pages):
        self.pages = pages

    # def _add_(self, other):
    #     return self.pages + other.pages

class Booky():
    def _init_(self,pages):
        self.pages = pages

    def _add_(self, other):
        return self.pages + other.pages


b1 = Bookx(100)
b2 = Booky(200)
print(b2+b1)


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages

# class Booky():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
# class Bookz():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
#
# b1 = Bookx(100)
# b2 = Booky(200)
# b3 = Bookz(300)
# print(b2+b3+b1)






class Booky():
    def _init_(self, pages):
        self.pages = pages

    def _lt_(self, other):
        return self.pages < other.pages

    def _gt_(self, other):
        return self.pages < other.pages

class Bookz():
    def _init_(self, pages):
        self.pages = pages

y = Booky(100)
z = Bookz(200)

print(y>z)   