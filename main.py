import pygame
import settings
import cell

window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

map = cell.Map()

# MAIN LOOP
running = True
while running:

    # EVENT LOOP
    for event in pygame.event.get():

        # Close program and exit loop if a quit event happens
        if event.type == pygame.QUIT:
            running = False

        # All Key Pressed Events
        if event.type == pygame.KEYDOWN:

            # Press escape to exit
            if event.key == pygame.K_ESCAPE:
                running = False

            # Press spacebar to simulate a new generation of cell lives for caves
            if event.key == pygame.K_SPACE:
                for i in range(25):  # can be any number, takes ~25 to completely generate any random starting seed
                    map.cave_generate()
                    map.update()

            # press return to use the 'game of life' rules to generate
            if event.key == pygame.K_RETURN:
                map.game_of_life_generate()
                map.update()

            # press tab to restart with another random map
            if event.key == pygame.K_TAB:
                map.reset()
                map.update()


    # DRAW STUFF
    map.draw(window)

    # DISPLAY FRAME
    pygame.display.update()
