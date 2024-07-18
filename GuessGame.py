from colorama import Fore
import random

def generate_number(number):
    secret_number = 0
    secret_number = random.randint(1, number)
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        guess_user = input(f'Guess a number from 1 to {difficulty}: ')
        if not guess_user.isnumeric():
            print('You only need to put numbers...')
        else:
            break
    return int(guess_user)

def compare_results(generate_num, user_choice):
    return generate_num == user_choice

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_user = get_guess_from_user(difficulty)
    check = compare_results(secret_number, guess_user)
    if check == True:
        print(Fore.GREEN + 'Your guess is correct!', Fore.RESET)
    else:
        print(Fore.RED + f'Your guess is wrong. Your numer is {guess_user} and computer number is {secret_number}', Fore.RESET)

