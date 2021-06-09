#this project will roll the dice and produce two random number(integer)
#need to import random for any random number generation

import random

#declaring the min and max number while rolling a dice
min_number = 1
max_number = 6

diceroll_again = "yes"

#declaring loop
while diceroll_again == "yes" or diceroll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #1st random number from rolling the dice
    print(random.randint(min_number, max_number))
    
    #2nd random number from rolling the dice
    print(random.randint(min_number, max_number))
    
    #Asking user whether to roll dice again or not. Any input other than yes or y will end the loop
    diceroll_again = input("Roll the Dices Again?") 