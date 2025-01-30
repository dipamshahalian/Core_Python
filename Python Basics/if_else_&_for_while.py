# -------------------------------IF-ELSE-----------------

# --------------------------------if------------------
# a = 10
# b = 3
# if a>b:
#     print("Dipam Shah")

# -------------------------------elif---------------
# a = 10
# b = 3
# if b>a:
#     print('Alian')
# elif a>b:
#     print('Software')

# -------------------------else---------------------
# a = 10
# b = 3
# if b>a:
#     print('Alian')
# elif a==b:
#     print('Software')
# else:
#     print('This is Dipam Shah')

# ------------------Short hand if---------------------
# a = 10
# b = 3
# if a>b: print("a is > b")

# --------------------------Short hand if-else----------------
# a = 10
# b = 6
# print('A is big') if a>b else print('B is big')

# ------------------ and, or, not with if-------------------
# a = 10
# b = 3
# # if a>b and b<a:
# #     print("True")
#
# if not a<b:
#     print('Correct')

# -------------------Nested if else----------------
# a = 10
# b = 5
# if a>b:
#     print('Keep going')
#     if b<a:
#         print('Still Correct')
#     else:
#         print('no sense')
# else:
#     print('End')

# ---------------------pass satement--------------
# x = 233
# y = 122
# if x>y:
#     pass


# -----------------------------------WHILE LOOP-----------------

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# -------------------using break statement------------

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# -------------------using continue statement------------

# i = 0
# while i<6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# ------------------using else statement after while-----------

# i = 0
# while i<6:
#     print(i)
#     i += 1
# else:
#     print('i is no longer less than 6')


# ----------------------FOR LOOP-----------------------

# -----------------------iterating over a list
# a = ['Dipam', 'Shah', 'AlianSoftware']
# for x in a:
#     print(x)

# -----------------iterating through letters
# for y in 'Hamilton':
#      print(y)

# ---------------------Using break statement
# car = ['ferrari', 'mclaren', 'mercedes']
# for h in car:
#     print(h)
#     if h == 'mclaren':
#         break

# -------------using continue statement
# for x in 'Alian':
#     if x == 'a':
#         continue
#     print(x)

# -----------range() function
# for x in range(6):
#     print(x)
#
# for x in range(2, 8):
#     print(x)

# for y in range(1, 10, 2):
#     print(y)

# for x in range(6):
#     print(x)
# else:
#     print('Finally Finished')

# for x in 'EnzoFerrari':
#     if x == 'o':
#         continue
#     print(x)

# ---------------Nested Loops
# car = ['Ferrari', 'Mercedes', 'Mclaren']
# driver= ['Lewis','George', 'Norris']
# for x in car:
#     for y in driver:
#         print(x, y)

# For loops can't be empty but if want then use pass
for x in [10,20,30]:
    pass