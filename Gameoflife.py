import math
import numpy as np
#import pygames

# What is the game of life?
""""
The Game of Life is a "game" by the British mathematician John Conway.
It is a cellular automaton but you can think of it as a simulation whose evolution depends on nothing but the intiial state.

Here's major things we need to consider: 
    Matter
    - 2D grid (environment) of cells
    - 2 states of the cells: Alive or Dead

    Rules
    1. Alive cells die if they have fewer than 2 or more than 3 living neighbors.
    2. Alive cells stay alive if they have 3 living neighbors.
    3. Dead cells with *exactly* 3 living neighbors become alive.
"""
# How do we code this?
"""
- Create the environment. A matrix grid that keeps track of alive and dead cells.

- Create the visualization of the grid

"""
# Defining our variable

dimensions = (1080, 1080)

# Create the environment
env = np.zeros(dimensions) # our environment will not have any life in there for now.

# Do I need a score actually? Not entirely sure... I just need to be able to check the neighbors.
# env[5,4] = 1
# env[5,5] = 1
# Going from a cell i, this is all the directions you would have to go to scan the neighboring cells
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (-1,1), (1,0), (1,1)]


def scan_neighbor(cell, i, j):
    num_rows = len(cell)
    num_col = len(cell[0]) if num_rows else 0 
    
    score = 0 # this is the score for each cell at the beginning
    for x,y in directions: # looping through each of these directions
        if 0 < (i+x) < num_rows-1 and 0 < (j+y) < num_col-1: 
            score += cell[i + x][j + y] 
        
    return score

# Implementing the rules
def death():
    pass

def alive():
    pass

def resurrection():
    pass

def check_neighbors(): 
    pass
    

# Overall logic - gameloop to be called
def Gameloop():
    check_neighbors()
    

