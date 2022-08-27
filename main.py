import start_game
import time
import validations

if __name__ == '__main__':
    while True:
        start_game.start()
        print('\n\n\t\t\t\t   -------------------♔-------------------')
        print('\n\t\t\t\t\t\tDo you want to play again?\n\n\t\t\t\t\t\t\t\t1 - yes\n\n\t\t\t\t\t\t\t\t0 - no\n')
        play_again = validations.validate_reload_game()
        print('\n\t\t\t\t   -------------------♔-------------------')
        time.sleep(2)
        if play_again == '0':
            print('\t\t\t\t\t\t\t\tGoodbye 😔\n')
            break
