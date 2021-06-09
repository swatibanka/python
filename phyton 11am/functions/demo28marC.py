#modifying global variable

a = 1000
def show():
    global a
    a = 99
    b= 200
    print(a,b)

print(a)
show()
print(a)