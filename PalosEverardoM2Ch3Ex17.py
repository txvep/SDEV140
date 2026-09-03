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

    # Get user input for dietary restrictions
vegetarian: str = str.lower(input("Is anyone in your party a vegetarian? (yes/no) "))
vegan: str = str.lower(input("Is anyone in your party a vegan? (yes/no) "))
gluten_free: str = str.lower(input("Is anyone in your party gluten-free? (yes/no) "))

    # Display restaurant choices based on dietary restrictions
print("Here are your restaurant choices:")
if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
    print("The Chef's Kitchen")
if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("Main Street Pizza Company")
if vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("Corner Café")
if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("Mama's Fine Italian")

    