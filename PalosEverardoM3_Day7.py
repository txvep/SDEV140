"""Write a program that takes the number of times to roll two dice from the console.  
Do a tally of the result number (2 through 12) in an indexed list.  
When program completes this experiment, you will display the tallies from the list 
and use them to calculate the percent of times each number occurred. 

Additional item: Store the expected percent for each result number in a stable table 
and display these alongside the corresponding results of your experiments in your display. 
If you run two different experiments, one using a relatively small number (<500) and another with a large number (say a million),
you will see a demonstration of the law of large numbers:  
The larger your sample size, the closer to the theoretical probability you will get.

Hint: Use formatted print lines to make results professionally lined up."""

import random

dice_tallies = [0] * 11  # Index 0 corresponds to sum 2, index 10 corresponds to sum 12
expected_percentages = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]  # Expected percentages for sums 2 through 12

def get_num_rolls() -> int:
    while True:
        try:
            num_rolls = int(input("Enter the number of times to roll the dice: "))
            if num_rolls <= 0:
                print("Please enter a positive integer.")
                continue
            return num_rolls
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def roll_dice(num_rolls: int) -> list:
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        dice_tallies[total - 2] += 1  # Adjust index to match sum (2-12)
    return dice_tallies

def display_results(num_rolls: int, tallies: list) -> None:
    print(f"{'Sum':<5}{'Tally':<10}{'Percent':<10}{'Expected %':<16}")
    print("-" * 40)
    for i in range(11):
        sum_value = i + 2
        tally = tallies[i]
        percent = (tally / num_rolls) * 100 if num_rolls > 0 else 0
        expected_percent = expected_percentages[i]
        print(f"{sum_value:<5}{tally:<10}{percent:<10.2f}{expected_percent:>16.2f}")

def main() -> None:
    num_rolls = get_num_rolls()
    tallies = roll_dice(num_rolls)
    display_results(num_rolls, tallies)

if __name__ == "__main__":
    main()