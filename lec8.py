#creating class
class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database")


#creating object is also called instance

s1 = Student("karan")
print(s1.name)
s2 = Student("Abhijit")
print(s2.name)

#ex1
# class Car:
#     color = "blue"
#     brand = "mercedes"
#
# car1 = Car()
# print(car1.color)
# print(car1.brand)