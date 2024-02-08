#!/usr/bin/python3
"""
This module contains the solve_n_queens function.
"""
import sys


def solve_n_queens(N):
    """
    This function solves the N queens problem.
    """
    def can_place(pos, ocuppied_positions):
        """
        This function checks if a queen can be placed in a certain position.
        """
        for i in range(len(ocuppied_positions)):
            cond1 = ocuppied_positions[i] == pos
            cond2 = ocuppied_positions[i] - i == pos - len(ocuppied_positions)
            cond3 = ocuppied_positions[i] + i == pos + len(ocuppied_positions)
            if cond1 or cond2 or cond3:
                return False
        return True

    def place_queen(ocuppied_positions, target_row, N):
        """
        This function places a queen in a certain position.
        """
        if target_row == N:
            return [ocuppied_positions]
        else:
            solutions = []
            for column in range(N):
                if can_place(column, ocuppied_positions):
                    new_positions = ocuppied_positions + [column]
                    solutions += place_queen(new_positions, target_row + 1, N)
            return solutions

    solutions = place_queen([], 0, N)
    return [[(i, pos) for i, pos in enumerate(sol)] for sol in solutions]


def main():
    """
    This is main function that takes an argument
    and checks if it is valid
    and prints the solutions to the N queens problem.
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

    for solution in solve_n_queens(N):
        print(solution)


if __name__ == "__main__":
    main()
