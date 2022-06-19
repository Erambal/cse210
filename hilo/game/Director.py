from game.Card import Card
import random

# The director will control the entirety of the game.
class Director:
# This will initialize the game
    def __init__(self):
        self.is_playing = True
        self.card = Card()

# This will gather the card number from Card.py
    def get_inputs(self):
        self.card.get_card_number()

# This will gather the information for the gameplay
    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates()
            self.continue_playing()

# This will keep track of scores and user input
    def do_updates(self):
        return self.card.points()

# This will give information to start_game and the user to know the card number
    def do_outputs(self):
        self.card.get_card_number()
        print(f"\nThis card is: {self.card.card_number}")

# This will ask the user to continue the game
    def continue_playing(self):
        continue_playing = input("Play again? [y/n]")
        if continue_playing == "y":
            self.is_playing = True
        elif continue_playing == "n":
            self.is_playing = False
            print(f"\nGame Over")