# List and Tuple
#using list
mark = [98.4, 99.0, 76.9, 88.0, 80.7]
print(mark)
print(type(mark))
print(mark[0])
print(mark[1])
print(len(mark))

# in python add in list any type of data like int, float, string etc.
student = ["Abhijit", 99.0, "bhubaneswer"]
print(student)

#ex of string
list = ["babul", 24, "odisha"]
print(list[0])
student[0] = "mohanty"
print(student)


#List Slicing
marks = [98.4, 99.0, 76.9, 88.0, 80.7, 100]
print(marks[2 : 4])
print(marks[2 : ])
print(marks[-1 : ])

#append()
list1 = [2, 1, 3]
list1.append(4)
print(list1)

#sort()
list1.sort()
print(list1)

#sort disending order
list1.sort(reverse=True)
print(list1)

listr = ["banana", "litchi", "apple"]
listr.sort()
print(listr)

listr.sort(reverse=True)
print(listr) #becuse the first letter to desending order


#reverse()
list2 = ["q","a","b","r","i","c"]
list2.reverse()
print(list2)


#insert()
list3 = [2, 1, 3]
list3.insert(1,4)
print(list3)

#remove()
list4 = [2,1,3,1] #remove first occurrence of element
list4.remove(3)
print(list4)

#pop(idx) remove element at idx
list5 = [2,1,3,1]
list5.pop(1)
print(list5)


# Tuple in python #tuple is immutable means we cannot change anything
tup = (2,1,5,6)
print(tup[0])
print(tup[1])

# , mandate single value
tup1 = (1,)
print(tup1)
print(type(tup1))

# slice in tuple
tup2 = (1,2,3,4)
print(tup2[1 : 3])
#method in tuple
'''
1. tup.index(el) #return index of first occurrence tup.index(1) is 1
2. tup.count(el) #counts total occurrences tup.count(1) is 2
'''
#index(el)
tup3 = (2,2,3,1)
print(tup3.index(1)) # 1 is element and 3 is index position

#count(el)
print(tup3.count(2))
