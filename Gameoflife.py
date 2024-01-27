import math
import numpy as np
import pygame
import random

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
    2. Alive cells stay alive if they have 2 or 3 living neighbors.
    3. Dead cells with *exactly* 3 living neighbors become alive.
"""
# How do we code this?
"""
- Create the environment. A matrix grid that keeps track of alive and dead cells.

- Create the visualization of the grid

"""
# These are the dimensions of the environment we want to look at
dimensions = (700, 700)
grid_rows, grid_cols = dimensions

# Create the environment
# def random_matrix(rows, cols, num_ones):
#     env = np.zeros((rows, cols), dtype=int)
#     ones = np.eye()


# env = random_matrix(grid_rows, grid_cols, 500)  # 500 is the number of initial live cells
env = np.random.randint(0, 2, (500,500))


# env = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
#                         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

# Going from a cell i, this is all the directions you would have to go to scan the neighboring cells
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# Implementing the rules
def scan_neighbor(cells, i, j):
    num_rows = len(cells)
    num_col = len(cells[0]) if num_rows else 0 
    
    score = 0 # this is the score for each cell at the beginning
    for x,y in directions: # looping through each of these directions
        if 0 <= (i+x) < num_rows and 0 <= (j+y) < num_col: 
            score += cells[i + x][j + y] 
        
    return score

def next_state(cell, score):
    # We need to check the current state and the score to determine the next state
    if cell:
        if score < 2 or score > 3:
            cell = 0
    else:
        if score == 3:
            cell = 1
    return cell


# Overall logic - gameloop to be called
def Gameloop(env):
    new_env = np.copy(env)  # Create a copy of the current environment
    for i in range(len(env)):
        for j in range(len(env[0])):
            score = scan_neighbor(env, i, j)
            new_env[i][j] = next_state(env[i][j], score)
    return new_env


# THIS IS JUST HERE FOR TRAINING PURPOSES. 
# screen_w, screen_h = dimensions
# # setting pygame up
# pygame.init() 
# screen = pygame.display.set_mode((screen_w, screen_h))
# clock = pygame.time.Clock()
# running = True

# matrix = [[1 ,0 ,0 ,0],
#           [0 ,0 ,0 ,0],
#           [1 ,0 ,0 ,0],
#           [1 ,0 ,1 ,0]]
# grid_node_width = grid_node_height = 10

# steps = 5
# # Creating a grid display
# def createSquare(x, y, color):
#     pygame.draw.rect(screen, color, [x,y, grid_node_width, grid_node_height])
    
# def visualizeGrid(matrix):
#     y = 0 # starting from the top of the screen
#     for row in matrix: 
#         x = 0 # starting at the left of the screen
#         for col in row:
#             if col == 0: # if dead, then we have a black square
#                 createSquare(x,y,(0,0,0))
#             else: 
#                 createSquare(x,y,(255,255,255)) # if alive, then the square will be white
#             x += grid_node_width
#         y += grid_node_height
#     pygame.display.update()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))  # Clear screen
#     visualizeGrid(env)  # Draw the current state of the grid
#     pygame.display.flip()  # Update the full display

#     env = Gameloop(env)  # Update the environment for the next state

#     clock.tick(60)  # Control the speed of updates

# pygame.quit()