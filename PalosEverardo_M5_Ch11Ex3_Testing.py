"""Testing the Customer class"""



# Create an instance of the Customer class
from PalosEverardoM5_Ch11Ex3 import Customer


customer1 = Customer("David Boom", "123 Main St", "555-1234", 1001, True)
customer2 = Customer("Alec Smith", "606 Lake St", "555-5678", 1002, False)
customer3 = Customer("Alice Johnson", "509 Winter Ave", "555-9012", 1003, True)

# Display the customer's information
print("Customer Information:")
print(f"Name: {customer1.get_name()}")
print(f"Address: {customer1.get_address()}")
print(f"Phone: {customer1.get_phone()}")
print(f"Customer Number: {customer1.get_customer_number()}")
print(f"Mailing List: {customer1.get_mailing_list()}")
print()
print(f"Name: {customer2.get_name()}")
print(f"Address: {customer2.get_address()}")
print(f"Phone: {customer2.get_phone()}")
print(f"Customer Number: {customer2.get_customer_number()}")
print(f"Mailing List: {customer2.get_mailing_list()}")
print()
print(f"Name: {customer3.get_name()}")
print(f"Address: {customer3.get_address()}")
print(f"Phone: {customer3.get_phone()}")
print(f"Customer Number: {customer3.get_customer_number()}")
print(f"Mailing List: {customer3.get_mailing_list()}")

