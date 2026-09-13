"""Programming Exercise #6 in Chapter 2 was the Sales Tax program. 
For that exercise, you were asked to write a program that calculates and displays the county and state sales tax on a purchase. 
If you have already written that program, redesign it so the subtasks are in functions. 
If you have not already written that program, write it using functions.


state_tax_rate = 0.05
county_tax_rate = 0.025

purchase_amount: float = float(input("Enter the amount of the purchase: "))
state_sales_tax: float = purchase_amount * state_tax_rate
county_sales_tax: float = purchase_amount * county_tax_rate
total_sales_tax = state_sales_tax + county_sales_tax
total_sale = purchase_amount + total_sales_tax

print(f"Amount of purchase: ${purchase_amount:.2f}")
print(f"State sales tax: ${state_sales_tax:.2f}")
print(f"County sales tax: ${county_sales_tax:.2f}")
print(f"Total sales tax: ${total_sales_tax:.2f}")
print(f"Total of the sale: ${total_sale:.2f}")
"""

state_tax_rate = 0.05
county_tax_rate = 0.025

def get_purchase_amount():
    return float(input("Enter the amount of the purchase: "))

def calculate_taxes(purchase_amount: float) -> tuple[float, float, float, float]:
    state_sales_tax = purchase_amount * state_tax_rate
    county_sales_tax = purchase_amount * county_tax_rate
    total_sales_tax = state_sales_tax + county_sales_tax
    total_sale = purchase_amount + total_sales_tax
    return state_sales_tax, county_sales_tax, total_sales_tax, total_sale

def display_results(purchase_amount: float, state_sales_tax: float, county_sales_tax: float, total_sales_tax: float, total_sale: float):
    print(f"Amount of purchase: ${purchase_amount:.2f}")
    print(f"State sales tax: ${state_sales_tax:.2f}")
    print(f"County sales tax: ${county_sales_tax:.2f}")
    print(f"Total sales tax: ${total_sales_tax:.2f}")
    print(f"Total of the sale: ${total_sale:.2f}")
    print("Everardo Palos")

def main():
    purchase_amount = get_purchase_amount()
    state_sales_tax, county_sales_tax, total_sales_tax, total_sale = calculate_taxes(purchase_amount)
    display_results(purchase_amount, state_sales_tax, county_sales_tax, total_sales_tax, total_sale)


if __name__ == "__main__":
    main()
