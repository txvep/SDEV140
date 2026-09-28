"""
Write an Employee class that keeps data attributes for the following pieces of information:

Employee name

Employee Number

Next, write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes

Shift Number (1 day or 2 night)

Hourly Pay Rate

Write appropriate Accessor and Mutator methods for each class.

Once you have written the classes, write a program that creates an object of the ProductionWorker.
Use the accessor methods to print out the object's full state.
Then test the mutator methods doing an update of all attributes followed by a second print of the object's full revised state.
"""


class employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id


class productionWorker(employee):
    def __init__(self, name, id, shift, pay):
        super().__init__(name, id)
        self.__shift = shift
        self.__pay = pay

    # Accessor methods
    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay

    # Mutator methods
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay):
        self.__pay = pay


# Program to create a ProductionWorker object and test accessors/mutators
def main():
    worker = productionWorker("Everardo Palos", "1505", 1, 25.00)

    print("Original Employee state:")
    print(f"Name: {worker.get_name()}")
    print(f"ID: {worker.get_id()}")
    print(f"Shift: {worker.get_shift()}")
    print(f"Pay Rate: ${worker.get_pay_rate():.2f}")
    print(worker)

    worker.set_name("Everardo Palos")
    worker.set_id("2505")
    worker.set_shift(2)
    worker.set_pay_rate(28.50)

    print("\nRevised Employee state:")
    print(f"Name: {worker.get_name()}")
    print(f"ID: {worker.get_id()}")
    print(f"Shift: {worker.get_shift()}")
    print(f"Pay Rate: ${worker.get_pay_rate():.2f}")
    print(worker)

if __name__ == "__main__":
    main()