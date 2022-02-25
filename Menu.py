#!/usr/bin/env python3

print('   _____          __  __ ______    _____ ______ _   _ _______ ______ _____')
print('  / ____|   /\   |  \/  |  ____|  / ____|  ____| \ | |__   __|  ____|  __ \\')
print(' | |  __   /  \  | \  / | |__    | |    | |__  |  \| |  | |  | |__  | |__) |')
print(' | | |_ | / /\ \ | |\/| |  __|   | |    |  __| | . ` |  | |  |  __| |  _  /')
print(' | |__| |/ ____ \| |  | | |____  | |____| |____| |\  |  | |  | |____| | \ \\')
print('  \_____/_/    \_\_|  |_|______|  \_____|______|_| \_|  |_|  |______|_|  \_\\')
print()
print('1 - Saper\n2 - Sudoku\n3 - 2048')
choice = input('\n\nWciśnij enter, żeby wyjść\n')
if choice == '1':
    print('\n' * 25)
    import Saper
elif choice == '2':
    print('\n' * 25)
    import Sudoku
elif choice == '3':
    print('\n' * 25)
    __import__('2048')
else:
    quit()
