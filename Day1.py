

x = 10 #pythos is dynamic, here we are assigning 10 to x i.e x is int
x = 'urjita'
x =  True   #here ture is a boolean value and x is assigned the same


## Arthimatic operation

x=10
y=20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

#Do not repeat ---- DRY code

def cal(x,y):           #cal is a function with parametere x and y
    print(x + y)        #arguments
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

cal(10,20)


# Basic types of Functions

# Functions without parameter and without return type
def cal():
    print(7 + 8)

cal()

# Functions with parameter and without return type
def cal(x, y):
    print(x + y)

cal(10, 20)


# Functions with parameter and with return type
def cal(x, y):
    return x + y


z = cal(10, 40)
print(z)


# Functions without parameter and with return type
def pivalue():
    return 3.14

z = pivalue()
print(z)














