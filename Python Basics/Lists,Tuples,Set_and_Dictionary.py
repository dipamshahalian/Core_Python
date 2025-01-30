# -------------------------------------------------------LIST-------------------------------
from pickle import TUPLE

# dept = ['QA', 'UI', 'Dev']
# print(dept)
# print(len(dept))
#
# list1 = ["Formula", 'One', "Car"]
# list2 = [True, False, True]
# list3 = [1,2,3,4,5,6,7]
# l4 = [999, 'JB', 'Juice W0Rl$']
#
# print(type(list1))

# Using a list constructor i.e. NOTE that round braces (())
# l5 = list(('a', 'b', 'c'))
# print(l5)


# --------------------------------WAYS to Access items present in list
a = [1,2,3,4,5,6,7,8,9]
# print(a[1]) # indexing
# print(a[-3]) # -ve indexing
# print(a[0:6]) # elements upto certain range only, last value is not included
# print(a[:3])
# print(a[7:])
# print(a[-5:])
# print(a[-8:-1])

# print('Yes 1 is there') if 10 in a else print("No 10 isn't there")

# -------------------------------Change value of item present in the list
# a[1] = 1
# print(a)

#  change range of values
singers = ['JB', 'Laroi', 'Jack_Harlow', 'Bruno']
# singers[1:3] = ['JuiceWRLD', 'Sheeran']
# print(singers)
#
# # insert items
# singers.insert(1, 'PostMalone')
# print(singers)

# -------------------Add LIST items in the list
# append
# singers.append('Sarbina')
# print(singers)

# insert
# done

# extend
# rappers = ['Travis', 'MetroBoomin', 'Snoop']
# singers.extend(rappers)
# print(singers)

# ----------Remove List items

# to remove specified item
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.remove("banana") # if multiple occurrences then first specified item will be deleted here its banana at 1st index
# print(thislist)

# to remove item from the specific index only:
# thislist = ["apple", "banana", "cherry"]
"""thislist.pop(1)
print(thislist)"""

# also we can use del keyword
# del thislist[0]
# print(thislist)

# clear is used to empty the entire list
# thislist.clear()
# print(thislist)


# -----------------------------------------------------------TUPLE---------------------------------------------

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# t2 = (1,)
# print(type(t2))


# -------------------------------------------------------SETS----------------------------------------

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# -------------------------------------------------------DICTIONARIES-------------------------------------

mydict ={
    "Team": "Ferrari", "Driver": "Lewis", "Championships": "7"
}
print(mydict)
print(mydict["Team"])
