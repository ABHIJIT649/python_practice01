"""function and recursion"""
def myFunc(a, b):
    sum = a + b
    print(sum)
    return sum

# function is used but less than redundancy

# call my function
myFunc(1,2) #argument value supply
myFunc(5,10)
myFunc(14,8)


#ex
"""function definition"""
def cal_sum(a,b): #parameter
    return a + b

sum1= cal_sum(23,56) # function call ; argument
sum2 = cal_sum(22,90)
print(sum1)
print(sum2)

#ex2
"""print hello"""
def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


#avrage of 3 number # mark average
def calc_avg(a,b ,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(98,87,99)

#build-in function
# two line in 1 line
print("abhijit",end=" ")
print("mohanty")

# user define function

"""Default parameters"""
# Assign a default value to parameter, which is used when no argument passed.


#Recursion
print("abhijit")