# human = ["chinmay","deshpande",12,44]
# # print(human)
# # print(type(human))
# # print(human[0])

# Dictionary -- consists of key and value ; discriptive
person = {

        'firstName':"chinmay",
        'lastName':"deshpande",
        'rollNo':13,
        'age':34

}
print(type(person))
print(person)  # prints the full dictionary
print(person['firstName'])  #prints value with firstName
print(person['lastName'])


for x in person:        # x=key
    print(x,person[x])  #prints all the key and its value one by one


for x in person.keys():
    print(x)            # prints only keys

for x in person.values():
    print(x)            # prints only values


for x,y in person.items():      #method items
    print(x,y)          #prints all the key and its value one by one


students = [

    {

        'firstName':"poorva",
        'lastName':"deshpande",
        'rollNo':33,
        'age':23

    },
{

        'firstName':"chinmay",
        'lastName':"deshpande",
        'rollNo':25,
        'age':37

    },
{

        'firstName':"Abhisha",
        'lastName':"deshpande",
        'rollNo':13,
        'age':34

    }

]


dictOne = students[0]
print(dictOne)
print(dictOne['lastName'])




# print(students[1]['age'])
# print(students[2]['firstName'])
#students = [dictOne,dictTwo,dictThree]
for item in  students:
    dict = item
    for key,val in dict.items():
        print(key,val)
#---------------------------------------------
vehical = {
    'color':"White",
    'regNo':123,
    'language':'english'
}
print(vehical)
print(vehical['color'])

for key in vehical:
    print(key,vehical[key])

for key in vehical.keys():
    print(key)

for key in vehical.values():
    print(key)

for x,y in vehical.items():
    print(x,y)

listA = [{'firstName':"chinmay"},{'firstName':"Samay"},{'firstName':"ram"}]
print(listA[0]['firstName'])

for item in listA:
    dict = item
    for x,y in dict.items():
        print(x,y)


#-----------------------------------------


h = {
    'age':23,
    'roll':34,
    'id':'2333'
}

# h['id'] = 777
# print(h)

j = h
print(j)
print(h)

j['id'] = 500

print(j)
print(h)



nn = {}
mm = nn.copy()
mm['age'] = 34
print(nn)
print(mm)

# to fetch the value from dictionary
print(nn['age'])

# to fetch the value from dictionary
print(nn.get('age'))

nn.pop('age')
print(nn)

# h.clear()
# print(h)

# del h
# print(h)
