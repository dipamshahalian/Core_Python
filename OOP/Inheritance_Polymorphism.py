# -------------------------------------------------------INHERITANCE------------------------------------
# it's all abt parent class and child class

# class Student(Person):
#     pass
#
# p3 = Student("Arya", 18)
# p3.myfun()

# class Student(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)
#
# p3 = Student("Arya", 'F')
# p3.myfun()

# ------------Using __init__() in Child class:
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
#
# x = Student("Mike", "Olsen")
# x.printname()


# ------------------------------------------------POLYMORPHISM---------------------------

# Same name diffn executions

# Function Polymorphism: ex. len() cuz it provides diffn type of o/p's for string, tuple, dictionary

# x = "Hello World!"
#
# print(len(x))
# # -----
# mytuple = ("apple", "banana", "cherry")
#
# print(len(mytuple))


# Class Polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
