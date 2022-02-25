#!/usr/bin/env python3

import functions
import copy

board = []
temp_board = []
test_board = []
sudoku_list = []
permutation = []
ANSI = {'reset': '\033[0m', 'bold': '\033[1m', 'blink': '\033[5m', 'black': '\033[30m', 'red': '\033[31m',
        'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
        'white': '\033[37m', 'background_black': '\033[40m', 'background_red': '\033[41m',
        'background_green': '\033[42m', 'background_yellow': '\033[43m', 'background_blue': '\033[44m',
        'background_magenta': '\033[45m', 'background_cyan': '\033[46m', 'background_white': '\033[47m'}

dictionary_sudoku = functions.read_csv_to_dictionary('Boards_Sudoku.csv')

file = functions.difficulty_choice()

for a in range(9):
    temp_board.append([])
    for b in range(9):
        temp_board[a].append(0)

sudoku_list = functions.random_board_selection(file, sudoku_list)

permutation = functions.permutation(permutation)

temp_board = functions.swapping_numbers(sudoku_list, temp_board, permutation)

# Preview solved board #
# functions.print_sudoku(temp_board)

board = functions.add_blank_spaces(temp_board)

board_2 = copy.deepcopy(board)
board_3 = copy.deepcopy(board)

empty_fields = functions.empty_fields_to_list(board)

position = [0, 0]
board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI['reset']

functions.print_sudoku(board)

while True:
    getch = functions.getch()
    if getch == b'w' or getch == 'w' and 1 <= position[0] <= 8:
        board[position[0]][position[1]] = board_2[position[0]][position[1]]
        position[0] -= 1
        board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI['reset']
    elif getch == b'a' or getch == 'a' and 1 <= position[1] <= 8:
        board[position[0]][position[1]] = board_2[position[0]][position[1]]
        position[1] -= 1
        board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI['reset']
    elif getch == b's' or getch == 's' and 0 <= position[0] <= 7:
        board[position[0]][position[1]] = board_2[position[0]][position[1]]
        position[0] += 1
        board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI['reset']
    elif getch == b'd' or getch == 'd' and 0 <= position[1] <= 7:
        board[position[0]][position[1]] = board_2[position[0]][position[1]]
        position[1] += 1
        board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI['reset']
    # Windows arrows
    elif getch == b'\xe0':
        import msvcrt
        getch = msvcrt.getch()
        if getch == b'H' and 1 <= position[0] <= 8:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[0] -= 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == b'K' and 1 <= position[1] <= 8:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[1] -= 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == b'P' and 0 <= position[0] <= 7:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[0] += 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == b'M' and 0 <= position[1] <= 7:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[1] += 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
    # Linux arrows
    elif getch == '\033' and functions.getch() == '[':
        getch = functions.getch()
        if getch == 'A' and 1 <= position[0] <= 8:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[0] -= 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == 'D' and 1 <= position[1] <= 8:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[1] -= 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == 'B' and 0 <= position[0] <= 7:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[0] += 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
        elif getch == 'C' and 0 <= position[1] <= 7:
            board[position[0]][position[1]] = board_2[position[0]][position[1]]
            position[1] += 1
            board[position[0]][position[1]] = ANSI['background_red'] + str(board[position[0]][position[1]]) + ANSI[
                'reset']
    elif (getch == b'1' or getch == '1') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(1) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(1) + ANSI['reset']
        board_3[position[0]][position[1]] = 1
    elif (getch == b'2' or getch == '2') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(2) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(2) + ANSI['reset']
        board_3[position[0]][position[1]] = 2
    elif (getch == b'3' or getch == '3') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(3) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(3) + ANSI['reset']
        board_3[position[0]][position[1]] = 3
    elif (getch == b'4' or getch == '4') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(4) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(4) + ANSI['reset']
        board_3[position[0]][position[1]] = 4
    elif (getch == b'5' or getch == '5') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(5) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(5) + ANSI['reset']
        board_3[position[0]][position[1]] = 5
    elif (getch == b'6' or getch == '6') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(6) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(6) + ANSI['reset']
        board_3[position[0]][position[1]] = 6
    elif (getch == b'7' or getch == '7') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(7) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(7) + ANSI['reset']
        board_3[position[0]][position[1]] = 7
    elif (getch == b'8' or getch == '8') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(8) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(8) + ANSI['reset']
        board_3[position[0]][position[1]] = 8
    elif (getch == b'9' or getch == '9') and position in empty_fields:
        board[position[0]][position[1]] = ANSI['background_red'] + ANSI['blue'] + str(9) + ANSI['reset']
        board_2[position[0]][position[1]] = ANSI['blue'] + str(9) + ANSI['reset']
        board_3[position[0]][position[1]] = 9
    elif getch == b'\r' or getch == '\r':
        if functions.valid_board(board_3):
            print('Plansza rozwiązana poprawnie!\n              😃')
        else:
            print('Plansza rozwiązana niepoprawnie!\n               ☹')
        break
    elif getch == b'q' or getch == 'q':
        nick = input('Podaj swój nick: ')
        dictionary_sudoku = functions.boards_to_dictionary(nick, dictionary_sudoku, board, board_2, board_3)
        functions.write_dictionary_to_csv(dictionary_sudoku, 'Boards_Sudoku.csv')
        break
    functions.print_sudoku(board)

input('Wciśnij enter, żeby wyjść')
