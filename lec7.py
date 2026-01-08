# file I/O in python
"""read the file"""
from random import sample
from symbol import with_stmt

# f = open("/Users/abhijitmohanty/PycharmProjects/PythonProject1/dmeo.txt","r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()


"""writing to file"""

# f = open("/Users/abhijitmohanty/PycharmProjects/PythonProject1/dmeo.txt","a")
#
# f.write("\n After that ")
#
# f.close()
#
# # Ex
# f= open("sample.txt","w")
#
# f.close()


"""combine read and write at a time 'r'"""
# f = open("dmeo.txt","r+")
# f.write("bac")
# print(f.read())
# f.close()


#ex "w+"
# f = open("dmeo.txt","w+")
# # f.write("bac")
# print(f.read()) # pura data delet khali
# f.close()


#width syntax

with open("dmeo.txt","r") as f:
   data = f.read()
   print(data)

with open("dmeo.txt","w") as f:
    f.write("new data")


#Deleting file
import os
os.remove("sample.txt")#remove file
