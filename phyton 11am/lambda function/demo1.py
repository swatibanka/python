x = lambda : print("I am lambda")
x()


x = lambda no1, no2 : print("The sum = ", no1+no2)
x(100,200)
x(no2 = 1, no1 = 99)


x = lambda : 50+60
res = x()
print("Result =", res)

x = lambda no1, no2: no1+no2
sum = x(50,70)
print("The SUM =", sum)