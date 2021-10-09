


name = "chinmay"
print(type(name))

# string stores the value by index

firstName = "raghav"
#      0   1  2  3  4  5
#      r   a  g  h  a  v
print(firstName[0])
print(firstName[5])



# object --- human
# properties -- age color weight height firstName
# methods -- walk() talk() running()


# object ---- car
# properties --  color type glasses regNo
# methods -- start() stop()


# object ----bank
# properties -- accountName , accountNumber
# methods -- depoist() withdraw()

# Method len()
# Action - to find the length
# Return number .. i.e the length of string


city = "Pune"

j = len(city)
print(j)

city = "Nagpur"
kk = len(city)
print(kk)

#     0  1   2  3  4  5
#     n   a  g  p  u  r

print(city[0])
print(city[kk-1])

# len of string -1 will the last index

nameC = "amol"
vv = len(nameC)
print(vv)
print(nameC[4-1])

#------------------------------>
# Methods of string
language = "Hindi"
bb = type(language)
print(bb)

# Method

# Action
# Return
bbc = language.lower()
print(bbc)

# Action
# Return
nn = language.upper()
print(nn)

language = "Hindi"
print(language.lower().upper().count('H'))
# lower() --- string --- string

# count - also consider substring
fruit = "banana"
vv = fruit.count('na')
print(vv)

# lower() upper() count() capitalize

# Method -- capatilize first character of string
# return  - string

oo = fruit.capitalize()
print(oo)















