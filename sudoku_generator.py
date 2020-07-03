from random import randrange
import numpy as np

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
    for row in range(10):
        for column in range(10):
            while True:
                val = randrange(10)
                if checkRow(row, val) and checkColumn(column, val) and checkSquare(square, val):
                    board[row][column] = val
                    break
                else: continue
    print(np.asmatrix(board))



def checkRow(row, val):


def checkColumn(column, val):

def checkSquare(square, val):


def main():
    """ Main entry point of the app """
    generate()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()