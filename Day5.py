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

flowers = ["sunflower","jasmine","lotus"]
userInput = input('Please specify which flower you want to buy?') # sunflower

# for flower in flowers:
#     if userInput == flower:
#         print('available')
# else:
#     print('Not available')

if(userInput in flowers):
    print('available')
else:
    print('Not available')