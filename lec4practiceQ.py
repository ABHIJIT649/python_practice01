#ex1
dict = {
    "table" : ["a piece of furniture" , "list of a facts and figure"] ,
   "cat": "a small animal"
}

print(dict["table"])
# di = list(dict.items())
# print(di[0][1]["t2"])
# print(dict["table"]["t2"])

#example-2
subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(subjects)
print(len(subjects))#set is not duplicate allowed

#example-3
mark = {}

a = int(input("enter your python subject mark : "))
mark.update({"phython": a})
b = int(input("enter your c++ subject mark : "))
mark.update({"c++": b})
c = int(input("enter your java subject mark : "))
mark.update({"java": c})
print("your all sub marl is : ",mark)

#example-4
"""figure out a way to store 9 & 9.0 as separate values in the set.
(you can take help of built-in data types)"""
val1= {9,9.0}
print(val1) # set not allowed duplicates
val2 = {9,"9.0"}
print(val2) # 1st method id one in int type second is string type so both are print

# second method is
val3 = {
    ("float" , 9),
    ("int" , 9.0)
}
print(val3)