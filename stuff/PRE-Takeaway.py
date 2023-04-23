"""Menu Program for the Takeaway Business by Miya for a friend known as "Ice Spice"
who is starting a restaurant which may or may not be selling rotten and slimy burgers.....
"""

# this is in fact the least important line of code in my program
import easygui


# you here with iceeee spiceeee
class Icespice:
    def __init__(self, name):
        self.name = name

    def search(self):
        # if the name done be cancel return none
        if self.name == "Cancel":
            return
        # find the combo from she in ha mood based on the name
        combo = menu_log[self.name]
        # return the combo, formatted string, and name
        return [combo, f"Babygirl you picked Ice Spice's special {self.name} Meal which contains: "
                       f"{arr_format(multiple_collapse(combo))}", self.name]

    def add(self):
        # if the name is in list_of_combos and the user don't not unwish to overwrite it, return None
        if self.name in list_of_combos and not easygui.ynbox(f"{self.name} is already a combo?!??!\n"
                                                             f"Do you wanna to overwrite this, babygirl?"):
            return
        # create an empty list for the new combo
        new_combo_items = []
        # while loop to add items to icespice's latest combo meal
        while True:
            # prompt thee user to choose a food item from list_of_food
            food_choice = easygui.choicebox("Choose food item:", choices=list_of_food)
            # if user chooses to continue or cancels........ spontaneously combust.
            if food_choice in ("Continue", None):
                break
            # prompt user to enter the amount of the selected food item they want to add to the new combo
            amount = easygui.integerbox(f"How many {food_choice}(s)?")
            # if user cancels or enters a negative amount, continue the loop
            if amount in (None, "") or amount < 0:
                continue
            # if the user is stupid and chose something not in dict_of_foods, die
            if dict_of_foods[food_choice] is None:
                break
            # add the selected food item to the new combo the number of times miss ice spice specified
            for i in range(amount):
                new_combo_items.append(food_choice)
        # if new_combo_items is not empty, return the new combo with its name
        return {self.name: new_combo_items} if new_combo_items else "x Nun Added x"


def price(array, reference):
    # return the sum of the values in reference for each item in array, round to 2 dp
    return round(sum(reference[item] for item in array), 2)


def arr_format(array, format_option="list", message=""):
    # if format_option is "list", return a formatted string with each item in the array on a new line
    if format_option == "list":
        return message + "\n" + "\n".join(f" -\t{array[items]}" for items in range(len(array)-1)) + f" -\t{array[-1]}"
    # if format_option is "line", return a formatted string with each item in the array,
    # separated by commas and "and" for the last item
    elif format_option == "line":
        return message + ", ".join(array[:-1]) + f" and {array[-1]}."


def multiple_collapse(array, resultant=list):
    # make a dictionary of the number of occurrences of each item in the array
    organised = {}
    # Create a list with the formatted string of each item and its count
    format_list = []
    for item in set(array):
        format_list.append(f"{item} x{array.count(item)}")
        organised.update({item: array.count(item)})
    # If resultant is "list", return format_list; otherwise, return organised
    return format_list if resultant == list else organised


# dictionary of the foods available
dict_of_foods = {
    "Continue": None,
    "Beef Burger": 5.69,
    "Cheeseburger": 6.69,
    "Regular Fries": 1,
    "Large Fries": 2,
    "Regular Drink": 1,
    "Large Drink": 2,
    "Smoothie": 2
}
menu_log = {
    "VALUE": ["Beef Burger", "Regular Fries", "Regular Drink"],
    "CHEESY": ["Cheeseburger", "Regular Fries", "Regular Drink"],
    "SUPER": ["Cheeseburger", "Large Fries", "Smoothie"]
}
list_of_combos = list(menu_log.keys())
list_of_food = list(dict_of_foods.keys())

while True:
    option = easygui.buttonbox("Ya here wit' IceSpice. I got big beefy burgers for sale, now how would "
                               "you want me ta serve you today? Grrrrah."
                               "", choices=["Search", "Add", "Combos", "Explode"])
    # if they wanna search
    if option == "Search":
        # create an Icespice object and call its search method to find a combo
        details = Icespice(easygui.choicebox(f"What combo is you searching for bestie boo?"
                                             f"", choices=["Cancel"]+list_of_combos)).search()

        # if a combo is found show details & price
        if details:
            easygui.msgbox(details[1] + f"\nWith a total "
                                        f"price of: ${price(menu_log[details[2].upper()], dict_of_foods)}")

    # if user presses add
    elif option == "Add":
        # create an icespice object and call its add method to add a new combo
        new_entry = Icespice(easygui.enterbox("What you wanna name the combo girlypop?").upper()).add()

        # if a new combo is added, print a message to notify icespice
        # (i just realised ice spice is the program and also the person using the program... hmm..)
        if isinstance(new_entry, dict):
            print("Added New Item(s)")
        # do the same if they don't add a new combo
        elif new_entry == "Nothing Added":
            print("Ice Spice ain't added new items babe")

    # don't be shy let ice spice see her combos!!!
    elif option == "Combos":
        easygui.msgbox(menu_log)

    # if miss gurl decides to press explode break out of the loop and ELIMINATE the program
    else:
        break
