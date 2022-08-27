import random
import base_class


class Dealer(base_class.GenericPlayer):
    def __init__(self, deck, name, chips):
        base_class.GenericPlayer.__init__(self, deck, name, chips)

    def get_deck_sum(self, index=0):
        for ind in range(index, len(self.deck)):
            if isinstance(self.deck[ind].rank, list):
                return 'Unknow'

        sum = 0
        for ind in range(index, len(self.deck)):
            sum += self.deck[ind].rank
        return sum

    def get_sum_except_ace(self):
        sum = 0
        for i in range(len(self.deck)):
            if not isinstance(self.deck[i].rank, list):
                sum += self.deck[i].rank
        return sum

    def check_for_ace(self):
        for ind in range(len(self.deck)):
            if isinstance(self.deck[ind].rank, list):
                print('\n\t\t\t\t\t\t\t\tYou have an Ace.\n\t\t\t\t\t\t\t\tYou must choose it\'s value')
                print('\t\t\t\t\t\t\t\tChoose between 1 and 11')
                rand = random.randint(0, 1)
                if (self.get_sum_except_ace() + 11 == 21) or (self.get_sum_except_ace() + 11 <= 21 and rand == 1):
                    print('\t\t\t\t\t\t\t\tChoose: 11')
                    self.deck[ind].rank = 11
                else:
                    print('\t\t\t\t\t\t\t\tChoose: 1')
                    self.deck[ind].rank = 1
