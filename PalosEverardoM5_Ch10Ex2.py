"""
Write a class named Car that has the following data attributes:
    __year_model (for the car’s year model)                             
    __make (for the make of the car)                             
    __speed (for the car’s current speed)                                                                                                      

The Car class should have an __init__ method that accepts the car’s year model and make as arguments. 
These values should be assigned to the object’s 
__year_model and __make data attributes.
It should also assign 0 to the __speed data attribute.

The class should also have the following methods:   
    The accelerate method should add 5 to the speed data attribute each time it is called.                                                                                  
    The brake method should subtract 5 from the speed data attribute each time it is called.
    The get_speed method should return the current speed.

Next, design a program that creates a Car object then calls the accelerate method five times. 
After each call to the accelerate method, get the current speed of the car and display it. 
Then call the brake method five times. 
After each call to the brake method, get the current speed of the car and display it.
"""

class Car:
    def __init__(self, year_model, make, speed)
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed


        