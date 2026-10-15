"""
Next, design a program that creates a Car object then calls the accelerate method five times. 
After each call to the accelerate method, get the current speed of the car and display it. 
Then call the brake method five times. 
After each call to the brake method, get the current speed of the car and display it.
"""
from Car import Car

def main():
    # Create a Car object
    my_car = Car(2022, "Toyota")

    # Accelerate the car five times and display the speed
    print("Accelerating:")
    for _ in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()} mph")

    # Brake the car five times and display the speed
    print("\nBraking:")
    for _ in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()} mph")

if __name__ == "__main__":
    main()
    

    


        