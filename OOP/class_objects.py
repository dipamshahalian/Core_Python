# --------------------------------------------------CLASS and OBJECT----------------------------------

# Simple class and object
# class Class1:
#     x = 5
#
# p1 = Class1()
# print(p1.x)

# ---------------------------- __init__() function-----------------------------
# class Car:
#     def __init__(self, name, championships):
#         self.name = name
#         self.championships = championships
#
# p1 = Car("Ferrari", 16)
# print(p1.name)
# print(p1.championships)
#
# class Company:
#     def __init__(self, name, employees):
#         self.name = name
#         self.employees = employees
#
# p3 = Company('Alian', 50)
# print(p3.name)
# print(p3.employees)

# -------------------------------------------  __str__() function--------------------------

# above are the ex. of string representation without and below is with str function

# class Company:
#     def __init__(self, name, employees):
#         self.name = name
#         self.employees = employees
#
#     def __str__(self):
#         return f"{self.name}({self.employees})"
#
# p3 = Company('Alian', 50)
# print(p3)

# ------------------------------- OBJECT METHODS-------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfun(self):
#         print("Hello my name is " +self.name)
#
# p1 = Person("Dipam", 21)
# p1.myfun()


