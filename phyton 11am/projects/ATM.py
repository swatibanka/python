#Validatng ATM pin, giving 3 attemps for pin and completing the operations and declaring the final balance
import time

print("Kindly insert your card")

#to halt the execution of the program for the given times in second
time.sleep(10)
# for 3 attemps to input pin number
for x in range(3):

    password = 1234 #suppose
    pin = int(input("Enter you pin number:"))

    balance = 5000 #suppose
    if pin == password :
        while True:
            #showing all the options
            print("""
                1 == balance
                2 == withdraw balance
                3 == deposit balance
                4 == exit
                """)
            
            try:
                option = int(input("enter your choice:"))
            except:
                print("Enter a valid choice")
            
            #for checking balance
            if option == 1:
                print("your balance is:", balance)
            if option == 2:
                withdrawal_amt = int(input("Enter your withdrawal amount:"))
                balance = balance - withdrawal_amt
                print("your account is debited with:", withdrawal_amt)
                print("your new balance is:", balance)

            if option ==3:
                deposit_amt = int(input("Enter your deposit amount:"))
                balance = balance + deposit_amt
                print("your account is credited with:", deposit_amt)
                print("your new balance is:", balance)

            if option == 4:
                break

    else:
        print("wrong pin")
        answer = int(input("To continue press 1:"))
        if answer ==1:
            continue
        else:
            break

print("Thanks for visitng")
