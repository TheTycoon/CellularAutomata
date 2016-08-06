import pygame


class Cell:
    def __init__(self, size, rows, columns, position, state):
        self.row = int(position / rows)
        self.column = position % columns
        self.rect = pygame.Rect(size * self.column, size * self.row, size, size)

        if state < 45:
            self.state = False
        elif self.row == 0 or self.column == 0:
            self.state = False
        elif self.row == rows - 1 or self.column == columns - 1:
            self.state = False
        else:
            self.state = True


# determine if a cell lives or dies based on how many neighborhood cells are alive
def generate(cellList, i, rows, columns):
    if cellList[i].row != 0 and cellList[i].row != rows - 1 and cellList[i].column != 0 and cellList[i].column != columns - 1:
        if cellList[i].state + cellList[i - 1].state + cellList[i + 1].state \
                + cellList[i + columns].state + cellList[i - columns].state \
                + cellList[i + columns + 1].state + cellList[i + columns - 1].state \
                + cellList[i - columns + 1].state + cellList[i - columns - 1].state > 4:
            cellList[i].state = True
        else:
            cellList[i].state = False