"""Design a program that asks the user to enter a store’s sales for each day of the week. 
The amounts should be stored in a list. 
Use a loop to calculate the total sales for the week and display the result."""

def main():

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']  

    sales = []  

    for day in days:
        while True:
            try:
                amount = float(input(f"Enter the sales for {day}: $"))
                if amount < 0:
                    print("Error: Sales cannot be negative. Please try again.")
                else:
                    sales.append(amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = 0
    for amount in sales: 
        total += amount

    print()
    print(f"\nTotal sales for the week: ${total:,.2f}")

if __name__ == "__main__":
    main()
