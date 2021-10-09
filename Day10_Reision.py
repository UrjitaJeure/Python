#-------->

#extension py

number = 10
print(type(number))

number = 10.0
print(type(number))

isAdult = True
print(type(isAdult))

char = "c"
print(type(char))

#--------------------------------
name = "chinmayd"
print(name[0])
print(name[2:len(name)])

# for loop

for char in name:
    print(char)

for x in range(len(name)):
    print(name[x])

# list


listA = [1,3,4,5,66,77,88]
print(type(listA))

for item in listA:
    print(item)

for x in range(len(listA)):
    print(listA[x])


# dictionary

human = {
    'fullName':'chinmay',
    'age':23

}

# Does not stores the value by index

print(human['fullName'])
print(human.get('fullName'))
for k in human:
    print(k,human[k])


#-------------------------------

setA = {33,44,55,66,77,77}
print(setA)

#-----------------------------

h = 'book'
#{
# #   'b':1,
# #   'o':2,
# #   'k':1
# #
# # }

g = {}


j = {
    'a':2,
    'b':3,
    'a':4
}

# updating the dict value
j['a'] = 5
# inserting the new value
j['x']= 3

#print(j.get('a',"no return"))

#print(j)

h = 'book'
j = {'b':1,'o':2,'k':1}
for char in h:
    print(char)
    j[char] = j.get(char,0) + 1
#   j['b'] = 1
#   j['o'] = 1
#   j['o']= 2
#   j['k'] = 1


hh = [334,44,55,55,66,77,88,99]
min = hh[0]
max = hh[0]

for x in hh:
    if max < x:
        max = x
    elif min > x:
        min = x    # -334

print(min)
print(max)


h = '4a3b2c'
# #aaaabbbcc
# print(int('4'))

# print(h)
#
# for x in h:
#     if type(x) == "<class 'str'>":
#         print("hello")

rev = " "

for i in range(len(h)):
    if(i%2 == 0):   # 4
        num = int(h[i])
        print(num)
        rev = rev + num * h[i+1]

print(rev)