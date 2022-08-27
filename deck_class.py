import constants
import card_class
import random


class Pack:
    def __init__(self):
        self.deck = [card_class.Card(rank, suit) for suit in constants.suits for rank in constants.ranks]
        random.shuffle(self.deck)
