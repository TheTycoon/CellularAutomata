import pygame
import settings
from random import randint


class Cell:
    def __init__(self, column, row, state):
        self.column = column
        self.row = row
        self.neighborhood = []
        self.rect = pygame.Rect(self.column * settings.TILESIZE, self.row * settings.TILESIZE,
                                settings.TILESIZE, settings.TILESIZE)
        '''
        Below are your initial settings for using the cave generating algorithm
        ~55% start off Alive, ~45% Dead
        All cells on the outer edges of map are Dead
        '''
        if self.row == 0 or self.column == 0 or self.row == settings.ROWS - 1 or self.column == settings.COLUMNS - 1:
            self.state = False
        elif state < 45:
            self.state = False
        else:
            self.state = True
        self.temp_state = self.state

    def set_neighborhood(self, grid):
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row))
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row + 1))
        self.neighborhood.append(grid.get_cell(self.column, self.row + 1))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row + 1))

    def check_neighborhood(self):
        living_cells = 0
        for i in range(len(self.neighborhood)):
            living_cells += self.neighborhood[i].state
        return living_cells


class Map:
    def __init__(self):
        self.grid = self.set_grid()
        self.create_neighborhoods()

    def set_grid(self):
        grid = [
                   [Cell(column, row, randint(0, 100)) for row in range(settings.ROWS)]
                   for column in range(settings.COLUMNS)
               ]
        '''
        for column in range(settings.COLUMNS):
            grid.append([])
            for row in range(settings.ROWS):
                grid[column].append(Cell(column, row, randint(0, 100)))
        '''
        return grid

    def get_cell(self, column, row):
        try:
            return self.grid[column][row]
        except LookupError:
            return Cell(settings.COLUMNS + 1, settings.ROWS + 1, False)

    def create_neighborhoods(self):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                cell = self.get_cell(column, row)
                cell.set_neighborhood(self)

    '''
    # this function removes the common 4x4 pillar with corners missing after one pass
    def remove_pillars(self):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                if self.check_pillar(column, row) is True:
                    rows = []
                    for i in range(4):
                        temp_row = [
                            self.get_cell(column, row + i), self.get_cell(column + 1, row + i),
                            self.get_cell(column + 2, row + i), self.get_cell(column + 3, row + i)
                        ]
                        rows.append(temp_row)

                    for test_row in rows:
                        for cell in test_row:
                            cell.temp_state = True
        self.update()

    def check_pillar(self, column, row):
        rows = []
        for i in range(4):
            temp_row = [
                self.get_cell(column, row + i), self.get_cell(column + 1, row + i), self.get_cell(column + 2, row + i),
                self.get_cell(column + 3, row + i)
            ]
            rows.append(temp_row)                #### ?????

        for cell in rows[1]:
            if cell.state is True:
                return False
        for cell in rows[2]:
            if cell.state is True:
                return False

        if not (rows[0][0].state is True and rows[0][1].state is False and rows[0][2].state is False and rows[0][3].state is True):
            return False
        elif not (rows[3][0].state is True and rows[3][1].state is False and rows[3][2].state is False and rows[3][3].state is True):
            return False
        else:
            return True
    '''

    def cave_generate(self):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                cell = self.get_cell(column, row)
                if cell.state + cell.check_neighborhood() >= 5:
                    cell.temp_state = True
                else:
                    cell.temp_state = False

    def game_of_life_generate(self):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                cell = self.get_cell(column, row)
                if cell.state is True:
                    if cell.check_neighborhood() < 2:
                        cell.temp_state = False
                    elif cell.check_neighborhood() == 2 or cell.check_neighborhood() == 3:
                        cell.temp_state = True
                    elif cell.check_neighborhood() > 3:
                        cell.temp_state = False
                elif cell.state is False and cell.check_neighborhood() == 3:
                    cell.temp_state = True

    def update(self):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                cell = self.get_cell(column, row)
                cell.state = cell.temp_state

    def reset(self):
        self.grid = self.set_grid()
        self.create_neighborhoods()

    def draw(self, screen):
        for row in range(settings.ROWS):
            for column in range(settings.COLUMNS):
                cell = self.get_cell(column, row)
                if cell.state is True:
                    pygame.draw.rect(screen, settings.WHITE, cell.rect, 0)
                else:
                    pygame.draw.rect(screen, settings.BLACK, cell.rect, 0)


