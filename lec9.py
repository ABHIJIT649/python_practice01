#del key word
class Student:
    def __init__(self,name):
        self.name = name


s1 = Student("Abhijit")
print(s1.name)
del s1.name
# print(s1.name)

"""privet attribute (__) two underscore and privet"""

class Account :
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass


    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12344","abcdfr132")
print(acc1.acc_no)
# print(acc1.__acc_pass)
print(acc1.reset_pass())



#ex2

class Person:
    __name = "anonymous"

    def __hello(self):
       print("hello person")

    def welcome(self):
       self.__hello()

p1 = Person()

# print(p1.__name)
print(p1.welcome())


"""Inheritance"""

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started")
#
#     @staticmethod
#     def stop():
#         print("car stopped")
#
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand
#
#
# class Fortuner(ToyotaCar):
#     def __init__(self,model):
#         self.model = model

# car1 = Fortuner("disel")
# car1.start()


"""multiple inheritance"""
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


"""super method"""
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

        # self.type = type

car1 = ToyotaCar("prius","hybrid")
print(car1.type,car1.name)

"""class method and static method"""

class Person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.name = name
        # Person.name = name # option to change class attribute
        #self.__class__.name = name # option to change class attribute

#use class method to change class attribute

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

"""property decorator"""
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        #percentage
        # self.percentage = str ((phy + chem + maths)/3) + "%"


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"
"""simple method to change mark of phy and see the percentage change"""


s1 = Student(99,90,87)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)


"""polymorphism"""

print(1 + 2) #3
print(type(1))

print("Abhjit" + " " + "Mohanty") #concatenate
print(type("Abhjit"))

print([1,2,3] + [4,5,6]) #marge
print(type([1,2,3]))

#ex1
"""create a complex number in python"""

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real,"i +" ,self.imag,"j")


    def __add__(self,num2):
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return Complex(newreal,newimag)

    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimag = self.imag - num2.imag
        return Complex(newreal,newimag)


num1 = Complex(3,4)
num1.showNumber()

num2 = Complex(5,9)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()