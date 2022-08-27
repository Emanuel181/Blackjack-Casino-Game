"""
Game logic is here
"""

import time
import random
import deck_class
import player_class
import get_infos
import dealer_class
import welcome
import validations


def final_check(dealer, player_1):
    """
    check for tie or a winner
    """

    if 21 >= dealer.get_deck_sum() > player_1.get_deck_sum():
        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
        print('\n\t\t\t\t\t\t\t\tDealer won')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

    elif 21 >= player_1.get_deck_sum() > dealer.get_deck_sum():
        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
        print(f'\n\t\t\t\t\t\t\t\t{player_1.name} won')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

    else:
        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
        print('\n\t\t\t\t\t\t\t\tTie')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')


def start():
    """
    driver function
    """

    pack = deck_class.Pack()

    welcome.welcome_screen()

    name = validations.validation_for_name()
    print('\t\t\t\t\t\tHow many chips you want to bet?')
    print('\t\t\t\t\t\t5€ = 1 chip')
    bet = validations.validate_int()
    print(f'\t\t\t\t\t\tYou have {bet} chips assigned')
    player_1 = player_class.Player([], name, bet)

    print('\n\t\t\t\t\t\tEnter your name: ', end='')
    for i in 'Dealer(It\'s me, your computer 🙂)':
        print(i, end='')
        time.sleep(0.22)

    print('\n\t\t\t\t\t\tHow many chips you want to bet?')
    print('\t\t\t\t\t\t5€ = 1 chip')
    print('\t\t\t\t\t\tEnter your amount: ', end='')
    bet = random.randrange(5, 3000, 5)
    for token in f'I will bet {bet}':
        print(token, end='')
        time.sleep(0.2)

    print(f'\n\t\t\t\t\t\tYou have {bet} chips assigned\n')
    dealer = dealer_class.Dealer([], 'Dealer', bet)
    time.sleep(2)

    player_1.deck.append(pack.deck.pop())
    dealer.deck.append(pack.deck.pop())

    player_1.deck.append(pack.deck.pop())
    dealer.deck.append(pack.deck.pop())

    stop_game = 'no'

    while True:

        get_infos.get_infos_player(player_1)
        player_1.check_for_ace()
        print(f'\n\t\t\t\t\t\t\t\tTotal: {player_1.get_deck_sum()}')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')


        get_infos.get_infos_player(dealer, 1)
        print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum(1)}')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

        if player_1.get_deck_sum() > 21:
            get_infos.get_infos_player(dealer)
            print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum()}')
            print(f'\n\t\t\t\t\t\t\t\t{player_1.name} has BUSTED')
            print('\n\t\t\t\t\t\t\t\tDealer has won')
            print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
            break

        print(f'\n\n\t\t\t\t   -------------------♔-------------------\
        \n\t\t\t\t\t\t\t{player_1.name}\'s turn:\n\n\t\t\t\t\t\t\t\t1 - HIT\
        \n\n\t\t\t\t\t\t\t\t2 - STAY\n')
        player_choose = str(validations.validate_1_or_2())
        print('\n\t\t\t\t   -------------------♔-------------------')

        if player_choose == '1':
            player_1.deck.append(pack.deck.pop())
            get_infos.get_infos_player(dealer, 1)
            print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum(1)}')
            print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

            get_infos.get_infos_player(player_1)
            player_1.check_for_ace()
            print(f'\n\t\t\t\t\t\t\t\tTotal: {player_1.get_deck_sum()}')
            print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

            if player_1.get_deck_sum() > 21:
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙\n')
                print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                print(f'\n\t\t\t\t\t\t\t\t{player_1.name} has BUSTED!')
                print('\n\t\t\t\t\t\t\t\tDealer won')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                break

        else:
            print('\n\n\t\t\t\t   -------------------♔-------------------')
            print('\n\t\t\t\t\t\t\t     Dealer\'s turn\n')
            print('\n\t\t\t\t   -------------------♔-------------------')

            time.sleep(2.5)

            get_infos.get_infos_player(player_1)
            print(f'\n\t\t\t\t\t\t\t\tTotal: {player_1.get_deck_sum()}')
            print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

            time.sleep(2.5)
            get_infos.get_infos_player(dealer)
            dealer.check_for_ace()
            print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum()}')
            print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

            while dealer.get_deck_sum() < 17:
                print('\n\n\t\t\t\t   -------------------♔-------------------')
                print('\n\t\t\t\t\t\t\t\tDealer turn:\n\n\t\t\t\t\t\t\t\t1-HIT\
                \n\n\t\t\t\t\t\t\t\t2-STAY\n')
                print('\n\t\t\t\t\t\t\t\tChoose: 1\n')
                print('\n\t\t\t\t   -------------------♔-------------------')

                dealer.deck.append(pack.deck.pop())
                time.sleep(2.5)
                get_infos.get_infos_player(player_1)
                print(f'\n\t\t\t\t\t\t\t\tTotal: {player_1.get_deck_sum()}')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

                time.sleep(2.5)
                get_infos.get_infos_player(dealer)
                dealer.check_for_ace()
                print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum()}')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

            if dealer.get_deck_sum() > 21:
                print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                print(f'\n\t\t\t\t\t\t\t\t{dealer.name} has BUSTED!')
                print(f'\n\t\t\t\t\t\t\t\t{player_1.name} won')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                break

            if dealer.get_deck_sum() == 21 and player_1.get_deck_sum() == 21:
                print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                print('\n\t\t\t\t\t\t\t\tTie')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                break

            if dealer.get_deck_sum() > player_1.get_deck_sum():
                print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                print('\n\t\t\t\t\t\t\t\tDealer won')
                print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                break

            if dealer.get_deck_sum() <= 19:
                print('\n\n\t\t\t\t   -------------------♔-------------------')
                print('\n\t\t\t\t\t\t\t\tDealer turn:\n\n\t\t\t\t\t\t\t\t1-HIT\
                \n\n\t\t\t\t\t\t\t\t2-STAY\n')

                hit = random.randint(0, 1)
                if dealer.get_deck_sum() == 19:
                    hit = random.randint(0, 1)

                print(f'\n\n\t\t\t\t\t\t\t\tChoose: {hit}')
                print('\n\t\t\t\t   -------------------♔-------------------')
                while hit:
                    dealer.deck.append(pack.deck.pop())

                    time.sleep(2.5)
                    get_infos.get_infos_player(player_1)
                    print(f'\n\t\t\t\t\t\t\t\tTotal: {player_1.get_deck_sum()}')
                    print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

                    time.sleep(2.5)
                    get_infos.get_infos_player(dealer)
                    dealer.check_for_ace()
                    print(f'\n\t\t\t\t\t\t\t\tTotal: {dealer.get_deck_sum()}')
                    print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

                    if dealer.get_deck_sum() > 21:
                        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                        print(f'\n\t\t\t\t\t\t\t\t{dealer.name} has BUSTED!')
                        print(f'\n\t\t\t\t\t\t\t\t{player_1.name} won')
                        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                        stop_game = 'yes'
                        break

                    if dealer.get_deck_sum() == 21 and player_1.get_deck_sum() == 21:
                        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                        print('\n\t\t\t\t\t\t\t\tTie')
                        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                        stop_game = 'yes'
                        break

                    if dealer.get_deck_sum() == 21:
                        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                        print('\n\t\t\t\t\t\t\t\tDealer won')
                        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                        stop_game = 'yes'
                        break

                    if dealer.get_deck_sum() > player_1.get_deck_sum():
                        print('\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑')
                        print('\n\t\t\t\t\t\t\t\tDealer won')
                        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')
                        stop_game = 'yes'
                        break

                if stop_game == 'yes':
                    break

                final_check(dealer, player_1)
                break

            else:
                final_check(dealer, player_1)
                break
