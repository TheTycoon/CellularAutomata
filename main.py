import pygame, sys
from pygame.locals import *
from random import randint

import CellClass


# create a new drawing surface, width=640, height=640
window = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Cellular Automata')

# Set rows, columns, and tilesize(square in pixels) for your grid
ROWS = 40
COLUMNS = 40
TILESIZE = 16

# fill a list with cells randomly assigned on or off
gridList = []
for i in range(ROWS * COLUMNS):
        gridList.append(CellClass.Cell(TILESIZE, ROWS, COLUMNS, i, randint(0, 100)))


# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close program and exit loop if a quit event happens
        if event.type == QUIT:
            running = False
            sys.exit()

        # All Key Pressed Events
        if event.type == pygame.KEYDOWN:

            # Press spacebar to simulate a new generation of cell lives
            if event.key == pygame.K_SPACE:
                for i in range(ROWS * COLUMNS):
                    CellClass.generate(gridList, i, ROWS, COLUMNS)

    # DRAW STUFF
    for i in range(ROWS * COLUMNS):
        if gridList[i].state:
            pygame.draw.rect(window, (250, 250, 250), gridList[i].rect, 0)
        else:
            pygame.draw.rect(window, (50, 50, 50), gridList[i].rect, 0)

    # DISPLAY FRAME
    pygame.display.update()
