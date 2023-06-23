#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, size):
    if row == size:
        # All queens have been placed, print the solution
        print([[i, board[i]] for i in range(size)])
        return
    for col in range(size):
        if is_safe(board, row, col):
            # Place the queen at the current position
            board[row] = col
            solve_nqueens(board, row + 1, size)

def nqueens(size):
    if not isinstance(size, int):
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * size
    solve_nqueens(board, 0, size)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
