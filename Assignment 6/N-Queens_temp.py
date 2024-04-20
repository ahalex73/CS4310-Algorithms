# Programmer: Alexander Holmes
# 4/13/24
# CS 4310: Design and Analysis of Algorithms
# Assignment 6: N-Queens problem

"""
The N-Queens Problem is the problem of placing N chess queens on an NxN chessboard so that no two queens attack each other.

The Queen comes from the game of chess. Having the ability to move up, down, and diagonal one space in any direction that still
remains available on the board (can't go off of the board)

backtracking_n_queens() - The backtracking function used to grant solutions to N-Queens

In this program we are appending solutions to a solutions list and checking to make
sure that we aren't appending reflections or rotations of correct solutions
"""



import time
import matplotlib.pyplot as plt
import math

def is_valid_queen(board, row, col):
    """ Checks if queens are safe from other queens after selecting a spot to place """
    # Only need to check from left to right board[0 -> -1] columns

    # Check if its a restricted row, labeled with -1
    if board[row][col] == -1:
        return False

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1: # or if restricting first row for queen placement to not have reflective solutions            
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
        
    return True


def backtracking_n_queens(board, row, n, solutions):
    if row == n:
        # String represenation of a solution board
        solution = ["".join("Q" if cell == 1 else "." for cell in row) for row in board]
        if solution not in solutions:
            solutions.append(solution)
        return

    for col in range(n):
        if is_valid_queen(board, row, col):
            board[row][col] = 1
            backtracking_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0
        

def n_queens(N):
    board = [[0 for i in range(N)]
                for j in range(N)]
    
    restrictive = math.ceil(N/2)
    
    # Insert restrictive first row selection
    for i in range(N):
        if i >= restrictive:
            #display_solution(board, N)
            board[0][i] = -1

    #display_solution(board, N)

    solutions = []
    backtracking_n_queens(board, 0, N, solutions)
    return solutions

def display_solution(board, N):
    """ Display solution board """
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


def main():
    """ Main function """    
    n_list = [4, 5, 6, 7, 8, 9, 10] # Test for various numbers of queens
    timing_list = []
    #print(timing_list)

    for i in range(len(n_list)):
        start_time = time.perf_counter_ns()
        N = n_list[i]
        solutions = n_queens(N)
        num_solutions = 0
        for idx in solutions:
            num_solutions += 1
        
        end_time = time.perf_counter_ns() - start_time

        timing_list.append(end_time)
        
        print(f"Number of solutions for {N}-Queens: {num_solutions}\tCalculated in {end_time} nanoseconds.")
    
    plt.plot(n_list, timing_list)
    plt.xlabel('Number of Queens (n)')
    plt.ylabel('Execution Time (nanoseconds)')
    plt.title('Execution Time vs. Number of Queens (N! complexity)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

