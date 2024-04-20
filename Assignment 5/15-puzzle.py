import copy
from heapq import heappush, heappop
import time

n = 4

# Defining ruleset 
# down, left, up, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def is_empty(self):
        return not self.heap

class node:
    def __init__(self, parent, mat, empty_tile_pos, cost, depth):
        self.parent = parent
        self.mat = mat          # store matrix
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.depth = depth      # could also be seen as number of moves taken so far

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and mat[i][j] != final[i][j]:
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, depth, parent, final) -> node:
    new_mat = copy.deepcopy(mat)
    # Move tile by 1 position
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculateCost(new_mat, final)
    new_node = node(parent, new_mat, new_empty_tile_pos, cost, depth)
    return new_node

def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end=" ")
        print()

def isSafe(x, y):    
    """ Check bounds of moving """
    return 0 <= x < n and 0 <= y < n

def printPath(root):
    """ Display path from root node to destination node """
    if root is None:
        return
    
    printPath(root.parent)
    printMatrix(root.mat)
    print()

def solve(initial, empty_tile_pos, goal_state):
    """ Branch and bound function to solve puzzle"""
    # Store live nodes of search tree in priority queue
    pq = priorityQueue()

    # Create the root node
    cost = calculateCost(initial, goal_state)
    root = node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)

    while not pq.is_empty():
        # Find a live node with least estimated cost and delete it from the list of live nodes
        minimum = pq.pop()

        # If minimum is the resulting node
        if minimum.cost == 0:
            printPath(minimum)
            return

        # Generate all possible children AKA Make all possible moves
        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if isSafe(*new_tile_pos):
                # Create a child node
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.depth + 1, minimum, goal_state)
                # Add child to list of live nodes
                pq.push(child)


initial_states = [
    [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 14, 15]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]],
]

goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]  # Solvable final configuration
empty_tile_pos_list = [[1, 2], [2, 2], [2, 3], [3, 1], [3, 2]]

start_time = time.perf_counter_ns()

for index, initial_state in enumerate(initial_states):
    print("--Initial matrix ", index + 1 , "--")
    solve(initial_state, empty_tile_pos_list[index], goal_state)
    print("--Finished solving matrix", index + 1, "--\n")

end_time = time.perf_counter_ns() - start_time


print("The Total execution time was", end_time, "nanoseconds")