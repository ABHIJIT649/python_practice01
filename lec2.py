# string and conditional statement
#String
str1 = "This is a string. we are creating ot is python."
print(str1)
str2 = "This is a string. \n we are creating ot is python."
print(str2) # \n next line
str3 = "This is a string. \t we are creating ot is python."
print(str3) #\t tab space

#concatination
str4 = "Abhijit"
str5 = "Mohanty"
final_str = str4 +  " " + str5
print(final_str)
print(len(final_str))

#length of str
str6 = "hello my name is Abhijit Mohanty"
print(len(str6))

#indexing
st = "Apna College"
print(st[0]) # access the character
print(st[1])
print(st[2])

#Slicing
slicing = "wellcome Abhijit"
print(slicing[0:5])
print(slicing[ :5])
print(slicing[1 : ])
print(slicing[ 9 : ])

#slicing -ve index
slt = "Abhijit"
print(slt[-5:-2])

#string FUnction

fun = "i am studying python from ApnaCollege"
#endswith()
print(fun.endswith("ege"))
print(fun.endswith("app"))

#capitalize()
print(fun.capitalize()) #first letter capital

#replace()
print(fun.replace("o","a"))
print(fun.replace("python","javascript"))

#findFunction
print(fun.find("o"))
print(fun.find("am"))

#count
print(fun.count("o"))
print(fun.count("from"))

#Conditional Statement
#if-elif-else
#ex1
age = 16
if age >= 18 :
    print("can vote")
    print("can drive")
else:
    print("can't vote")

#ex2
light = "black"
if light == "red":
    print("stop")
elif light == "yello":
    print("look")
elif light == "green":
    print("go")
else:
    print("WRONG SIGNAL")



