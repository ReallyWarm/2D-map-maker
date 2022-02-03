import pygame

class Grid:
    def __init__(self, width, height, row, col, start):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.start = start

    def draw(self, screen, scroll):
        for i in range(self.row + 1):
            rowY = self.height * i
            endRowX = self.width * self.col
            pygame.draw.line(screen, (255,255,255), (0, rowY), (endRowX, rowY))
        for i in range(self.col + 1):
            colX = self.width * i
            endColY = self.height * self.row
            pygame.draw.line(screen, (255,255,255), (colX, 0), (colX, endColY))
