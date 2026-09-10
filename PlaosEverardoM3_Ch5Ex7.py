"""7. Random Number File WriterWrite a program that writes a series of random numbers to a file. 
Each random number should be in the range of 1 through 500. 
The application should let the user specify how many random numbers the file will hold.
8. Random Number File Reader                           
This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. 
Write another program that reads the random numbers from the file, displays the numbers, then displays the following data:    
The total of the numbers  The number of random numbers read from the file
"""

import random

min_number: int = 1
max_number: int = 500

def get_input() -> int:
    while True:
        try:
            count = int(input("Enter the number of random numbers to generate: "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def write_random_numbers_to_file(filename: str, count: int) -> None:
    with open(filename, 'w') as file:
        for _ in range(count):
            random_number: int = random.randint(min_number, max_number)
            file.write(f"{random_number}\n")


def read_random_numbers_from_file(filename: str) -> list:
    numbers: list =[]
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid number found in file: {line.strip()}")
    return numbers


def display_numbers_and_stats(numbers: list) -> None:
    total: int = sum(numbers)
    count: int = len(numbers)

    print("Random Numbers:")
    for number in numbers:
        print(number)

    print(f"Total of the numbers: {total}")
    print(f"Number of random numbers read from the file: {count}")

def main() -> None:
    filename: str = "random_numbers.txt"

    count: int = get_input()

    write_random_numbers_to_file(filename, count)

    numbers: list = read_random_numbers_from_file(filename)

    display_numbers_and_stats(numbers)

if __name__ == "__main__":
    main()
