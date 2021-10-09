name = "chinmay"

# strings stores the character by index
#   0     1    2    3     4   5    6
#   c     h    i    n     m    a   y
#  -7    -6   -5   -4    -3   -2  -1


print(name[0])
print(name[-3])

# slice
#name[start:end:step]
print(name[1:5])
print(name[2:6]) #endposition not included
print(name[3:])
print(name[:6])
print(name[-6:6])
print(name[-7:-3])
print(name[-3:-7])
print(name[1:6:2])

fullName = "chinmay deshpande"

print(fullName[0])

#basic two types of for loop

for char in fullName:
    print(char)

# range() function

# for loop with range() func
#
#
# for x in range(1,10):
#     print(x)
#
# for x in range(10):
#     print(x)
#
# for x in range(2,10):
#     print(x)
#
# for x in range(2,99):
#     print(x)
#
# for x in range(2,99,3):
#     print(x)


name = "amol"

# for char in name:
#     print(char)

# for x in range(4):
#     print(name[x])



g = "raghav"

print(g[0])
for char in g:
    print(char)

for char in range(6):
    print(g[char])


fruits = "apple"
print(fruits.count('p'))
count = 0

for char in fruits:
    if char == 'p':
        count = count + 1
print(count)

count2 = 0
for char in range(len(fruits)):
    #print(fruits[char])
    if fruits[char] == 'p':
        count2 = count2 + 1
print(count2)

#--------

m = "chinmaya deshpande"
for index in range(len(m)):
    if m[index] == "a":
        print(index)
# even
for x in range(2,51,2):
    print(x)

for x in range(2,100):
    if x % 2 == 0:
        print(x)

# odd
for x in range(1,50,2):
    print(x)




