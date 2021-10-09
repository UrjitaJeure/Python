amit = {
    'firstName':"amit",
    'lastName': "Dani",
    'age': 23,
    'rollNo': 45,
    'skills':["python","java","c#"]
}

# by square braacket notation
print(amit['firstName'])
# by get method
print(amit.get('firstName'))

# Updating the value
amit['firstName'] = "amol"
print(amit)
#Updating the value by update method
amit.update({'language':"marathi"})
amit.update({'language':"Hindi"})
print(amit)
#Deleting the values from dictionary

amit = {
    'firstName':"amit",
    'lastName': "Dani",
    'age': 23,
    'rollNo': 45,
    'skills':["python","java","c#"]
}

amit.popitem()
print(amit)
amit.pop('lastName')
print(amit)

#
# amit.clear()
# print()

amol = amit.copy()
print(amol)
print(amit)

amit['age']= 44
print(amol)
print(amit)

# setdefault
amit.pop('age')
print(amit.setdefault('age',56))
print(amit)


y = ['age','rollNumber','name']
x = [1,2,3]
bh = dict.fromkeys(y,x)
print(bh)



amit = {
    'firstName':"amit",
    'lastName': "Dani",
    'age': 23,
    'rollNo': 45,
    'skills':["python","java","c#"]
}


for key in amit:
    print(key , amit[key])

for x in amit.keys():
    print(x)

for x in amit.values():
    print(x)

for x,y in amit.items():
    print(x,y)

