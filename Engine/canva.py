import pygame
from .grid import Grid
from .draw import Draw
from .debug import debug
from Manager import Sprite

class Canva:
    def __init__(self, width, height, row, col, setting):
        self.screen = pygame.display.get_surface()
        self.width = width * col
        self.height = height * row
        self.cell_w = width
        self.cell_h = height
        self.cell_col = col
        self.cell_row = row
        self.setting = setting

        self.start = [100, 100]
        self.scroll = [0, 0]
        self.draw_pos = None

        self.canva = pygame.Rect(self.start[0], self.start[1], self.width, self.height)
        self.grid = Grid(width, width, row, col, self.canva.topleft)
        self.preview = pygame.Rect(self.start[0], self.start[1], width, height)

        self.sprites_data = []
        self.sprites_draw = pygame.sprite.Group()
        self.index_image = 0
        
        self.draw_grid = False
        self.snap_grid = False

        self.hover = False
        self.hold = False
        self.drawing = False

    def update(self, event_list, mouse):
        self.hover = self.canva.collidepoint(mouse)

        self.drawing = False
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hover:
                self.drawing = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and self.hover:
                self.hold = not self.hold
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.hold = False

    def display(self):
        pygame.draw.rect(self.screen, self.setting['background'], self.canva)

        if self.draw_grid: 
            self.grid.display(self.scroll, self.setting)
        if self.snap_grid and self.hover:
            pygame.draw.rect(self.screen, [255,100,100], self.preview)
        self.sprites_draw.draw(self.screen)

    def active(self, mouse):
        self.draw_pos = mouse

        if self.snap_grid and self.hover:
            snap = self.grid.snap(self.draw_pos, self.scroll)
            if 0 <= snap[0] <= self.cell_col-1 and 0 <= snap[1] <= self.cell_row-1:
                self.colrow_pos = snap
                self.draw_pos = [self.colrow_pos[0] * self.cell_w + self.start[0],
                                 self.colrow_pos[1] * self.cell_h + self.start[0]]

                self.preview.x = self.draw_pos[0]
                self.preview.y = self.draw_pos[1]
        
        debug(self.drawing)
        if self.drawing and self.sprites_data:
            Draw((self.draw_pos), self.sprites_data[0].getAt(self.index_image), [self.sprites_draw])

    def loadSprite(self, file_name, size, row=1, col=5, colorkey=None):
        self.sprites_data.append(Sprite(file_name, size, row, col, colorkey))
        # print(self.sprites_data[0].get())
        # print(self.sprites_data[0].getAt(10))

    def toggleGrid(self):
        self.draw_grid = not self.draw_grid
        if not self.draw_grid: 
            self.snap_grid = False

    def snapGrid(self):
        if self.draw_grid: 
            self.snap_grid = not self.snap_grid

    # test image
    def test_1(self):
        self.index_image = 0
    def test_2(self):
        self.index_image = 17
