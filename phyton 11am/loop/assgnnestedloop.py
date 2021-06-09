counter = 1
for x in range(3):
    for y in range(3):
        print(counter,end="")
        counter +=1
    print()

#for practice, some mistakes
for x in range(1,6):
    for y in range(x):
        print(x, end="")
    print()


row_numbers = int(input("enter row numbers :"))
for x in range(1,row_numbers+1):
    for y in range(1,x+1):
        print(y,end="")
    print()



row_numbers = int(input("enter row numbers :"))
for x in range(1,row_numbers+1):
    for y in range(x+1):
        print(x,end="")
    print()























































