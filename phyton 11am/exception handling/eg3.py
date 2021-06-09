print("hello")
try:
    no1 = int(input("enter integer no:"))
    no2 = int(input("enter integer no:"))
    print("Sum =", no1+no2)
    print("div =", no1/no2)
except ZeroDivisionError as zde:
    print(zde)
    print("don't divide by zero")
except ValueError as ve:
    print(ve)
    print("only integer values are allowed")

print("Sub =", no1-no2)
print("Mul =", no1*no2)

print("bye")