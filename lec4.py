#Dictionary & set in python
info = {
    "name" : "Abhijit",
    "subject" : ["python","js","java"],
    "topics" : ("dict" , "set"),
    "cgpa" : 9.6,
    "mark" : [99,87,95],
    "age"  :24,
    "is_adult" : True

}

print(info)
print(info["name"])
print(info["age"])
print(info["subject"])

info["name"] = "Abhijit Mohanty" #overwrite
info["surname"] = "Babul  Mohanty"
print(info)

#empty dict
null_dict = {}
print(null_dict)
null_dict["name"] = "apna bhubaneswer"
print(null_dict)

"""Nested dictionaries"""
student = {
    "name" : "Abhi",
    "subjects" : {
        "phy" : 98,
        "js" : 76,
        "math" : 99
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

#Dict Method
#key()
print(student.keys())
#value()
print(student.values())
#item() # pair   s return
print(student.items())
pairs = list(student.items())
print(pairs[1])
#get()
print(student.get("name"))
print(student.get("subjects"))
#update()
student.update({"state" : "odisha"})
print(student)


"""set in python"""

collections = {1,2,2,2,3,4,"hello","world","world"}
print(collections)
print(type(collections))
print(len(collections)) # total num of item just ignore duplicates

#create a empty set
# collection = {} """not a empty set it is a empty dict"""

collection2 = set() # this is empty set
# add()
collection2.add("hello")
collection2.add("Abhijit")
collection2.add("world")
collection2.add(1)
collection2.add(2)
collection2.add(3)

#remove()
collection2.remove(2)
collection2.remove("world")
print(collection2)

#slear()
print(len(collection2))
collection2.clear()
print(collection2)

# pop() -> remove a random value
collection3 = {"Abhi","gendu","amiya","subha"}

print(collection3.pop())
print(collection3.pop())
print(collection3.pop())

#union()
set1 = {1,2,3}
set2 = {3,4,5,}
print(set1.union(set2)) # return a new set

#intersection()
print(set1.intersection(set2)) #op->3
