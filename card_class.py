import constants


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = constants.values[rank]
        self.str_rank = rank

