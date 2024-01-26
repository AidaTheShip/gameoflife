import pygame
from Gameoflife import dimensions, env

screen_w, screen_h = dimensions
# setting pygame up
pygame.init() 
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
running = True

# matrix = [[1 ,1 ,0 ,1],
#           [1 ,0 ,0 ,1],
#           [1 ,1 ,0 ,1],
#           [1 ,1 ,1 ,1]]
grid_node_width = grid_node_height = 10

steps = 5
# Creating a grid display
def createSquare(x, y, color):
    pygame.draw.rect(screen, color, [x,y, grid_node_width, grid_node_height])
    
def visualizeGrid():
    y = 0 # starting from the top of the screen
    for row in env: 
        x = 0 # starting at the left of the screen
        for col in row:
            if col == 0: # if dead, then we have a black square
                createSquare(x,y,(0,0,0))
            else: 
                createSquare(x,y,(255,255,255)) # if alive, then the square will be white
            x += grid_node_width
        y += grid_node_height
    pygame.display.update()



# this will be the actual game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    visualizeGrid()
    pygame.display.flip()
    clock.tick(60) # FPS is limited to 60
            
pygame.quit()