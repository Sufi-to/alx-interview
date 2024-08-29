#!/usr/bin/python3
"""Module for solving n_queen queens problem"""

from sys import argv


if len(argv) > 2 or len(argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n_queen = int(argv[1])


def solve_n_queens(n_queen, row=0, cols=[], dgn1=[], dgn2=[]):
    """ Solves the position of the queens """
    if row < n_queen:
        for j in range(n_queen):
            if j not in cols and row + j not in dgn1 and row - j not in dgn2:
                yield from solve_n_queens(n_queen,
                                          row + 1,
                                          cols + [j],
                                          dgn1 + [row + j],
                                          dgn2 + [row - j])
    else:
        yield cols


def solve_board(n_queen):
    """ Solves the board given the number of queens """
    for solution in solve_n_queens(n_queen):
        board = []
        for row, col in enumerate(solution):
            board.append([row, col])
        print(board)


solve_board(n_queen)
