"""
6.Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
Write a program that calculates the average of all the numbers stored in the file.

9.Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.
"""




def calculate_average_from_file(filename: str) -> float | None:
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                 number = int(line.strip())
                 numbers.append(number)
                
        if len(numbers) == 0:
            print(f"The file '{filename}' is empty. No numbers to calculate the average.")
            return None
        else:
            average = sum(numbers) / len(numbers)
            return average
    except IOError:
        print(f"Error: Could not open or read the file '{filename}'.")
        return None
    except ValueError:
        print(f"Error: One or more items in the file '{filename}' could not be converted to an integer.")
        return None


def main() -> None:
    filename: str = "numbers.txt"
    average: float | None = calculate_average_from_file(filename)
    if average is not None:
        print(f"The average of the numbers in the file '{filename}' is: {average}")
    
if __name__ == "__main__":
    main()

