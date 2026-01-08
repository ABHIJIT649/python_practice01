# creating class
# class Student:
#     collage_name = "ABC college"
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark
#         print("adding new student in database")
#
#
# #creating object is also called instance
#
# s1 = Student("karan",90)
# print(s1.name,s1.mark)
# s2 = Student("Abhijit",99)
# print(s2.name,s2.mark)
# print(s2.collage_name )
from lec3practiceQ import student


#ex1
# class Car:
#     color = "blue"
#     brand = "mercedes"
#
# car1 = Car()
# print(car1.color)
# print(car1.brand)


#method
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def welcome(self):
        print("welcome ",self.name)

    def get_mark(self):
        return self.mark



s1 = Student("karan",90)
# print(s1.name,s1.mark)
s1.welcome()
print(s1.get_mark())


"""static method"""

"""Abstract"""
#ex1
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car is started..")

car1 = Car()
car1.start()

