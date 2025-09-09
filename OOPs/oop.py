# # OOPs --> Object Oriented Programming --> It is just another way of writing code. 

# # int , string , Bool , list 

# # Real World -- Car --> 
# # Color , Brand , year , number of Wheels , Speed , Engine 

# # class Car:
# #   int Speed 
# #   string brand 

# # Class , Object -- Everything in Python is an Object. variable , Sets , List , Dictionaries , tuples etc.

# x  = int(30)
# print(type(x))
# # We have created an object of int class

# # Class is a blueprint for the object.

# # We can create obejcts suing the class (Blueprint).

# # car1 = Car()
# # car2 = Car()


# # li = [2,3,45,6,6]

# li2 = list([23,45,67,89])


# # Functions vs Methods 
# # def Name():

# # Functions inside a class are called Methods. Methods can only be accessed by the objects of the class. 
# # And these are accessed using the . (dot) operator.

# # len() ---> is a function 
# print(len(234))


# # append -- List 
# li2.append(30)




# Define a class named 'Dog'
class Dog:
    # Class attribute: shared by all instances of the class
    species = "Canine"

    # Constructor method: called when a new object is created
    def __init__(self, name, age):
        # print("Hello")
        self.name = name  # Instance attribute: unique to each object
        self.age = age    # Instance attribute: unique to each object

    # Instance method: defines behavior of the object
    def bark(self):
        return f"{self.name} says Woof!"

    def Eats(self):
        return f"{self.name} is eating!"


# Create objects (instances) of the 'Dog' class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
# dog3 = Dog("jhumroo" , 13)

# Access class attributes
# print(f"Dog species: {Dog.species}")

# Access instance attributes
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")

# Call instance methods
# print(dog1.bark())
# print(dog2.bark())

# print(f"{dog3.name} is {dog3.age} years old.")




# __init__  -- Dunder Method / Magic Method / Special Method 

# Constructor Method -- __init__() --> We don't call this method. This will be called when we create the Object of the class.

# Self --> We are passing the object ID using self.
# id()
# print(id(dog2))
# print(id(dog1))

# __Python__()  -- NO 

# Inheritance -- One class can reuse the code from another class. 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__ method
        self.breed = breed

    def speak(self):  # Overriding the speak method
        return f"{self.name} barks!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

# Create instances of the classes
my_animal = Animal("Generic Animal")
my_dog = Dog("Buddy", "Golden Retriever")

# Demonstrate inherited and overridden methods
print(my_animal.speak())
print(my_dog.speak())
print(my_dog.fetch())

# Abstraction -- Car -- Hiding the uneccessary information from the actual user. 


# Polymorphism -- Occuring in Many forms. --> Runtime , Compile ---> + --> int + int , String + String , Set + Set 

# Encapsulation -- Combining the related details 

# Super()  -- to call the init contructor of Parent Class.


# private member (_) , public member 