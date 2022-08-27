import string


def validate_reload_game():
    play_again = input('\n\t\t\t\t\t\tEnter your option: ')
    if play_again in ['1', '0']:
        return play_again
    else:
        while True:
            print('\n\t\t\t\t\t\t\t\tYou must chose between 1(to play again)\n\t\t\t\t\t\t\t\tor 0(to stop the game)')
            play_again = input('\n\t\t\t\t\t\t\t\tEnter your option: ')
            if play_again in ['1' '0']:
                break
        return play_again


def validation_for_name():
    allowed = [letter for letter in string.ascii_uppercase + string.ascii_lowercase + ' ']
    name = input('\t\t\t\t\t\tEnter your name: ')
    ok = 1
    while len(name) < 3 or ok == 0:
        print('\t\t\t\t\t\tSuch a short name doesn\'t exist')
        name = input('\t\t\t\t\t\tEnter your name: ')

        cnt = 0
        for i in name:
            if i == ' ':
                cnt += 1

        if cnt != len(name):
            ok = 1

    while True:
        ok = 1
        for letter in name:
            if letter not in allowed:
                print('\t\t\t\t\t\tName can only have letters and spaces. Try again.')
                ok = 0
                break
        if ok:
            return name
        name = input('\t\t\t\t\t\tEnter your name: ')


def validate_int():
    number = input('\t\t\t\t\t\tEnter number: ')
    if not number.isnumeric():
        while True:
            print('\t\t\t\t\t\tThis is not a number')
            number = input('\t\t\t\t\t\tEnter number: ')
            if number.isnumeric():
                return int(number)
    return int(number)


def validate_1_or_2():
    number = input('\t\t\t\t\t\tEnter number: ')
    if number not in ['1', '2']:
        while True:
            print('\t\t\t\t\t\tThis is not a valid number')
            number = input('\t\t\t\t\t\tEnter number: ')
            if number in ['1', '2']:
                return int(number)
    return int(number)


def validate_for_ace():
    number = input('\t\t\t\t\t\t\t\tEnter number: ')
    while number not in ['1', '11']:
        print('\t\t\t\t\t\t\t\tYou can choose either 1, or 11')
        number = input('\t\t\t\t\t\t\t\tEnter number: ')

    return int(number)
