#   Class
#   example1
class student:

     def __init__(self):              #constructor
         self.name = "ravi"
         self.age = 40
         self.marks = 100


     def info(self):
         print('Hi My name is ' + self.name)
         print('and age is '+ str(self.age))
         print('I got  '+str(self.marks) +  ' marks')


calling=student()
calling.info()

print('**********************************************************************************')
# example2

class student2:

     def __init__(self,nm,ag,mrk):     #constructor with parameters
         self.name2 = nm
         self.age2 = ag
         self.marks2 = mrk


     def info2(self):
         print('My name is '+ self.name2)
         print('and age is '+ str(self.age2))        #converting to string
         print('I got  ' + str(self.marks2)+  ' marks')

person = student2("kenny",20,100)
person.info2()
person.language = "english"         #we can add elements
print(person.language)
person.language = "hind"            #we can update


print('**********************************************************************************')
#example3

class student3:
    def __init__(self,nm="",mrk=0):           #constructors with parameters and default values
        self.name3 = nm
        self.marks3 = mrk

    def info3(self):
        print('Hi i am',self.name3)
        print('I got ' + str(self.marks3)+ ' marks')

call =student3()
call.info3()



#-------------------------->

#class  ----> 4

# name
# age
# language
# adharNo


# 4 Objects --->
# Reference variable only one
# loop ---
# # name
# # age
# # language
# # adharNo

# use constructor to set the values - 4 min

