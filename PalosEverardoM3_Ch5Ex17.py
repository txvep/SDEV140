"""
1. A prime number is a number that is only evenly divisible by itself and 1. 

For example, the number 5 is prime because it can only be evenly divided by 1 and 5. 
The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.338                            

Write a Boolean function named is prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. 
Use the function in a program that prompts the user to enter a number then displays a message indicating whether the number is prime.

2. This exercise assumes that you have already written the is_prime function in Programming Exercise 16. 
Write another program that displays all of the prime numbers from 1 to 100. 
The program should have a loop that calls the  function.
"""

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print("Prime numbers from 1 to 100:")

for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")

print()
print("Everardo Palos")