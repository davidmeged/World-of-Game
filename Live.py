import MemoryGame
import GuessGame
import CurrencyRouletteGame

def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')

def load_game():
    while True:
        print("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
            4. Exit""")
        while True:
            selected_game = input('Enter you choice: ')
            if selected_game.isnumeric() and 0 < int(selected_game) < 5:
                break
            else:
                print('Wrong choice. Please select numbers 1-4.')
        if selected_game == '4':
            break
        while True:
            difficulty_game = input('Please choose game difficulty from 1 to 5: ')
            if difficulty_game.isnumeric() and 0 < int(difficulty_game) < 6:
                difficulty_game = int(difficulty_game)
                break
            else:
                print('Wrong choice. Please select numbers 1-5.')
        if selected_game == '1': #Memory Game
            MemoryGame.play(difficulty_game)
        elif selected_game == '2': #Guess Game
            GuessGame.play(difficulty_game)
        elif selected_game == '3': #CurrencyRouletteGame
            CurrencyRouletteGame.play(difficulty_game)

