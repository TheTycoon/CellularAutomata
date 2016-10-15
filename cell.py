import pygame

import settings


class Cell:
    def __init__(self, row, column, state):
        self.row = row
        self.column = column

        self.temp_state = False

        if state < 45:
            self.state = False
        elif self.row == 0 or self.column == 0 or self.row == settings.ROWS - 1 or self.column == settings.COLUMNS - 1:
            self.state = False
        else:
            self.state = True

        self.rect = pygame.Rect(self.column * settings.TILESIZE, self.row * settings.TILESIZE,
                                settings.TILESIZE, settings.TILESIZE)

    def set_neighborhood(self, grid):
        self.top_left = grid[self.column - 1][self.row - 1]
        self.top = grid[self.column][self.row -1]
        self.top_right = grid[self.column + 1][self.row - 1]
        self.left = grid[self.column - 1][self.row]
        self.right = grid[self.column + 1][self.row]
        self.bottom_left = grid[self.column - 1][self.row + 1]
        self.bottom = grid[self.column][self.row + 1]
        self.bottom_right = grid[self.column + 1][self.row + 1]

    def check_neighborhood(self):
        living_cells = self.state + self.top_left.state + self.top.state + self.top_right.state + self.left.state \
                       + self.right.state + self.bottom_left.state + self.bottom.state + self.bottom_right.state
        return living_cells

    def cave_generate(self):
        if self.check_neighborhood() >= 5:
            self.temp_state = True
        else:
            self.temp_state = False

    def game_of_life_generate(self):
        if self.state is True:
            if self.check_neighborhood() < 3:
                self.temp_state = False
            elif self.check_neighborhood() == 3 or self.check_neighborhood() == 4:
                self.temp_state = True
            elif self.check_neighborhood() > 4:
                self.temp_state = False
        elif self.state is False and self.check_neighborhood() == 3:
            self.temp_state = True

    def update(self):
        self.state = self.temp_state


