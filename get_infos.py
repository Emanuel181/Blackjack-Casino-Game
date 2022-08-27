import validations


def get_infos_player(player, index=0):
    print(f'\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑\
                       \n\t\t\t\t\t\t\t     {player.name} has:')
    if player.name == 'Dealer' and index == 1:
        print('\n\t\t\t\t\t\t\t\t-> Hidden card')
    for ind in range(index, len(player.deck)):
        if isinstance(player.deck[ind].rank, list):
            print(f'\n\t\t\t\t\t\t\t\t-> 11 of {player.deck[ind].suit}')
        else:
            print(f'\n\t\t\t\t\t\t\t\t-> {player.deck[ind].rank} of {player.deck[ind].suit}')


