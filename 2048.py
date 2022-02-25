#!/usr/bin/env python3

import functions

board = []
ANSI = {'reset': '\033[0m', 'bold': '\033[1m', 'blink': '\033[5m', 'black': '\033[30m', 'red': '\033[31m',
        'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
        'white': '\033[37m', 'background_black': '\033[40m', 'background_red': '\033[41m',
        'background_green': '\033[42m', 'background_yellow': '\033[43m', 'background_blue': '\033[44m',
        'background_magenta': '\033[45m', 'background_cyan': '\033[46m', 'background_white': '\033[47m'}

dictionary_2048 = functions.read_csv_to_dictionary('Highscores_2048.csv')
functions.dictionary_values_to_int(dictionary_2048)

nick = input('Podaj swój nick: ')
if nick not in dictionary_2048:
    dictionary_2048[nick] = 0

for a in range(4):
    board.append([])
    for b in range(4):
        board[a].append(0)

functions.add_tile(board)
functions.add_tile(board)
functions.print_2048(board)

while True:
    getch = functions.getch()
    if getch == b'w' or getch == 'w':
        functions.merge_up(board)
    elif getch == b'a' or getch == 'a':
        functions.merge_left(board)
    elif getch == b's' or getch == 's':
        functions.merge_down(board)
    elif getch == b'd' or getch == 'd':
        functions.merge_right(board)
    # Windows arrows
    elif getch == b'\xe0':
        import msvcrt
        getch = msvcrt.getch()
        if getch == b'H':
            functions.merge_up(board)
        elif getch == b'K':
            functions.merge_left(board)
        elif getch == b'P':
            functions.merge_down(board)
        elif getch == b'M':
            functions.merge_right(board)
    # Linux arrows
    elif getch == '\033' and functions.getch() == '[':
        getch = functions.getch()
        if getch == 'A':
            functions.merge_up(board)
        elif getch == 'D':
            functions.merge_left(board)
        elif getch == 'B':
            functions.merge_down(board)
        elif getch == 'C':
            functions.merge_right(board)

    functions.add_tile(board)
    functions.print_2048(board)

    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3]:
        functions.print_2048(board)
        print('Przegrałeś!/Przegrałaś!\n          ☹')
        break
    if 2048 in board[0] or 2048 in board[1] or 2048 in board[2] or 2048 in board[3]:
        print('Brawo, wygrałeś/wygrałaś!\n            😃\nCzy chcesz kontynuować?\nTak - wciśnij enter\n'
              'Nie - wciśnij q')
        getch = functions.getch()
        if getch == b'\r' or getch == '\r':
            continue
        elif getch == b'q' or getch == 'q':
            break
    if 131072 in board[0] or 131072 in board[1] or 131072 in board[2] or 131072 in board[3]:
        print('Najwyższy czas zrobić sobie przerwę ;-)\nWciśnij q, żeby wyjść')
        getch = functions.getch()
        if getch == b'q' or getch == 'q':
            break

score = functions.score_from_board(board)
if score > dictionary_2048[nick]:
    dictionary_2048[nick] = score

functions.write_dictionary_to_csv(dictionary_2048, 'Highscores_2048.csv')

input('Wciśnij enter, żeby wyjść')
