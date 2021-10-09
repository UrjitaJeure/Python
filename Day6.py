x = 10
# collection ---> string list dictionary tuple set array
fruits = ["apple","mango",12,True]
# Array
#  list stores the value bu index

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

name = "amol"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
for char in name:
    print(char)

for index in range(len(name)):
    print(name[index])

#----------------------------------
print(type(name))
#         0         1    2    3
fruits = ["apple","mango",12,True]
print(type(fruits))
print(fruits[len(fruits)-1])




#using for loop
for item in fruits:
    print(item)

# using for with range function
for index in range(len(fruits)):
    print(fruits[index])

# printing last element of the list
print(len(fruits)-1)
print(fruits[(len(fruits)-1)])

# Methods

# Action
# Return


fruits = ["apple","mango","banana","chiku"]

#Method append
#Add the element at the last
#Return the length of new list

vb = fruits.append("papaya")
print(vb)
print(fruits)

#          0        1       2       3      4       5
fruits = ["apple","abc","mango","banana","chiku","mango"]


# updating the value at index 2
# fruits[2]= "grapes"
# print(fruits)

#listName.index(object,start,end)
# g = fruits.index("mango",3,5)
# print(g)

# If element is not found returns the error
# print(fruits.index("ango"))

# append , index , in operator

# flowers = ["sunflower","jasmine","lotus"]
# userInput = input('Please specify which flower you want to buy?') # sunflower

# for flower in flowers:
#     if userInput == flower:
#         print('available')
# else:
#     print('Not available')

# if(userInput in flowers):
#     print('available')
# else:
#     print('Not available')

n =  [1,33,4,55,6,66,44,55,33,22]
print(type(n))

n.append(23)
print(n)
#------------------------------------
ka = n.index(33)
print(ka)

#---------------------------------
ka = n.index(33,3,len(n)-1)
print(ka)

#----------------------------------
print('lily' in ["Lily","Sunflower"])

for item in n:
    print(item)

for item in range(len(n)):
    print(n[item])

#------------------------------------

city = ["pune","delhi","banglore","chennai"]
city[0] = "Mumbai"
print(city)

#----------------------------------------->
cityB = city
print(city)
print(cityB)
cityB[2] = "jaipur"
print(city)
print(cityB)

#----------------------------------------

country = ["Uk","USA","Japan","Uk"]

countB = country.copy()
countB[0] = "Bali"

print(countB)
print(country)

#--------------------------------------------

kaa =country.count("Uk")
print(kaa)

#---------------------------

# clearing the list

# country.clear()
# # print(country)

#---------------------

# Deleting the complete data struture
# del country
# print(country)

#----------------------------------

vehicle = ["cycle","scooter","motor","car"]
vehicleB = ["tracktor"]
vehicle.extend(vehicleB)

#----//["cycle","scooter","motor","car","tractor"]

print(vehicle)
vehicleB.extend(vehicle)
print(vehicleB)
#----------------------------------------
vehicle = ["cycle","scooter","motor","car"]
vehicle.insert(2,"john deer")
print(vehicle)


print(vehicle.sort())

#-------------------------------------
# vehicle.pop( ) // removes the lastElement
#vehicle.pop(2) // removes the element at index 2

# vehicle = ["cycle","scooter","motor","car"]
# vehicle.pop(2)
# print(vehicle)

#----------------------------------------

# vehicle = ["cycle","scooter","motor","car"]
# vehicle.remove("scooter")
# print(vehicle)

#-------------------------------------

# vehicle = ["cycle","scooter","motor","car"]
# vehicle.reverse()
# print(vehicle)

#Alphabet sorting

vehicle = ["cycle","scooter","motor","car"]
vehicle.sort()
print(vehicle)

# Number sorting
a= [12,22,3,33]

a.sort()
a.reverse()
print(a)