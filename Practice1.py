##Polymorphism
##Types
##Duck typing


# class girl(object):
#     def intro(self):
#         print('I am a girl')
#
#
# class boy(object):
#     def intro(self):
#         print('I am a boy')
#
# def call_them(obj):
#     obj.intro()
#
# a = girl()
# b = boy()
# call_them(a)
# call_them(b)


class girl(object):
    def introg(self):
        print('I am a girl')


class boy(object):
    def introb(self):
        print('I am a boy')

def call_them(obj):
    if (hasattr(obj, 'introg')):
        obj.introg()
    elif (hasattr(obj, 'introb')):
        obj.introb()
    else:
        print("Incorrect object passed")

a = girl()
b = boy()
call_them(a)
call_them(b)



##Operator overloading

class count1():
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
         return self.value + other.value        # object overloading. to add 2 objects
                                                #same class, same method name, different signature
class count2():
    def __init__(self, value):
        self.value = value




v1 = count1(1000)
v2 = count2(2000)
print(v1+v2)


#method overloading
# same class , same method name , different signature - overloading

class introduction:

    def sum(self, a = 'Null' , b = 'Null', c = 'Null'):
        if(a != 'Null' and b != 'Null' and c != 'Null'):
            print(a , b, c)
        elif(a!='Null' and b!='Null'):
            print(a, b)
        else:
            print('Please enter minimum 2 input ')

b = introduction()
b.sum('Urjita','Sonali')            #signatures
b.sum('Urjita','Sonali','Roja')
b.sum('Urjita')

#method overriding
