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
"""