# ----------------------------------------Functions--------------------------
# def func1(): # def is keyword
#     print("Yo")
#
# func1() #calling a function
#
# def func2(fname): #fname is the argument
#     print(fname + "N/A")
#
# func2("Email: ")
# func2("Age: ")
# func2("Gender: ")

# def func3(fname, faddress): # two args bt giving only one value to expect an ERROR
#     print(fname + "N/A")
#
# func3()

# def my_function(*kids): # if no. of args are unknown
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")

# def funcnew(**kid):
#     print("His last name is " +kid["lname"])
#
# funcnew(fname = "Dipam", lname="Shah")


# --------------------------------LAMBDA----------------------------------
"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression."""

# x = lambda a: a+10
# print(x(5))
#
# y = lambda a, b: a+b
# print(y(5, 6))

# def myfunc(n):
#     return lambda a: a*n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(10))


# --------------------------------Return Types---------------------------------------------

def get_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]

print(get_numbers())

def get_user():
    return {"name": "Alice", "role": "Admin"}
print(get_user())