"""
Last month, Joe purchased some stock in Acme Software, Inc. 
Here are the details of the purchase:    The number of shares that Joe purchased was 2,000.  
When Joe purchased the stock, he paid $40.00 per share. 
 Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.
 Two weeks later, Joe sold the stock. 
Here are the details of the sale:    The number of shares that Joe sold was 2,000.  He sold the stock for $42.75 per share.  
He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
Write a program that displays the following information:    The amount of money Joe paid for the stock.  
The amount of commission Joe paid his broker when he bought the stock.  The amount for which Joe sold the stock.  
The amount of commission Joe paid his broker when he sold the stock.  
Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). 
If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.
"""

shares_purchased = 2000
purchase_price_per_share = 40.00
commission_rate = 0.03

purchase_amount = shares_purchased * purchase_price_per_share
purchase_commission = purchase_amount * commission_rate

shares_sold = 2000
sale_price_per_share = 42.75

sale_amount = shares_sold * sale_price_per_share
sale_commission = sale_amount * commission_rate

net_proceeds = sale_amount - sale_commission
total_cost = purchase_amount + purchase_commission
profit_or_loss = net_proceeds - total_cost

print(f"Amount paid for the stock: ${purchase_amount:.2f}")
print(f"Commission paid for buying the stock: ${purchase_commission:.2f}")
print(f"Amount received for selling the stock: ${sale_amount:.2f}")
print(f"Commission paid for selling the stock: ${sale_commission:.2f}")
print(f"Net proceeds from the sale: ${net_proceeds:.2f}")
print(f"Total cost of the investment: ${total_cost:.2f}")
print(f"Profit or loss: ${profit_or_loss:.2f}")
print('Everardo Palos')
