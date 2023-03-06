import easy_gui
import random

while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)
    play_again = easy_gui.buttonbox("Welcome to Rock Paper Scissors\n\n"
                                    "Rock beats scissors\n"
                                    "Scissors beats peppa\n"
                                    "peppa beats wok\n"
                                    "do you want to play?\n",
                                    "welcome and rules", choices=["Yes", "No"])
    if play_again == "No":
        break
    else:
        player = easy_gui.buttonbox("Choose your weapon", "Choose weapon",
                                    choices=[weapons[0], weapons[1], weapons[2]])
