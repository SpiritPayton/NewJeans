"""Menu Program for the Takeaway Business
"""

import easygui

menu_choice = easygui.buttonbox(f"Ayo welcome to Thee Terrific Takeaways, here's the menu:", "Menu")

# create a list of combo meals
combo_meals = ["Combo Value: Beef burger, Fries, Fizzy drink",
               "Combo Cheezy: Cheeseburger, Fries, Fizzy drink",
               "Combo Super: Cheeseburger, Large fries, Smoothie"]

print(combo_meals)
