"""A software company sells a package that retails for $99. 
Quantity discounts are given according to the following 
table:QuantityDiscount10–1910%20–4920%50–9930%100 or more40%
Write a program that asks the user to enter the number of packages purchased. 
The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
"""

# Software package discount calculator

PRICE_PER_PACKAGE:int = 99

packages_purchased = int(input("Enter the number of packages purchased: "))

discount_rate: float = 0.0

if packages_purchased < 10:
    discount_rate = 0.0
if 10 <= packages_purchased <= 19:
    discount_rate = 0.10
elif 20 <= packages_purchased <= 49:
    discount_rate = 0.20
elif 50 <= packages_purchased <= 99:
    discount_rate = 0.30
elif packages_purchased >= 100:
    discount_rate = 0.40

subtotal: float = packages_purchased * PRICE_PER_PACKAGE
discount_amount: float = subtotal * discount_rate
total: float = subtotal - discount_amount

print(f"Discount amount: ${discount_amount:,.2f}")
print(f"Total amount after discount: ${total:,.2f}")
print("Everardo Palos")
