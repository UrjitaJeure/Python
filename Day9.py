# # Set does not stores the value by index
# # Set only stores unique, no duplicate value
#
setA = {1,3,4,5,6,6,666,66}
print(setA)
print(setA[0])

setB = {1,3,4,5,66}
for a in setB:
    print(a)


setB.remove(66)
print(setB)

setB.pop()
print(setB)

setB.clear()
print(setB)

del setB
print(setB)
#
setC = {33,44,55}
setC.update([1,2,3,4,5])
setC.update("chinmay")
setC.update((2,3,4,56,7,8))
#
print(setC)
#
#
setD = {33,44,55}
#
setE = setD.copy()
print(setE)
print(setD)
setE.remove(44)
#
print(setE)
print(setD)
#
setF = {33,44,55}
setG = setF
setG.remove(55)
print(setF)
print(setG)

setJ ={1,3,4}
setK = {33,44,1}

print(setJ.difference(setK))
print(setK.difference(setJ))

setJ ={1,3,4}
setK = {33,44,1}


# setJ.difference_update(setK)
# print(setJ)

# setK.difference_update(setJ)
# print(setK)



setJ ={1,3,4}
setK = {33,44,1}


print(setJ.intersection(setK))
# setJ.intersection_update(setK)
#print(setJ)
setK.intersection_update(setJ)
print(setK)



setJ ={1,3,4}
setK = {33,44,1}


setJ.add(44)
print(setJ)


# setK.discard(33)
# print(setK)


# setK.discard(12)
# print(setK)


setJ ={1,3,4}
setK = {33,44,1}


setrr = {1,2,3}
sertt = {1,2}

print(setrr.issubset(sertt))
print(sertt.issubset(setrr))

print(setrr.issuperset(sertt))
print(sertt.issuperset(setrr))


setrr = {1,2,3}
sertt = {1,2,44,5,6,7,8,9}
print(setrr.union(sertt))



setA = {122,444,556}
setB = {1231,333,4445}
# print(setA.symmetric_difference(setB))
# setA.symmetric_difference_update(setB)
# print(setA)


# True when no element is common among sets ; unique values
print(setA.isdisjoint(setB))





# listA = [2,3,4,5,6]

# for x in listA:
#     print(x)
#
# for x in range(len(listA)):
#     print(listA[x])

h = '4a3b2c'

for x in h:
    print(type(h))