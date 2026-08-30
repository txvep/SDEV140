''''''
Write a program that will ask the user to enter the amount of a purchase. 
The program should then compute the state and county sales tax. 
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
The program should display the amount of the purchase, the state sales tax, 
the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

- ask the user to enter the amount of a purchase
- compute the state sales tax (5% of the purchase amount)
- compute the county sales tax (2.5% of the purchase amount)
- calculate the total sales tax (state sales tax + county sales tax)
- calculate the total of the sale (purchase amount + total sales tax)
''''''
state_tax_rate = 0.05
county_tax_rate = 0.025

purchase_amount = float(input("Enter the amount of the purchase: "))
state_sales_tax = purchase_amount * state_tax_rate
county_sales_tax = purchase_amount * county_tax_rate
total_sales_tax = state_sales_tax + county_sales_tax
total_sale = purchase_amount + total_sales_tax

print(f"Amount of purchase: ${purchase_amount:.2f}")
print(f"State sales tax: ${state_sales_tax:.2f}")
print(f"County sales tax: ${county_sales_tax:.2f}")
print(f"Total sales tax: ${total_sales_tax:.2f}")
print(f"Total of the sale: ${total_sale:.2f}")


