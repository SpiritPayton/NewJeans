import easy_gui

while True:
    places_to_visit = easy_gui.enterbox("Enter the names of 5 places you would like to visit\nSeparate each place"
                                        "name with a comma", "Enter favouriite places")
    places = places_to_visit.split(",")
    if len(places) != 5:
        easy_gui.msgbox(f"Sorry but you can only enter the names of 5 places\n"
                        f"and you entered {len(places)} places.", "Too many places!!")

    else:
        break

for place in places:
    output = f"\n*    ".join(places)

easy_gui.msgbox(f"My bucket list: \n\n*    {output}", "Travel bucket list")
