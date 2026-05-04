#INHERITANCE
  --> Program
  class Parent:
    def show(self):
        print("Parent class")
class Child(Parent):
    def display(self):
        print("Child class")
c = Child()
c.show()
c.display()

#Types of Inheritance
Single
Multiple
Multilevel
  
 ## Multilevel Example Program : 
class A:
    def show(self):
        print("Class A")
class B(A):
    pass
class C(B):
    pass
obj = C()
obj.show()
