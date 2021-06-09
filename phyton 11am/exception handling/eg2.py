print("hello")
no1 = int(input("enter integer no:"))
no2 = int(input("enter integer no:"))

print("Sum =", no1+no2)

try:
    print("div =", no1/no2)
except ZeroDivisionError as zde:
    print(zde)
    print("don't divide by zero")

print("Sub =", no1-no2)
print("Mul =", no1*no2)

print("bye")