# ----------------------------File System Operations----------------------

# ------------------------------ 1. OS module

# ------Get current working directory

import os
# print(os.getcwd())

# ------Change Directory

# os.chdir("C:/Users/001/Desktop/Core_Python/Exception Handling")
# print(os.getcwd())

# ------List Files and Directories

# print(os.listdir("."))  # Lists all files and folders in the current directory

# To check if a file exist or not:

# if os.path.exists("C:/Users/001/Desktop/Core_Python/Working with Files and Directories/Read_Write_Files.py"):
#     print("Yeah File exists")
# else:
#     print("Are u sure?")


# --------------------------2. shutil module

import shutil

# -------To copy a file into another one:

# shutil.copy("File Sysytem Operations.py", "this_is_jst_for_dumping.txt")

# ------To delete a file:

# os.remove("this_is_jst_for_dumping.txt")
