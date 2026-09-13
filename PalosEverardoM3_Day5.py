"""Make use of the random number feature in Python to simulate the rolling of a pair of dice.  
Get input from operator for the number of rolls and retrieve an optional seed number (zero to use the system clock).  

Encase this in a while loop to allow multiple runs.  
Experiment with two runs with no seed number, two runs with the same seed number and a run with a different seed number."""

import random

while True:
    num_rolls = int(input("Enter the number of rolls: "))
    seed = int(input("Enter a seed number (0 for system clock): "))
    
    if seed == 0:
        random.seed()
    else:
        random.seed(seed)
    
    print("Rolling the dice...")
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll: {die1} + {die2} = {die1 + die2}")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break