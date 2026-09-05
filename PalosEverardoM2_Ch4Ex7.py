"""
Write a program that calculates the amount of money a person would earn over a period of time 
if their salary is one penny the first day, two pennies the second day, and continues to double each day. 
The program should ask the user for the number of days. 
Display a table showing what the salary was for each day, then show the total pay at the end of the period. 
The output should be displayed in a dollar amount, not the number of pennies.
"""

money: float = 0.01
days: int = int(input("Enter the number of days you worked: "))
total_pay: float = 0.0

print("Day\tSalary")
for day in range(1, days + 1):
    print(f"{day}\t${money:.2f}")
    total_pay += money
    money *= 2

print(f"\nTotal pay: ${total_pay:.2f}")

print("Everardo Palos")
