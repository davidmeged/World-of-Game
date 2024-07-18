from colorama import Fore
import random
from currency_converter import CurrencyConverter

def get_money_interval(difficulty):
    usd_ils_object = CurrencyConverter()
    ils = int(usd_ils_object.convert(1, 'USD', 'ILS'))
    ran_number = random.randint(1, 101)
    secret_number = ils * ran_number
    first_number = secret_number - (5 - difficulty)
    end_number = secret_number + (5 - difficulty)
    return [first_number, end_number]

def get_guess_from_user():
    while True:
        user_guess = input('Enter your number guess: ')
        if not user_guess.isnumeric():
            print('You only need to put numbers...')
        else:
            break
    return int(user_guess)

def play(difficulty):
    list = get_money_interval(difficulty)
    user = get_guess_from_user()
    if  list[0] < user < list[1]:
        print(Fore.GREEN + f'You succeeded! The range of number was from {list[0]} to {list[1]}.', Fore.RESET)
    else:
        print(Fore.RED + f'Loser. The range of number was from {list[0]} to {list[1]}.', Fore.RESET)

