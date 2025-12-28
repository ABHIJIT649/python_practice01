"""(01) WAP to print the length of a list(list is the parameter)"""
cities = ["odisha","mumbai","chennai","gurgaon","delhi"]
heros = ["ironman","thor","cap","odin","saktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

"""(02) Wap to print the element of a list in a single line.(list is the parameter)"""

hero = ["ironman","thor","cap","odin","saktiman"]

def sing_line(list):
    for item in list:
        print(item, end=" ")

sing_line(cities)


"""(03)Wap to find the factorial of n.(n is the parameter)"""

def fact_number(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
        print(fact)

fact_number(4)

"""(04) WAP tp convert USD to INR"""
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val ,"USD = ",inr_val,"INR")

converter(200)


"""WAP to input in a user and op odd or evn"""
x = int(input("enter a number : "))
def evn_odd(x):
    if x%2 == 0:
        print("even")
    else:
        print("odd")

evn_odd(x)


