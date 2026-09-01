"""
    You have a group of friends coming to visit for your high school reunion, 
    and you want to take them out to eat at a local restaurant.
      You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:
        Joe’s Gourmet Burgers – Vegetarian: No, Vegan: No, Gluten-Free: No
        Main Street Pizza Company – Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
        Corner Café – Vegetarian: Yes, Vegan: Yes, Gluten-Free: No
        Mama’s Fine Italian – Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
        the Chef’s Kitchen – Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
      Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, 
      to which then displays only the restaurants to which you may take the group. 
      Here is an example of the program’s output:
        is anyone in your party a vegetarian? (yes/no) yes
        is anyone in your party a vegan? (yes/no) no
        is anyone in your party gluten-free? (yes/no) yes
        here are your restaurant choices:
        Main Street Pizza Company
        Corner Café
        the Chef’s Kitchen
      Here is another example of the program’s output:
        is anyone in your party a vegetarian? (yes/no) no
        is anyone in your party a vegan? (yes/no) no
        is anyone in your party gluten-free? (yes/no) no
        here are your restaurant choices:
        Corner Café
        The Chef’s Kitchen

"""


def get_restaurant_choices():
    # Define the restaurant options and their dietary restrictions
    restaurant_options = {
        "Joe\'s Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten_free": False},
        "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten_free": True},
        "Corner Café": {"vegetarian": True, "vegan": True, "gluten_free": False},
        "Mama\'s Fine Italian": {"vegetarian": True, "vegan": False, "gluten_free": True},
        "the Chef\'s Kitchen": {"vegetarian": True, "vegan": True, "gluten_free": True}
    }

    # Get user input for dietary restrictions
vegetarian: str = str.lower(input("Is anyone in your party a vegetarian? (yes/no) "))
vegan: str = str.lower(input("Is anyone in your party a vegan? (yes/no) "))
gluten_free: str = str.lower(input("Is anyone in your party gluten-free? (yes/no) "))

    # Filter restaurants based on dietary restrictions
available_restaurants = restaurant_options

    if vegetarian == "yes":
        available_restaurants = {
            name: info for name, info in available_restaurants.items() if info["vegetarian"]
        }
    if vegan == "yes":
        available_restaurants = {
            name: info for name, info in available_restaurants.items() if info["vegan"]
        }
    if gluten_free == "yes":
        available_restaurants = {
            name: info for name, info in available_restaurants.items() if info["gluten_free"]
        }

    # Display the restaurant choices
    print("Here are your restaurant choices:")
    for restaurant in available_restaurants:
        print(restaurant)


# Call the function to run the program
get_restaurant_choices()


