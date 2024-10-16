# Dice Roll
# Made By Gabriel Tachie Menson
# Made In Visual Studio Code
# Started: 2024 - October - 15
# Finished: 2024 - October - 15

# Import the random plugin.
import random

print("How many sides do you want your die to have?")
sides = int(input("Enter in a number in number form. Press enter to continue."))
print(" ")

# This is the coin flip. The code choose numder from 1 to the number selectced by the user randomly.
# This is beacue this dice in this situation has as many sides has the user wants.
dice = random.randint(1,sides)
dice = str(dice)

print("Your die landed on " + dice + ".")