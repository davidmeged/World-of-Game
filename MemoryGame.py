from colorama import Fore
from random import sample
import time

def generate_sequence(difficulty):
    list = [num for num in range(1, 101)]
    return sample(list, difficulty) #create a list of random numbers

def get_list_from_user(difficulty):
    while True:
        list_user = input(f'Enter the number you saw ({difficulty} numbers): ')
        if not list_user: #Check if list is empty
            print('The list is empty.')
            continue
        else:
            list_user = list_user.split(',')
            if len(list_user) != difficulty: #Checks if the user has entered the correct amount of numbers.
                print(f'You need {difficulty} numbers...')
                continue
            elif False in list(map(str.isnumeric, list_user)): #Checks if the user puts characters that are not numbers.
                print('You only need to put numbers...')
                continue
            else:
                break
    new_list = [int(num) for num in list_user] #Converts the user's input from a string to numbers.
    return new_list

def is_list_equal(list_computer, list_user):
    list_computer.sort()
    list_user.sort()
    return list_user == list_computer

def play(difficulty):
    random_list_computer = generate_sequence(difficulty)

    #Prints the numbers of the computer and deletes after 0.7 seconds.
    print(random_list_computer, end='')
    time.sleep(0.7)
    print('\r   ')


    memory_list_user = get_list_from_user(difficulty)

    if is_list_equal(random_list_computer, memory_list_user):
        print(Fore.GREEN + 'You are a genius', Fore.RESET)
    else:
        print(Fore.RED + f'You are wrong, this is list of the computer: {random_list_computer}', Fore.RESET)
