"""
A) Write a program that writes a series of random numbers.  
Number Range 1 to 500 integers.  Get user prompt for the total number to generate and write.

B) For the above created file read in and display all the numbers. 
 Accumulate the total number as well as the sum of numbers.  Display these as well as the average at the end."""

import random

num_range_min: int = 1
num_range_max: int = 500

print("Random Number Generator and Statistics Program")
total_numbers = int(input("Enter the total number of random numbers to generate: "))

with open("random_numbers.txt", "w") as f:
    for _ in range(total_numbers):
        number = random.randint(num_range_min, num_range_max)
        f.write(str(number) + "\n")

print("Random numbers written to file.")

with open("random_numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]
    total = len(numbers)
    sum_numbers = sum(numbers)
    average = sum_numbers / total if total > 0 else 0

print(f"Total numbers: {total}")
print(f"Sum of numbers: {sum_numbers}")
print(f"Average: {average}")

