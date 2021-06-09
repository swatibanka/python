a = 1000

def show():
    print("i am show")
    print(a)
    b = 200
    print(b)
    print("sum = ", a+b)

print("hello")
show()
print("bye")


#global and variable name are same

a = 1000

def show():
    print(a)
    b = 200
    print(b)
    a = 99
    print("sum =", a+b)

print (a)
show()
print(a)
