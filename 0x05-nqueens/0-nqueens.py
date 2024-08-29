#!/usr/bin/python3
"""Nqueens challenge"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at board[row][col] without being attacked.

    Args:
        board (list): Chessboard state.
        row (int): Row index.
        col (int): Column index.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """
    Place queens column by column and save solutions.

    Args:
        board (list): Chessboard state.
        col (int): Current column index.
        solutions (list): List to store solutions.

    Returns:
        bool: True if a solution is found.
    """
    if col >= len(board):
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0

    return res


def solve_nqueens(N):
    """
    Solve the N-queens problem and return all solutions.

    Args:
        N (int): Size of the chessboard.

    Returns:
        list: All possible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    """
    Parse input, validate, and print N-queens solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
