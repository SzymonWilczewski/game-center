#!/usr/bin/env python3

import random
import copy
import platform
import csv

numbers_2048 = {0: '  ║       ║  ', 2: '  ║   2   ║  ', 4: '  ║   4   ║  ', 8: '  ║   8   ║  ', 16: '  ║   16  ║  ',
                32: '  ║   32  ║  ', 64: '  ║   64  ║  ', 128: '  ║  128  ║  ', 256: '  ║  256  ║  ',
                512: '  ║  512  ║  ', 1024: '  ║  1024 ║  ', 2048: '  ║  2048 ║  ', 4096: '  ║  4096 ║  ',
                8192: '  ║  8192 ║  ', 16384: '  ║ 16384 ║  ', 32768: '  ║ 32768 ║  ', 65536: '  ║ 65536 ║  ',
                131072: '  ║ 131072║  '}

# General


def getch():
    if platform.system() == 'Windows':
        return getch_windows()
    elif platform.system() == 'Linux':
        return getch_linux()


def getch_windows():
    import msvcrt
    return msvcrt.getch()


def getch_linux():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def write_dictionary_to_csv(dictionary, file_name):
    with open(file_name, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dictionary.items():
            writer.writerow([key, value])


def read_csv_to_dictionary(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        dictionary = dict(reader)
        return dictionary


def dictionary_values_to_int(dictionary):
    for key, value in dictionary.items():
        dictionary[key] = int(value)


# Saper


def generate_board(board, board_height, board_width):
    for a in range(board_height + 3):
        board.append([])
        for b in range(board_width + 3):
            if a == 0:
                if b == 0:
                    board[a].append('   ')
                elif b == 1:
                    board[a].append(' ')
                elif b == board_width + 2:
                    board[a].append(' ')
                elif 1 <= (b - 1) < 10:
                    board[a].append(' ' + str(b - 1) + ' ')
                elif 10 <= (b - 1) < 100:
                    board[a].append(' ' + str(b - 1))
                elif 100 <= (b - 1) < 1000:
                    board[a].append(str(b - 1))
            elif a == 1:
                if b == 0:
                    board[a].append('   ')
                elif b == 1:
                    board[a].append('╔')
                elif b == board_width + 2:
                    board[a].append('╗')
                else:
                    board[a].append('═══')
            elif a == board_height + 2:
                if b == 0:
                    board[a].append('   ')
                elif b == 1:
                    board[a].append('╚')
                elif b == board_width + 2:
                    board[a].append('╝')
                else:
                    board[a].append('═══')
            else:
                if b == 0:
                    if 1 <= (a - 1) < 10:
                        board[a].append('  ' + str(a - 1))
                    elif 10 <= (a - 1) < 100:
                        board[a].append(' ' + str(a - 1))
                    elif 100 <= (a - 1) < 1000:
                        board[a].append(str(a - 1))
                elif b == 1:
                    board[a].append('║')
                elif b == board_width + 2:
                    board[a].append('║')
                else:
                    board[a].append(' - ')


def generate_bombs(ANSI, board, board_height, board_width, bombs):
    while sum(x.count(ANSI['red'] + ' o ' + ANSI['reset']) for x in board) < bombs:
        board[random.randint(2, board_height + 1)][random.randint(2, board_width + 1)] = ANSI['red'] + ' o ' + ANSI[
            'reset']


def generate_numbers_on_board(ANSI, board, board_height, board_width):
    for c in range(2, board_height + 2):
        for d in range(2, board_width + 2):
            if board[c][d] == ' - ':
                board_temp = [board[c - 1][d - 1], board[c - 1][d], board[c - 1][d + 1], board[c][d - 1],
                              board[c][d + 1],
                              board[c + 1][d - 1], board[c + 1][d], board[c + 1][d + 1]]
                if board_temp.count(ANSI['red'] + ' o ' + ANSI['reset']) > 0:
                    board[c][d] = ' ' + str(board_temp.count(ANSI['red'] + ' o ' + ANSI['reset'])) + ' '


def coordinates(ANSI, board, board_height, board_displayed, board_width):
    for e in range(2, board_width + 2):
        board_displayed[0][e] = ANSI['bold'] + ANSI['red'] + board_displayed[0][e] + ANSI['reset']
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for z in range(board_height + 3):
        print(*board_displayed[z], sep=' ')
    width = int(input('Wybierz współrzędną: ')) + 1
    board_displayed[0] = board[0][:]
    for f in range(2, board_height + 2):
        board_displayed[f][0] = ANSI['bold'] + ANSI['red'] + board_displayed[f][0] + ANSI['reset']
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for z in range(board_height + 3):
        print(*board_displayed[z], sep=' ')
    height = int(input('Wybierz współrzędną: ')) + 1
    for g in range(2, board_height + 2):
        board_displayed[g][0] = board[g][0]
    return width, height


def empty_fields_append(board, height, width, empty_fields):
    if board[height - 1][width - 1] == ' - ' and (height - 1, width - 1) not in empty_fields:
        empty_fields.append((height - 1, width - 1))
    if board[height - 1][width] == ' - ' and (height - 1, width) not in empty_fields:
        empty_fields.append((height - 1, width))
    if board[height - 1][width + 1] == ' - ' and (height - 1, width + 1) not in empty_fields:
        empty_fields.append((height - 1, width + 1))
    if board[height][width - 1] == ' - ' and (height, width - 1) not in empty_fields:
        empty_fields.append((height, width - 1))
    if board[height][width] == ' - ' and (height, width) not in empty_fields:
        empty_fields.append((height, width))
    if board[height][width + 1] == ' - ' and (height, width + 1) not in empty_fields:
        empty_fields.append((height, width + 1))
    if board[height + 1][width - 1] == ' - ' and (height + 1, width - 1) not in empty_fields:
        empty_fields.append((height + 1, width - 1))
    if board[height + 1][width] == ' - ' and (height + 1, width) not in empty_fields:
        empty_fields.append((height + 1, width))
    if board[height + 1][width + 1] == ' - ' and (height + 1, width + 1) not in empty_fields:
        empty_fields.append((height + 1, width + 1))


def add_spaces_to_board_displayed(board_displayed, height, width):
    if board_displayed[height - 1][width - 1] == ' - ':
        board_displayed[height - 1][width - 1] = '   '
    if board_displayed[height - 1][width] == ' - ':
        board_displayed[height - 1][width] = '   '
    if board_displayed[height - 1][width + 1] == ' - ':
        board_displayed[height - 1][width + 1] = '   '
    if board_displayed[height][width - 1] == ' - ':
        board_displayed[height][width - 1] = '   '
    if board_displayed[height][width] == ' - ':
        board_displayed[height][width] = '   '
    if board_displayed[height][width + 1] == ' - ':
        board_displayed[height][width + 1] = '   '
    if board_displayed[height + 1][width - 1] == ' - ':
        board_displayed[height + 1][width - 1] = '   '
    if board_displayed[height + 1][width] == ' - ':
        board_displayed[height + 1][width] = '   '
    if board_displayed[height + 1][width + 1] == ' - ':
        board_displayed[height + 1][width + 1] = '   '


def defeat(ANSI, board, board_height, board_width, height, width):
    for h in range(2, board_height + 2):
        for i in range(2, board_width + 2):
            if board[h][i] == ' - ':
                board[h][i] = '   '
                board[height][width] = ANSI['background_red'] + ' o ' + ANSI['reset']
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for z in range(board_height + 3):
        print(*board[z], sep=' ')
    print('Przegrałeś!/Przegrałaś!\n          ☹')


def win(ANSI, board_height, board_width, board_displayed):
    for j in range(2, board_height + 2):
        for k in range(2, board_width + 2):
            if board_displayed[j][k] == ' - ':
                board_displayed[j][k] = ANSI['red'] + ' o ' + ANSI['reset']
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for z in range(board_height + 3):
        print(*board_displayed[z], sep=' ')
    print('Wygrałeś!/Wygrałaś!\n        😃')


# Sudoku


def add_blank_spaces(board_without_blank_spaces):
    test_board = copy.deepcopy(board_without_blank_spaces)

    for g in range(9):
        for h in range(7):
            test_board[g][random.randint(0, 8)] = ' '

    test_if_board_is_solvable = copy.deepcopy(test_board)

    if solve(test_if_board_is_solvable):
        return test_board
    else:
        add_blank_spaces(board_without_blank_spaces)


def solve(board):
    empty_position = find_empty_position(board)
    if not empty_position:
        return True
    else:
        row, column = empty_position

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = ' '
    return False


def find_empty_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ' ':
                return i, j
    return None


def valid(board, number, position):
    # row
    for i in range(9):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # column
    for i in range(9):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, (box_y * 3) + 3):
        for j in range(box_x * 3, (box_x * 3) + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def print_sudoku(board):
    for z in range(9):
        if z == 0:
            print('\n' * 25)
        if z == 3 or z == 6:
            print('══════╬═══════╬══════')
        print(board[z][0], board[z][1], board[z][2], '║',
              board[z][3], board[z][4], board[z][5], '║',
              board[z][6], board[z][7], board[z][8])


def empty_fields_to_list(board):
    empty_fields_list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                empty_fields_list.append([i, j])
    return empty_fields_list


def valid_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not valid(board, board[i][j], (i, j)):
                return False
    return True


def difficulty_choice():
    print('Wybierz poziom trudności:\n1 - Easy\n2 - Medium\n3 - Hard\n4 - Very hard')
    file = int(input())
    if file == 1:
        file = 'Sudoku_Easy.txt'
    elif file == 2:
        file = 'Sudoku_Medium.txt'
    elif file == 3:
        file = 'Sudoku_Hard.txt'
    elif file == 4:
        file = 'Sudoku_Very_Hard.txt'
    return file


def random_board_selection(file, sudoku_list):
    import linecache
    puzzle_number = random.randint(1, 48)
    for c in range((puzzle_number * 10) - 8, (puzzle_number * 10) + 1):
        getline_temp_list = linecache.getline(file, c).split()
        for d in range(9):
            sudoku_list.append(int(getline_temp_list[d]))
    return sudoku_list


def permutation(permutation):
    while len(permutation) != 9:
        temp = random.randint(1, 9)
        if temp not in permutation:
            permutation.append(temp)
    return permutation


def swapping_numbers(sudoku_list, temp_board, permutation):
    randomizer = random.randint(0, 1)
    counter = 0
    if randomizer == 0:
        range_1 = random.choice([range(9), range(8, -1, -1)])
        range_2 = random.choice([range(9), range(8, -1, -1)])
        for e in range_1:
            for f in range_2:
                if sudoku_list[counter] == 1:
                    temp_board[e][f] = permutation[0]
                elif sudoku_list[counter] == 2:
                    temp_board[e][f] = permutation[1]
                elif sudoku_list[counter] == 3:
                    temp_board[e][f] = permutation[2]
                elif sudoku_list[counter] == 4:
                    temp_board[e][f] = permutation[3]
                elif sudoku_list[counter] == 5:
                    temp_board[e][f] = permutation[4]
                elif sudoku_list[counter] == 6:
                    temp_board[e][f] = permutation[5]
                elif sudoku_list[counter] == 7:
                    temp_board[e][f] = permutation[6]
                elif sudoku_list[counter] == 8:
                    temp_board[e][f] = permutation[7]
                elif sudoku_list[counter] == 9:
                    temp_board[e][f] = permutation[8]
                counter += 1
    else:
        range_1 = random.choice([range(9), range(8, -1, -1)])
        range_2 = random.choice([range(9), range(8, -1, -1)])
        for e in range_1:
            for f in range_2:
                if sudoku_list[counter] == 1:
                    temp_board[f][e] = permutation[0]
                elif sudoku_list[counter] == 2:
                    temp_board[f][e] = permutation[1]
                elif sudoku_list[counter] == 3:
                    temp_board[f][e] = permutation[2]
                elif sudoku_list[counter] == 4:
                    temp_board[f][e] = permutation[3]
                elif sudoku_list[counter] == 5:
                    temp_board[f][e] = permutation[4]
                elif sudoku_list[counter] == 6:
                    temp_board[f][e] = permutation[5]
                elif sudoku_list[counter] == 7:
                    temp_board[f][e] = permutation[6]
                elif sudoku_list[counter] == 8:
                    temp_board[f][e] = permutation[7]
                elif sudoku_list[counter] == 9:
                    temp_board[f][e] = permutation[8]
                counter += 1
    return temp_board


def boards_to_dictionary(nick, dictionary, board, board2, board3):
    if nick in dictionary:
        decision = input('\nCzy nadpisać planszę?\nt - Tak, n - Nie\n')
        if decision == 't':
            dictionary[nick] = (board, board2, board3)
            return dictionary
        else:
            return dictionary
    else:
        dictionary[nick] = (board, board2, board3)
        return dictionary


# 2048


def add_tile(board):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    list_of_tiles = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    if board[x][y] == 0:
        board[x][y] = random.choice(list_of_tiles)
    else:
        add_tile(board)


def merge_list(original_list):
    temp_list = []
    final_list = []
    counter = 0

    for i in original_list:
        if i != 0:
            temp_list.append(i)

    while len(temp_list) < len(original_list) + 1:
        temp_list.append(0)

    while counter < len(temp_list) - 1:
        if temp_list[counter] == temp_list[counter + 1] and temp_list[counter] != 0:
            final_list.append(temp_list[counter] * 2)
            counter += 2
        else:
            final_list.append(temp_list[counter])
            counter += 1

    while len(final_list) < len(original_list):
        final_list.append(0)

    return final_list


def merge_up(board):
    for i in range(len(board[0])):
        temp_list = []
        for j in range(len(board)):
            temp_list.append(board[j][i])
        temp_list = merge_list(temp_list)
        for x in range(len(board)):
            board[x][i] = temp_list[x]


def merge_left(board):
    for i in range(len(board)):
        temp_list = []
        for j in range(len(board[0])):
            temp_list.append(board[i][j])
        temp_list = merge_list(temp_list)
        for x in range(len(board[0])):
            board[i][x] = temp_list[x]


def merge_down(board):
    for i in range(len(board[0])):
        temp_list = []
        for j in reversed(range(len(board))):
            temp_list.append(board[j][i])
        temp_list = merge_list(temp_list)
        temp_list.reverse()
        for x in range(len(board)):
            board[x][i] = temp_list[x]


def merge_right(board):
    for i in range(len(board)):
        temp_list = []
        for j in reversed(range(len(board[0]))):
            temp_list.append(board[i][j])
        temp_list = merge_list(temp_list)
        temp_list.reverse()
        for x in range(len(board[0])):
            board[i][x] = temp_list[x]


def score_from_board(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            score += board[i][j]
    return score


def print_2048(board):
    print('\n' * 25)
    for z in range(4):
        print('                                                    ')
        print('  ╔═══════╗    ╔═══════╗    ╔═══════╗    ╔═══════╗  ')
        print('  ║       ║    ║       ║    ║       ║    ║       ║  ')
        print(numbers_2048[board[z][0]], numbers_2048[board[z][1]],
              numbers_2048[board[z][2]], numbers_2048[board[z][3]], sep='')
        print('  ║       ║    ║       ║    ║       ║    ║       ║  ')
        print('  ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ')
        print('                                                    ')
