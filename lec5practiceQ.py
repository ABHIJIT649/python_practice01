#print number from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
#
# #print number from 10o to 1
# j = 100
# while j >= 1:
#     print(j)
#     j -= 1

# print th multiplication table of a n
# n = int(input("enter a number : "))
# i = 1
# while i <= 10:
#     print(i * n)
#     i += 1

#print the element of the following list using loop
#[1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
#
# idx = 0
# while idx < len(nums):
#     print(nums[idx]) #nums[0],nums[1]....
#     idx += 1

#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
# num = [1,4,9,16,25,36,49,64,81,100]
#
# x = int(input("enter a number : "))
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("the number is found in idx :",i)
#         break
#     else:
#         print("finding..... ")
#     i += 1

#exx
# mob_no = [8018639436,9938388563,6372654807,9090238749]
#
# x = int(input("please enter mob no  : "))
# i = 0
# while i < len(mob_no):
#     if x == mob_no[i]:
#         print("the mob no is found in idx :",i)
#         break
#     else:
#      print(mob_no[i])
#
#
#     i += 1

#for loop
#print the elements of the following list using loop
#[1,4,9,16,25,36,49,64,81,100]

# numbers = [1,4,9,16,25,36,49,64,81,100]
#
# for value in  numbers:
#     print(value)


#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100,49)
#
# x = int(input("enter a number : "))
#
# idx = 0
# for el in nums:
#     if x == el :
#         print("found the number idx : ",idx ,"->",x)
#         break
#     idx += 1


"""range()"""
#print number from 1 to 100.

# for i in range(1, 101):
#     print(i)
#
# #print numbers from 100 to 1.
# for j in range(100, 0 ,-1): #dicresing
#     print(j)

#print the multiplication table of  a n number.
# n = int(input("enter a number : "))
# for m in range(1 , 11):
#     print(m * n)


#pass
#WAP to find the sum of first n number.(using while)
#for loop
# n = 10
#
# sum = 0
# for i in range(1, n+1):
#     sum  = sum+i
# print("total sum of n number : ",sum)

#while loop ex1
n = 10
sum1 = 0
while n >= 1:
    # print(n)
    sum1 += n
    n -= 1
print("total sum is : ",sum1)

#while loop ex1
n = 10
sum = 0
i = 1
while i <= n:
    sum = sum+i
    i += 1
print("total sum is : ",sum)


#WAP to find the factorial of first n numbers,(using for)
#factorial of 5  => 1*2*3*4*5
#using for
n = int(input("enter a number :"))
factorial = 1 #fact because 1 b 0* fact = all 0

for i in range(1,n+1):
    factorial = factorial*i
print("total factorial of number is : ",factorial)

# using while

n = int(input("enter a number : "))
i = 1
fact = 1

while i <= n:
    fact = fact*i
    i += 1
print("total fact is : ",fact)
