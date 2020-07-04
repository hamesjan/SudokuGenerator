import numpy as np
import random

def generate():
    """
    The classic Sudoku game involves a grid of 81 squares.
    The grid is divided into nine blocks, each containing nine squares.
    The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares.
    Each number can only appear once in a row, column or box.
    """

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for row in range(9):
        for column in range(9):
            print(np.asmatrix(board))
            print(row, column)
            square = get_square(board, row, column)
            print(square)
            while True:
                val = random.randint(1, 9)
                print(val)
                if check_row(board, row, val) and check_column(board, column, val) and check_square(square, val):
                    board[row][column] = val
                    print('success')
                    break


    print(np.asmatrix(board))


def get_square(board, row, column):
    if row < 3:
        if column < 3:
            square = [board[i][0:3] for i in range(0, 3)]
        elif column < 6:
            square = [board[i][3:6] for i in range(0, 3)]
        else:
            square = [board[i][6:9] for i in range(0, 3)]
    elif row < 6:
        if column < 3:
            square = [board[i][0:3] for i in range(3, 6)]
        elif column < 6:
            square = [board[i][3:6] for i in range(3, 6)]
        else:
            square = [board[i][6:9] for i in range(3, 6)]
    else:
        if column < 3:
            square = [board[i][0:3] for i in range(6, 9)]
        elif column < 6:
            square = [board[i][3:6] for i in range(6, 9)]
        else:
            square = [board[i][6:9] for i in range(6, 9)]
    return square


def check_row(board, row, val):
    if val not in board[row]:
        return True
    return False


def check_column(board, column, val):
    temp = []
    for each in board:
        temp.append(each[column])
    if val not in temp:
        return True
    return False


def check_square(square, val):
    for each in square:
        if val not in each:
            continue
        else:
            return False
    return True


def main():
    """ Main entry point of the app """
    generate()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
