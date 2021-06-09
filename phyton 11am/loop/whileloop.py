#script for sum of all digits, tell u get a single digit
#for eg 123456=1+2+3+4+5+6=21=2+1=3

no = int(input("enter a number: "))

while (no>9):
    sum = 0
    while (no>0):
        rem = no%10
        no = no//10
        sum = sum+rem
    no = sum
    
print("The sum of all digit:", sum)




#script fr adding first digit and last digit of given number
no = int(input("enter a number: "))
f_no = no%10
while (no>0):
    rem = no%10
    no = no//10
    

print("The sum of given number: ", f_no+rem)






#script to a given number in reverse order.

no = int(input("enter a number: "))

rev = 0
while (no>0):
    rem = no%10
    no = no//10
    rev = (rev*10)+rem

print("The given number in reverse order:", rev)

print(input("Enter a number: ")[::-1])

#script to print sum of all digits of given number

no = int(input("enter a number: "))
sum = 0
while (no>0):
    rem = no%10
    no = no//10
    sum = sum+rem

print("The sum of all digit:", sum)

print(input("Enter a number: ")[::-1])
