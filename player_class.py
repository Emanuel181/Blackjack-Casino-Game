import validations
import base_class

class Player(base_class.GenericPlayer):
    def __init__(self, deck, name, chips):
        base_class.GenericPlayer.__init__(self, deck, name, chips)

    def get_deck_sum(self):
        sum = 0
        for card in self.deck:
            sum += card.rank
        return sum

    def get_sum_except_index(self, index):
        sum = 0
        for i in range(len(self.deck)):
            if i != index:
                sum += self.deck[index].rank
        return sum

    def check_for_ace(self):
        for ind in range(len(self.deck)):
            if isinstance(self.deck[ind].rank, list):
                print('\n\t\t\t\t\t\t\t\tYou have an Ace.\n\t\t\t\t\t\t\t\tYou must choose it\'s value')
                print('\t\t\t\t\t\t\t\tChoose between 1 and 11')
                number = validations.validate_for_ace()
                if number == 1:
                    self.deck[ind].rank = 1
                else:
                    self.deck[ind].rank = 11

