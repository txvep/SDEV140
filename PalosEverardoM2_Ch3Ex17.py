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


Restaurant_list = { "Main Street Pizza Company": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "Yes"},
                   "Corner Café": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "No"},
                   "Mama's Fine Italian": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "Yes"},
                   "The Chef's Kitchen": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "Yes"},
                   "Joe's Gourmet Burgers": {"Vegetarian": "No", "Vegan": "No", "Gluten-Free": "No"}}


# Get user input for dietary restrictions
vegetarian: str = input("Is anyone in your party a vegetarian? (Yes/No) ").lower()
vegan: str = input("Is anyone in your party a vegan? (Yes/No) ").lower()
gluten_free: str = input("Is anyone in your party gluten-free? (Yes/No) ").lower()

requirements = []
if vegetarian == "yes":
    requirements.append("Vegetarian")
if vegan == "yes":
    requirements.append("Vegan")
if gluten_free == "yes":
    requirements.append("Gluten-Free")

# Find restaurants that satisfy every required restriction
matches = []
for name, options in Restaurant_list.items():
    if all(options[req] == "Yes" for req in requirements):
        matches.append(name)

# Display results
print("Here are your restaurant choices:")
if matches:
    for restaurant in matches:
        print(restaurant)
else:
    print("Sorry, no restaurants match all of those needs.")

print("Everardo Palos")




    