"""
    Write a class named Person with data attributes for a person’s name, address, and telephone number. 
    Next, write a class named Customer that is a subclass of the Person class. 
    The Customer class should have a data attribute for a customer number, 
    and a Boolean data attribute indicating whether the customer wishes to be on a mailing list. 
    Demonstrate an instance of the Customer class in a simple program.
"""

class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    # Accessor methods
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    # Mutator methods
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

