Programmer: Alexander Holmes
4/1/24
CS 4310: Design and Analysis of Algorithms
Assignment 4: Traveling Salesman Problem

This program implements the dynamic programming method for the traveling
salesman problem. 

The traveling salesperson problem is the idea of finding the shortest
path or shortest route for a salesperson to take on a business trip. 
We are given a starting point and a number of cities (nodes).
 
There are two cost matrices given, representing the cost weight
associated with each node in the problem. Each number represents the 
(cost/time associated with getting to the next node/city)

For a given adjacency matrix 
        [0, 10, 15, 20]
        [5, 0,  9,  10] 
        [6, 13, 0,  12]
        [8, 8,  9,  0 ]

    The first line reads there is 0 cost to get to our starting node from our starting node
    The second line, where it has a 0 reads there is 0 cost to get to node 2 from node 2
    The third line, where it has a 0 reads there is 0 cost to get to node 3 from node 3. Same with node 4.
    
    Essentially each line is giving the cost to travel to each other neighboring node. 
    If the node wasn't reachable from the other, we would initialize it with infinity 'inf()' in order to
    let the computer know we didn't have a connection there.

HOW TO RUN
This is a python file, using python's 3.11.8 64-bit interpreter. 
Run ' ./huffman_codes.py ' in the terminal (for windows & python3) or simply hit the run button on an IDE.

