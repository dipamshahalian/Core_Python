# --------------------------MULTITHREADING-------------------------

# Multithreading is a technique that allows a program to run multiple threads (smaller units of a process) concurrently, enabling better performance and responsiveness.

# Python’s threading module is used to create and manage threads.

"""🔹 Perform multiple tasks at the same time (e.g., downloading multiple files simultaneously).
🔹 Improve UI responsiveness (e.g., handling user inputs while performing background tasks).
🔹 Optimize I/O-bound operations (e.g., network requests, file handling).
"""

import threading

# -------1. Basic
# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#
# thread = threading.Thread(target=print_numbers)
#
# thread.start()
#
# thread.join()
#
# print("Main thread execution is completed")

# 2. --------Multithreading with Multiple Threads
# import threading
# import time
#
# def print_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Thread 1: {i}")
#
# def print_letters():
#     for letter in "ABCDE":
#         time.sleep(1)
#         print(f"Thread 2: {letter}")
#
# # Creating multiple threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Start both threads
# thread1.start()
# thread2.start()
#
# # Wait for both threads to complete
# thread1.join()
# thread2.join()
#
# print("Both threads finished execution")


# ------------3. Daemon Threads

# import threading
# import time
#
# def background_task():
#     while True:
#         print("Running in background...")
#         time.sleep(10)
#
# # Creating a daemon thread
# thread = threading.Thread(target=background_task, daemon=True)
# thread.start()
#
# time.sleep(40)
# print("Main program exiting...")



# --------------------------MULTIPROCESSING----------------------------

import multiprocessing

def print_numbers():
    for i in range(5):
        print(f"Numbers: {i}")

if __name__ == "__main__":
    process = multiprocessing.Process(target=print_numbers())
    process.start()
    process.join()