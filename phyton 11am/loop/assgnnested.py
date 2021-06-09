counter = 5
for x in range(1,5):
    for y in range(x):
        if counter ==40:
            print(40, end = " ")
        print(counter,end =" ")
        counter = counter+5
    print()










counter = 9
for x in range(1,5):
    for y in range(x):
        print(counter,end ="")
        counter = counter-1
    print()






for x in range(1,6):
    for y in range(x):
        print(chr(y+65), end="")
    print()


counter = 1
for x in range(1,6):
    for y in range(x):
        print(counter, end="")
        counter+=1
    print()



counter = 1
row_numbers = int(input("enter row numbers :"))
for x in range(1,row_numbers+1):
    for y in range(1,x+1):
        print(counter,end="")
        counter +=1
    print()

counter = 9
row_numbers = int(input("enter row numbers :"))
for x in range(1,5,-1):
    for y in range(1,x-1):
        print(counter,end="")
        counter = counter - 1
    print()