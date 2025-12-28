"""1.WAP to ask the user to enter names of there 3 favorite movies & store them in list"""
#step-1
# a = str(input("enter the first moves name : "))
# b = str(input("enter the second moves name : "))
# c = str(input("enter the third moves name : "))
#
# movies = [a,b,c]
# print(movies)

#step-2
# movies = []
# x = str(input("enter the first moves name : "))
# y = str(input("enter the second moves name : "))
# z = str(input("enter the third moves name : "))
#
# movies.append(x)
# movies.append(y)
# movies.append(z)
#
# print(movies)

"""2.WAP to check if a list contains a palindrome element.(Hint:use copy() method)
[1,2,3,2,1]   [1,"abc","abc",1]
"""
# list1 = [1,2,1]
# list2 = [1,2,3]
# copy_list = list1.copy()
# copy_list.reverse()
#
# if copy_list == list1 :
#     print("this is palindrome")
# else:
#     print("this is not palindrome")
#
# copy_list1 = list2.copy()
# copy_list1.reverse()
#
# if copy_list1 == list2 :
#     print("this is palindrome")
# else:
#     print("this is not palindrome")


"""3.WAP to count the number of student with the 'A' grade in the following tuple
["C","D","A","A","B","B","A"]
 """
student = ["C","D","A","A","B","B","A"]
print(student.count("A"))


"""4.Store the above values in a list & store them from "A" to "D" in a dictionary"""
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)
list.reverse()
print(list)