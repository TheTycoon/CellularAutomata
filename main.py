import pygame
from pygame.locals import *
from random import randint

import cell
import settings

window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

# fill a list with cells randomly assigned on or off
grid = []
for row in range(settings.ROWS):
    grid.append([])
    for column in range(settings.COLUMNS):
        grid[row].append(cell.Cell(column, row, randint(0,100)))


# set the neighborhood around all cells except border cells
for row in range(settings.ROWS):
    for column in range(settings.COLUMNS):
        if row != 0 and column != 0 and row != settings.ROWS - 1 and column != settings.COLUMNS - 1:
            grid[column][row].set_neighborhood(grid)

# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close program and exit loop if a quit event happens
        if event.type == QUIT:
            running = False

        # All Key Pressed Events
        if event.type == pygame.KEYDOWN:

            # Press spacebar to simulate a new generation of cell lives for caves, don't generate border cells
            if event.key == pygame.K_SPACE:
                for row in range(settings.ROWS):
                    for column in range(settings.COLUMNS):
                        if row != 0 and column != 0 and row != settings.ROWS - 1 and column != settings.COLUMNS - 1:
                            grid[column][row].cave_generate()
                for row in range(settings.ROWS):
                    for column in range(settings.COLUMNS):
                        if row != 0 and column != 0 and row != settings.ROWS - 1 and column != settings.COLUMNS - 1:
                            grid[column][row].update()

            # press return to use the 'game of life' rules to generate
            if event.key == pygame.K_RETURN:
                    for row in range(settings.ROWS):
                        for column in range(settings.COLUMNS):
                            if row != 0 and column != 0 and row != settings.ROWS - 1 and column != settings.COLUMNS - 1:
                                grid[column][row].game_of_life_generate()
                    for row in range(settings.ROWS):
                        for column in range(settings.COLUMNS):
                            if row != 0 and column != 0 and row != settings.ROWS - 1 and column != settings.COLUMNS - 1:
                                grid[column][row].update()


    # DRAW STUFF
    for row in range(settings.ROWS):
        for column in range(settings.COLUMNS):
            if grid[row][column].state is True:
                pygame.draw.rect(window, settings.WHITE, grid[row][column].rect, 0)
            else:
                pygame.draw.rect(window, settings.GRAY, grid[row][column].rect, 0)

    # DISPLAY FRAME
    pygame.display.update()
