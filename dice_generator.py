## Alexander Rudolph

#import Image
import random
import math

## Libraries for making bar graphs
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
##

#image = Image.open('09021001.png')
#image.show()

D4 = [1,2,3,4]
D6 = [1,2,3,4,5,6]
D8 = [1,2,3,4,5,6,7,8]
D12 = [1,2,3,4,5,6,7,8,9,10,11,12]
#D20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
DICE_TO_ROLL = [] ## Add a dice each time it's entered
DICE_TO_RECORD = [] ## Record each outcome of the dice
lVal = 0

# defs
def rollDice(diceList):
    rollTotal = 0
    i = 0
    for x in DICE_TO_ROLL:
        rollTotal += DICE_TO_ROLL[i][random.randint(0, len(DICE_TO_ROLL[i])-1)]
        #print(DICE_TO_ROLL[i])
        i += 1
    return rollTotal

print("Enter a dice type: ")
print("The available dice are: D4, D6, D8, D12")
print("Make sure to enter 2 or more dice.")
print("When you are finished adding dice, enter \"done\"")
user_input = ""

## Begin dice adding loop
count = 0
while not (user_input.lower() == "done"):
    ## accpetable input types
    ## Ask for number of dice
    ##Reject incorrect input
    user_input = raw_input()
    #print(str(user_input))
    print("Please enter a die to roll: ")

    if user_input.lower() == "d4":
        ## Add to the DICE_TO_ROLL array
        DICE_TO_ROLL.append(D4)
        lVal += D4[len(D4)-1]
        #print(lVal)
        ## print(DICE_TO_ROLL[count])
        count += 1

    elif user_input.lower() == "d6":
        DICE_TO_ROLL.append(D6)
        lVal += D6[len(D6)-1]
        count += 1

    elif user_input.lower() == "d8":
        DICE_TO_ROLL.append(D8)
        lVal += D8[len(D8)-1]
        count += 1

    elif user_input.lower() == "d12":
        DICE_TO_ROLL.append(D12)
        lVal += D12[len(D12)-1]
        count += 1

    elif user_input.lower() == "done":
        break;
    else:
        print("Wrong input!")
        break;
    ##print(count)
## End dice adding loop

print("How many times would you like to roll the dice?")
roll_input = int(raw_input())

roll_count = 0
roll_sum = 0
while(roll_count < roll_input):
    roll_sum = rollDice(DICE_TO_ROLL)
    DICE_TO_RECORD.append(roll_sum)
    roll_count += 1
    #print(roll_count)
    #print(roll_sum)

#print("Displaying results of dice rolls: ")
#for i in DICE_TO_RECORD:
#    print(i),

###
###
def printGraph(diceList):
    diceList = DICE_TO_ROLL
    objects = ()
    temp = len(DICE_TO_ROLL)

    for i in range(0, lVal-temp+1):
        objects = objects + (i+temp,)

        y_pos = np.arange(len(objects))

        #performance = [0,0,0,0,0,0,0,0,0,0,0]
    performance = []
    for i in range(0, lVal-temp+1):
        performance.append(0)

        #  Check dice total and add it to the graph
    for i in DICE_TO_RECORD:
        performance[i-temp] += 1

        ## Display the output of the dice rolls
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Value')
        plt.title('Dice roll totals')

    plt.show()
    
###
###

printGraph(DICE_TO_ROLL)


