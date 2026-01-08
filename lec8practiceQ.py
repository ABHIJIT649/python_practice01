"""(01) : create a student class that takes name and mark of 3 object as argument in constructor. then create a method to print the average"""

class Student :
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    @staticmethod
    def hello():
        print("hello")


    def cal_avg(self):
        sum = 0
        for val in self.mark:
            sum = sum + val
        print("hi",self.name,"your avg score is",sum/3)



s1 = Student("karan",[90,98,45])
s2 = Student("Abhijit",[99,88,97])
s3 = Student("jiban",[88,87,91])

s1.cal_avg()
s2.cal_avg()
s3.cal_avg()

s1.hello()


"""(02) create a Account class with 2 attributes-balance & account no."""
"""(03) create a methods for debit,credit & printing th balance."""

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc


    #debit method
    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.",amount,"was debited your account")
        print("total available balance is ",self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.",amount,"was credited your account")
        print("available balance is ",self.get_balance())


    #printing method
    def get_balance(self):
        return self.balance


acc1 = Account(10000,8018639463)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(12000)

print(acc1.get_balance())
