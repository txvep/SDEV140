"""
12. Population
Write a program that predicts the approximate size of a population of organisms.
The application should prompt the user to enter the starting number of organisms, the average
daily population increase (as a percentage), and the number of days the organisms will be
left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:

Day Approximate Population
2
2.6
3.38
4.394
5.7122
7.42586
9.653619
12.5497
16.31462
21.209
    """


organism_input: str = input("Enter the starting number of organisms: ")
while organism_input.isdigit() == False or int(organism_input) < 1:
    print("Please enter a valid starting number of organisms (must be greater than 0): ")
    organism_input = input("Enter the starting number of organisms: ")

start_num_organisms: int = int(organism_input)

avg_daily_increase_input: str = input("Enter the average daily population increase (as a percentage): ")
while True:
    try:
        while avg_daily_increase_input.isdigit() == False and int(avg_daily_increase_input) < 1:
            print("Please enter a valid average daily population increase (must be greater than 0): ")
            avg_daily_increase_input = input("Enter the average daily population increase (as a percentage): ")
        break   
    except ValueError:
        print("Invalid input. Please enter a valid number.")

avg_daily_increase: float = 1 + int(avg_daily_increase_input)/100

num_days_input: str = input("Enter the number of days the organisms will be left to multiply: ")
while num_days_input.isdigit() == False and int(num_days_input) < 1:
    print("Please enter a valid number of days (must be greater than 0): ")
    num_days_input = input("Enter the number of days the organisms will be left to multiply: ")

num_days: int = int(num_days_input)

print("Day Approximate Population")
for day_num in range(num_days):
    print(day_num+1, (day_num * avg_daily_increase))
