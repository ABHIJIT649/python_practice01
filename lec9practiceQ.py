"""[A] :-(01) Define a circle class to create a circle
with radius r using the constructor.
"""
"""(02) Define an Area() method of the which calculates
the area of the circle."""
"""(03) Define a Perimeter() method of the class which allow
 you to calculate the perimeter of the circle."""

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius  ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


"""[B] :-(01) define a Employee class with attributes role, department and
salary."""
"""(02) crtaeta a engineer class that inherits properties from Employee & has additional attributes names and age """


class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role = " ,self.role)
        print("department = " ,self.dept)
        print("salary = " ,self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",70000)

eng1 = Engineer("Abhijit mohanty",70000)
eng1.showdetails()


"""[c] :- create a class called order which stores item
& its price.
use dunder method __gt__ to convey that 
order1> order2 if price of order > price of order2"""


class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price


odr1 = Order("chips",50)
odr2 = Order("tea",20)

print(odr1 > odr2)



