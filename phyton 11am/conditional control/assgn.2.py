#5
no1 = int(input("enter a number:"))
if (no1%5==0) and (no1%11==0):
    print("divisible number")

else:
    print("non-divisible")

print("--------------------")
slabtype = input("enter a type:")
list1 = ("industry")
list2 = ("commercial")
list3 = ("residence")

if slabtype in list1:
    print("rate is 5")
if slabtype in list2:
    print("rate is 4")
if slabtype in list3:
    print("rate is 6")

else:
    print("enter correct slabname")