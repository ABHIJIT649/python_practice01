#loop
count = 1 #iterator
while count <= 5 :
    print("hello")
    # count = count+1
    count += 1 #iteration

#print number from 1 to 5
i = 1
while i <= 5 :
    print(i)
    i += 1

 # print number from 5 to 1

i = 5
while i >= 1 :
    print(i)
    i -= 1


"""Brake and continue"""
#break : used to terminate the loop when encountered
#continue : terminate execution in the current iteration & continues execution of thr loop with the next iteration.

#break
k = 1
while k <= 5:
    print(k)
    if k == 3:
        break
    k += 1

#continue
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue #skip
    print(i)
    i += 1

#exxxx
i = 0
while i < 10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1

#for loop
veggis = ["patato","tamato","cucumer","brinjal"]
for val in veggis:
    print(val)

#for loop in tuple
tup = (1,2,3,4,5,6,7,8)
for n in tup :
    print(n)

#string in for loop
str = "Abhijit mohanty"
for chr in str:
    print(chr)


#optionl else
str = "Abhijit"
for chr in str:
    if chr == "j":
        print("found j..")
        break
    print(chr)
else:
    print("end")



"""range()"""
#Range function return a sequence of number, starting from 0 by
#defult, and increments by 1(by default),stops before a specified number.
"""range(start?,stop,step?)"""
#ex
range(5)#op -> 1,2,3,4 #stape size 1 mean +1
print(range(5))

#ex1
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

# ex2
seq1 = range(10)
for i in seq1:
    print(i)

#ex3
for i in range(11):
    print(i)


#start and stop
for i in range(2 , 10):
    print(i)

#ex4
for i in range(2 , 10,2):# stape size 2 [2,4 ,6 ,8]
    print(i)


    #all even number
for i in range(2, 100 ,2):
    print(i)

    #all odd number
for j in range(1, 100 ,2):
    print(j)


"""pass statement [null statement]"""
"""pass is a null statement that dose. it is used as a placeholder for future code."""
#for le in range()10:
#   pass

# ex
for i in range(5):
    pass
print("some useful work") #skep karna

