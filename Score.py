import os.path
def add_score(difficulty):
    if os.path.isfile('score.txt'):
        with open('score.txt', 'r') as file_score:
            file_score = file_score.read()
    else:
        with open('score.txt', 'x') as file_score:
            file_score = file_score.write('0')
    file_score = int(file_score)
    POINTS_OF_WINNING = (difficulty * 3) + 5
    file_score += POINTS_OF_WINNING
    with open('score.txt', 'w') as add_score:
        add_score.write(str(file_score))


