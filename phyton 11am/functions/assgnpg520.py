def call(a,b):
    print("ENTER 1st No:",a)
    print("Enter 2nd No:",b)
    c = a+b
    print("sum is =",c)

call(5,6)

print("------------------")

def fun1(x):
    print(x)

fun1(20)

print("------------------")

def name(fname,lname):
    fullname = fname+lname
    print("Full Name is : ",fullname)

name(fname = "swati", lname = "banka")

print("------------------")

def interestAmt(amount,time,r):
    interest = amount*time*r/100
    print("Interest is : ",interest)
interestAmt(1000,60,20)

print("-------------------")

def average(a,b,c,d,e):
    avg = (a+b+c+d+e)/5
    print(" Average is : ",avg)
average(a=40, c=60, e=80,b=20,d=100)

print("-------------------")

def average(total):
    avg = total/3
    print("Average is : ",avg)
average(600)

print("-------------------")
def area(r):
    a = 3.14 * r * r
    print("circle area:",a)
area(3)

print("-------------------")

def rarea(l,b):
    a = l * b
    print("Area of rect :",a)
rarea(20,35)

print("-------------------")
def calBill(cost,q):
    billAmt = cost * q
    print(" Billis : ",billAmt)
calBill(q=200, cost =500) 

print("-------------------")
def calDisAmt(billAmt,d):
    dAmt = billAmt/100*d
    print(" Discount : ",dAmt)
calDisAmt(10000,10)