from pkg_resources import non_empty_lines

name = "Abhijit" #string
age = 23
price = 23.99

age2 = age

print(age2)
print("my name is  :" , name)
print("my age  is  :" , age)
print("my price  is  :" , price)

#find the type
print(type(name))
print(type(age))
print(type(price))


#boolean and non

age = 23
old = False
a = None

print(type(old))
print(type(a))


#sum of two number
a = 4
b = 5
sum = a + b
print(sum)

#comment
#singline comment
# print("hello world")
# print("hello world")

#multiline comment
"""
print("hello world")
"""

#Arithmetic operator

a = 10
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # riminder
print(a ** b) #power operator (a^b) 10 * 10 two time

# Relational Operator

a = 50
b = 20

print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
print(a == b) # False
print(a != b) #True

#Assignment Operator

num = 10
# num = num + 10 #10+10 = 20
num += 10 #10 + 10 = 20  #short type
print("num : ", num)

#2
num2 = 20
num2 -= 20
print("num2 : ", num2)

#3
num3 = 30
num3 *= 30
print(num3)

#Logical operator( not ,  and , or )
#not Operator
print(not False)
print(not True)
#ex
a = 30
b = 50
print(not (a < b))

#and Operator
# val1 = True
# val2 = False # op - False
val1 = True
val2 = True
print("and operator : ",val1 and val2)

#or Operator
val3 = True
val4 = False

print("OR operator : ", val3 or val4) # one is true and true

print("OR operator: " ,(a == b) or (a < b)) # one value is true op is true

#Type Conversion

#conversion (Automatics)
a = 2
b = 4.24
sum2 = a + b
print(sum2) #conver int to float answer is float value

#Type casting (manually)
c = int("2")
d = 4.24
sum3 = c + d
print(sum3) #convert string to int and float

#ex
f = 3.44
i = int(3.44)
print(i)
print(type(i))

#input in user
name = input("enter your name : ")
print("wellcome",name) #all input value convert in string

#ex
user = input("Enter your name : ")
age = int(input("Enter your age : "))
mark = float(input("Enter your mark"))

print("Wellcome ",user)
print("age = ",age)
print("mark =",mark)
