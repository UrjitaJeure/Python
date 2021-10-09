x = 10
name = 'urjita'

#print(x+y)      # we cannot add 2 different data types in python. type error

print(type(x))  # to know the type of variable

# Addition Subtraction Multiplication Division ,Modulus
x=100
y=20
print(x+y) # 120
print(x-y) # 80
print(x*y) # 2000
print(x/y) # 5
print(x%y)  # 0

x = 10
print(type(x))

y = 10.0
print(type(y))



#Comparison operators
# <, >, <=, >=, !=, ==

a = 20
b = 50
x = 10
print(type(x))

x = 10.0
print(type(x))

x = True
print(type(x))
w = 16
u = 20
print(16 > 20) # False
print(12 == 13) # False
print(23 < 55) # True
print(12 != 13) # True
print(5 >= 5) # True
print(7 >= 8) # False

print(20 == 50) # whenever you use logical operators result will be in boolean

# Logical operator
# and , or , not


# and
# # True  True   True
# # True  False  False
# # False True   False
# # False False  False

# or
# # True  True   True
# # True  False  True
# # False True   True
# # False False  False

#not
# True - False
# False - True
print('-------------------')
print(5 > 6 or 7 > 6)
print(44 == 44 or 12 != 11 and 6 != 6)
print(not True)
print(not False)
print(4!=4 or 5 ==5 and 67 *5 or 7!=8)
#----------------------------------------


#Conditional statements -- we use conditional statement when we have multiple outputs
# 10 and above ------> 20 %
# 1-10 -------> 10 %

numberOfTickets = 5

if(numberOfTickets > 10):
    print('20 percent')
else:
    print('10 percent')








