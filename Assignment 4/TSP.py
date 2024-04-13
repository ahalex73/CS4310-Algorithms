# Programmer: Alexander Holmes
# 4/1/24
# CS 4310: Design and Analysis of Algorithms
# Assignment 4: Traveling Salesman Problem

from sys import maxsize 
from itertools import permutations
import time

def travellingSalesmanProblem(cost_matrix, s): 
    V = len(cost_matrix)
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize
    min_tour = None
    next_permutation = permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += cost_matrix[k][j] 
            k = j 
        current_pathweight += cost_matrix[k][s] 
 
        # update minimum 
        if current_pathweight < min_path:
            min_path = current_pathweight
            min_tour = [s] + list(i) + [s]  # S = Starting Node, i is arbitrary next node to travel to

    return min_path, min_tour

def print_matrix(matrix):
    for row in matrix:
        print(row)

def calculate_g_functions(cost_matrix):
    V = len(cost_matrix)
    g_functions = [[maxsize] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if i != j:
                g_functions[i][j] = cost_matrix[i][j]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                g_functions[i][j] = min(g_functions[i][j], g_functions[i][k] + g_functions[k][j])

    return g_functions

def print_cost_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def run_for_matrix(cost_matrix):
    """ Gives a provided matrix to run traveling salesperson on """
    num_cities = len(cost_matrix)

    start_time = time.perf_counter_ns()
    s = 0
    min_cost, min_tour = travellingSalesmanProblem(cost_matrix, s)
    g_functions = calculate_g_functions(cost_matrix)
    execution_time = time.perf_counter_ns() - start_time

    print("\nCost Adjacency Matrix:")
    print_matrix(cost_matrix)
    print("\nMinimum Cost:", min_cost)
    print("\nAssociated Tour (0 = Starting node):", min_tour)
    print("\ng-functions:")
    print_matrix(g_functions)
    print("\nExecution Time:", execution_time, "nano-seconds")

if __name__ == "__main__": 
    # Matrix representation of cost_matrix 
    cost_matrix_from_slides = [
        [0, 10, 15, 20],
        [5, 0, 9, 10], 
        [6, 13, 0, 12],
        [8, 8, 9, 0]
    ]

    example_cost_matrix = [
        [0, 5, 1, 3],
        [7, 0, 3, 4], 
        [6, 13, 0, 10],
        [9, 18, 12, 0]
    ]

    run_for_matrix(cost_matrix_from_slides)
    print("Waiting for 5 seconds to run for new example...")
    time.sleep(5)
    run_for_matrix(example_cost_matrix)
