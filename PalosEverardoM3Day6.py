"""
A) Write a program that writes a series of random numbers.  
Number Range 1 to 500 integers.  Get user prompt for the total number to generate and write.

B) For the above created file read in and display all the numbers. 
 Accumulate the total number as well as the sum of numbers.  Display these as well as the average at the end."""

import random

num_range_min: int = 1
num_range_max: int = 500

while True:
    try:
        total_numbers = int(input("Enter the total number of random numbers to generate: "))
        if total_numbers <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")
        raise SystemExit

with open("random_numbers.txt", "w") as f:
    for _ in range(total_numbers):
        numbers_input = random.randint(num_range_min, num_range_max)
        f.write(str(numbers_input) + "\n")

print("Random numbers written to file.")

with open("random_numbers.txt", "r") as f:
    numbers: list[int] = []
    for line in f:
        try:
            number = int(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Invalid number found in file: {line.strip()}")

display_list: list[int] = numbers
total: int = len(numbers)
sum_numbers: int = sum(numbers)
average: float = sum_numbers / total if total > 0 else 0

print("Random Numbers:")
for number in display_list:
    print(number)
print(f"Total numbers: {total}")
print(f"Sum of numbers: {sum_numbers}")
print(f"Average: {average}")