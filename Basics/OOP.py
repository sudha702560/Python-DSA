# OOPs -- Object Oriented Programming

# It is just a different way of writing code.

# Arvinder -- Country , name , Age , College , 

# name - 
# college - ABC 
# age = 27

# Class -- Class tells us that how exaclty our object is going to look like.

# Class  - It is a blueprint.

# class Person:
#     self.name = name 
#     self.college = college
#     self.age = age

# class Person:
#     self.name = name 
#     self.college = college
#     self.age = age
#     slef.id = id 

# Object -- 
# 
# _init_ , self , dunder method / magic method 


# CAr - Name , Year , Color , Number OF wheels 

# Object --  


# Without creating object we can not use the code inside the class.

# Class - Data members -- variables 
# Class Methods 
class Car:
    # constructor -- Magic Methods / Dunder Methods 
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color 
        # print("Hello")

    
    # Method 
    def PrintDetails(self):
        print(self.brand , "-" , self.color)

car1 = Car("ABC","Red")
# car1.PrintDetails()
# print(car1.color)
# print(id(car1))

car2 = Car("HONDA","Yellow")
# print(car2.brand)
# print(car1.brand)
# print(id(car2))
# Everything in Python is object.


# Method vs Function -- 

# Method can only be called by the class object.
# x = 3 

# print(type(x))

# l = [1,3,4,5,6,6]
# print(type(l))
# l.append()
# Function -- Block of code which can be called by anyone.
# len() -- is a function


# 

class Student:
    def __init__(self,name,roll_no, grade):
        self.name = name 
        self.roll_no = roll_no
        self.grade = grade
    
    def PrintDetails(self):
        print(self.name , self.roll_no , self.grade)

    
st1 = Student("Arvin",101,"A")
st1.PrintDetails()
st2 = Student("Arvi",151,"D")
st2.PrintDetails()
# 1234567 --> name --- Arvin
#  1234567 --> roll No  = 101



# 0985673 --> name = Arvi 
# 0985673 --> rool no = 151
# 