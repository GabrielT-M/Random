# Coin Flip
# Made By Gabriel Tachie Menson
# Made In Visual Studio Code
# Started: 2024 - October - 15
# Finished: 2024 - October - 15


# Import the random plugin.
import random


# This is the coin flip. The code choose 1 or 2 randomly
coin = random.randint(1,2)


# If the result is 1 the coin is heads
if coin == 1:
    print("Your coin landed on heads.")

# If the result is 2 the coin is tails
if coin == 2: 
    print("Your coin landed on tails.")