# Polymorphism
def add(a, b, c=0):
    return a + b + c
print(add(2, 3))
print(add(2, 3, 4))

--> METHOD OVERLOADING
--> METHOD OVERRIDING
#-->Program
class Demo:
    def add(self, *nums):
        return sum(nums)
d = Demo()
print(d.add(1, 2))
print(d.add(1, 2, 3, 4))

#--> Program
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        print("Child method")
c = Child()
c.show()

#Using Super Method
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")
c = Child()
c.show()

#Encapsulation
class Bank:
    def __init__(self):
        self.__balance = 1000
    def deposit(self, amt):
        self.__balance += amt
    def get_balance(self):
        return self.__balance
b = Bank()
b.deposit(500)
print(b.get_balance())

#Abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")
c = Car()
b = Bike()
c.start()
b.start()
