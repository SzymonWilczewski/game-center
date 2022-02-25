#!/usr/bin/env python3

import functions
import random
import copy

board_width = int(input('Wpisz szerokość planszy: '))
board_height = int(input('Wpisz wysokość planszy: '))
bombs = int(input('Wpisz liczbę bomb: '))
board = []
empty_fields = []
counter = 0
ANSI = {'reset': '\033[0m', 'bold': '\033[1m', 'blink': '\033[5m', 'black': '\033[30m', 'red': '\033[31m',
        'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
        'white': '\033[37m', 'background_black': '\033[40m', 'background_red': '\033[41m',
        'background_green': '\033[42m', 'background_yellow': '\033[43m', 'background_blue': '\033[44m',
        'background_magenta': '\033[45m', 'background_cyan': '\033[46m', 'background_white': '\033[47m'}
print('------------------------------------------')

if bombs > (board_width * board_height):
    print('Nieprawidłowa ilość bomb!')
    quit()

functions.generate_board(board, board_height, board_width)

board_displayed = copy.deepcopy(board)

functions.generate_bombs(ANSI, board, board_height, board_width, bombs)

functions.generate_numbers_on_board(ANSI, board, board_height, board_width)

while True:
    width, height = functions.coordinates(ANSI, board, board_height, board_displayed, board_width)

    if board[height][width] == (ANSI['red'] + ' o ' + ANSI['reset']):
        functions.defeat(ANSI, board, board_height, board_width, height, width)
        quit()
    elif (board[height][width] == ' 1 ' or board[height][width] == ' 2 ' or board[height][width] == ' 3 ' or
          board[height][width] == ' 4 ' or board[height][width] == ' 5 ' or board[height][width] == ' 6 ' or
          board[height][width] == ' 7 ' or board[height][width] == ' 8 '):
        board_displayed[height][width] = board[height][width]
    elif board[height][width] == ' - ':
        functions.empty_fields_append(board, height, width, empty_fields)

        while counter < len(empty_fields):
            height = empty_fields[counter][0]
            width = empty_fields[counter][1]

            (board_displayed[height - 1][width - 1], board_displayed[height - 1][width],
             board_displayed[height - 1][width + 1], board_displayed[height][width - 1],
             board_displayed[height][width], board_displayed[height][width + 1],
             board_displayed[height + 1][width - 1], board_displayed[height + 1][width],
             board_displayed[height + 1][width + 1]) = (board[height - 1][width - 1], board[height - 1][width],
                                                        board[height - 1][width + 1], board[height][width - 1],
                                                        board[height][width], board[height][width + 1],
                                                        board[height + 1][width - 1], board[height + 1][width],
                                                        board[height + 1][width + 1])

            functions.add_spaces_to_board_displayed(board_displayed, height, width)

            functions.empty_fields_append(board, height, width, empty_fields)

            counter += 1

    if sum(x.count(' - ') for x in board_displayed) == bombs:
        functions.win(ANSI, board_height, board_width, board_displayed)
        quit()
