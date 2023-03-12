"""Program to run a card game
"""
import random
import easy_gui

# Define the card numbers and suits
card_numbers = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


# Define a function to compare two cards
def compare_cards(player_card, computer_card):
    if card_numbers.index(player_card) > card_numbers.index(computer_card):
        return 'Player wins!'
    elif card_numbers.index(player_card) < card_numbers.index(computer_card):
        return 'Computer wins!'
    else:
        return 'It\'s a tie!'


# Define a function to display the results of the game and ask if the player wants to play again
def play_again():
    message = 'Player\'s card: {}\nComputer\'s card: {}\n\n{}'.format(player_card, computer_card, compare_cards(player_card, computer_card))
    title = 'Card Game'
    choices = ['Play again', 'Exit']
    reply = easy_gui.buttonbox(message, title, choices=choices)
    return reply == choices[0]


# Main game loop
play_game = True
while play_game:
    # Draw a card for the player and the computer
    player_card = random.choice(card_numbers)
    computer_card = random.choice(card_numbers)

    # Ask the computer who has the winning card
    message = 'The computer says that the {} of {} is higher than the {} of {}. Who has the winning card?'.format(
        computer_card, random.choice(card_suits), player_card, random.choice(card_suits))
    title = 'Card Game'
    choices = ['Player', 'Computer']
    reply = easy_gui.buttonbox(message, title, choices=choices)

    # Display the results and ask if the player wants to play again
    if reply == choices[0]:
        play_game = play_again()
    else:
        message = 'The computer wins! Better luck next time.'
        title = 'Card Game'
        choices = ['Play again', 'Exit']
        reply = easy_gui.buttonbox(message, title, choices=choices)
        play_game = reply == choices[0]
