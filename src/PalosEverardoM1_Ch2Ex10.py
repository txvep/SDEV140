"""
A cookie recipe calls for the following ingredients:   
    1.5 cups of sugar  1 cup of butter  2.75 cups of flour
    The recipe produces 48 cookies with this amount of the ingredients. 
Write a program that asks the user how many cookies he or she wants to make, 
then displays the number of cups of each ingredient needed for the specified number of cookies.
    """

recipe = {
    "sugar": 1.5,
    "butter": 1.0,
    "flour": 2.75
}

cookies_wanted = int(input("How many cookies do you want to make? "))

sugar_needed = (recipe["sugar"] / 48) * cookies_wanted
butter_needed = (recipe["butter"] / 48) * cookies_wanted
flour_needed = (recipe["flour"] / 48) * cookies_wanted

print(f"Ingredients needed for {cookies_wanted} cookies:")
print(f"Sugar: {sugar_needed:.2f} cups")
print(f"Butter: {butter_needed:.2f} cups")
print(f"Flour: {flour_needed:.2f} cups")
print('Everardo Palos')