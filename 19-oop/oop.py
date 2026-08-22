"""
What is a Class?
- A class is a blueprint that defines what an object will look like.
- A class is like a template or a plan.
- Student:
   name, age, department
   study, take an exam
 
 
Class Definition:
class Student:    # Student -> class name
  pass
 
 
Why do we use classes?
* To make code more organized
* To reduce code repetition
* To make managing large projects easier
* Scikit-learn -> the most important machine learning library
 
The __init__ Method: A special method that runs automatically when an object is created (constructor method).
 
 
Student class
  - name  - age
 
 
class Student:
    def __init__(self, name, age):
        print(f"Creating a new student:\n name:{name} - age:{age}")
 
# Creating an object
student1 = Student("Ali", 21)
 
Attribute: Variables that represent the properties belonging to a class or an object,
in other words, the structures that hold an object's data.
Student:
  - name, age and department >> these are the student's attributes
 
 
class Student:
    def __init__(self, name, age):
        self.name = name   # name attribute   # means the student's name and the student's age
        self.age = age     # age attribute
 
# Using Attributes:
student1 = Student("Ali", 21)  # object
# How can we access the attributes of the student1 object?
print(student1.name)  # Ali
print(student1.age)   # 21
 
 
Method: A function defined inside a class. Methods represent the actions an object can perform.
 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age         # Both of these are attributes
 
    def introduce(self):
        print(f"Hello, my name is: {self.name}")
 
student1 = Student("Ali", 21)
student2 = Student("Hasan", 28)
 
student1.introduce()
student2.introduce()

Creating objects and using classes:
   - class: template > car
   - object: think of it as the structure produced from the template (mercedes, audi)


class kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def bilgi_goster(self):
        print(f"kitap:{self.ad}")
        print(f"yazar:{self.yazar}")
        print(f"sayfa:{self.sayfa}")

# creating an object
kitap1 = kitap("Python programlama", "Kaan", 500)

# accessing attribute values
print(kitap1.ad)
print(kitap1.yazar)
print(kitap1.sayfa)

# Method
kitap1.bilgi_goster()

# kitap:Python programlama
# yazar:Kaan
# sayfa:500

# Creating multiple objects
kitap1 = kitap("Python programlama", "kaan", 500)
kitap2 = kitap("Python programlamaya giriş", "can", 150)

print(kitap2.ad)
kitap2.bilgi_goster()


# Object Oriented Programming
# constructor special method:

class Person:
    def __init__(self):
        print("Wow! it worked automaticly")

p1 = Person()

# (__str__) dunder (magic special method)
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}"

p1 = Person("Elif Yalın", 34)
print(p1)

# (__repr__) dunder special method: used to get more detailed info for debugging
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __repr__(self):
        return f"Name:{self.name!r}\nAge:{self.age!r}"

p1 = Person("Cansu Öztekin", 20)
print(p1)


# Creating our own custom method:
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def myinfo(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age} year old")

p1 = Person("Mehmet Demir", 29)
p1.myinfo()  # functions don't run unless called. The exception to this is def __init__

# Changing a class variable from outside the class:
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def myInfo(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age} years old")

p1 = Person("Tuğçe Özgün", 45)
p1.age = 33
print(p1.age)
p1.myInfo()

# We can't leave a class body empty, to avoid an error: use pass or ...
class Person:
    pass

# Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myPrint(self):
        print(self.firstname, self.lastname)

p1 = Person("Yılmaz", "Tekin")
p1.myPrint()

class Student(Person):  # child class (derived class)
    pass

p1 = Person("Yılmaz", "Tekin")
p1.myPrint()

# Using my own methods instead of the inherited class method

class Person:  # parent class or base class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myPrint(self):
        print(self.firstname, self.lastname)

class Student(Person):  # child class
    def __init__(self, fname, lname):

p1 = Student("Su", "Dinçer")
p1.myPrint()


# The super() method:
class Person:  # parent class or base class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myPrint(self):
        print(self.firstname, self.lastname)

class Student(Person):  # child class
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

p1 = Student("Su", "Dinçer")
p1.myPrint()


# Creating methods specific to the inheriting class
class Person:  # parent class or base class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myPrint(self):
        print(self.firstname, self.lastname)

class Student(Person):  # child class
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduation}")

p1 = Student("Su", "Dinçer", 2022)
p1.welcome()

"""

# Method Overriding:
class Animal:
    def speak(self):
        return "sound"

class Mouse(Animal):
    pass

class Dog(Animal):
    def speak(self):  # method overriding
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
m = Mouse()
print(dog.speak())
print(cat.speak())
print(m.speak())