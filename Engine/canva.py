import pygame
from .grid import Grid

class Canva:
    def __init__(self, width, height, row, col):
        self.width = width * col
        self.height = height * row
        self.start = [0, 0]
        self.scroll = [0, 0]

        self.grid = Grid(width, width, row, col, self.start)
        self.canva = pygame.Rect(self.start[0], self.start[1], self.width, self.height)
        
        self.hold = False
        self.draw_grid = False

    def draw(self,screen):
        if self.draw_grid: self.grid.draw(screen, self.scroll)

    def toggleGrid(self):
        self.draw_grid = not self.draw_grid

    def isDrag(self, event_list, mouse):
        # print(self.hold)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.canva.collidepoint(mouse):
                    self.hold = not self.hold

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.hold = False