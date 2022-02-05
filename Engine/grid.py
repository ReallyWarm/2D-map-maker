import pygame
from .debug import debug

class Grid:
    def __init__(self, width, height, row, col, canva_pos):
        self.screen = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.start = canva_pos


    def snap(self, mouse, scroll):
        snap_col = int((mouse[0] - self.start[0]) / self.width)
        snap_row = int((mouse[1] - self.start[1]) / self.height)
        snap_colrow = [snap_col, snap_row]

        # debug(snap_colrow)
        return snap_colrow

    def display(self, scroll, color):
        endRowX = (self.width * self.col) + self.start[0]
        for i in range(self.row + 1):
            rowY = (self.height * i) + self.start[1]
            pygame.draw.line(self.screen, color['grid'], (self.start[0], rowY), (endRowX, rowY))

        endColY = (self.height * self.row) + self.start[1]
        for i in range(self.col + 1):
            colX = (self.width * i) + self.start[0]
            pygame.draw.line(self.screen, color['grid'], (colX, self.start[1]), (colX, endColY))
