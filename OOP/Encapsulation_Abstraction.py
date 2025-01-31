""""# All abt public, pvt and protected members moreover the getter and setter methods

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute (encapsulated)

    # Getter method to access the balance
    def get_balance(self):
        return self.__balance

    # Setter method to modify the balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# Creating an instance of BankAccount
account = BankAccount("12345", 1000)

# Accessing public attribute
print(account.account_number)

# Accessing private attribute directly (will cause an error)
# print(account.__balance)  # AttributeError

# Accessing balance through getter method
print(account.get_balance())

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(300)

# Trying to withdraw more than the balance
account.withdraw(1500)"""


# --------------------------------ABSTRACTION--------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started.")

class Bike(Vehicle):
    def start(self):
        print("Bike Started.")

car = Car()
bike = Bike()

car.start()
bike.start()