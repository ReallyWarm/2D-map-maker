import pygame
from .grid import Grid
from .draw import Draw
from Manager import Sprite
from .debug import debug

class Canva:
    def __init__(self, screen, width, height, row, col, setting):
        self.screen = screen
        self.width = width * col
        self.height = height * row
        self.cell_w = width
        self.cell_h = height
        self.cell_col = col
        self.cell_row = row
        self.setting = setting

        # Start position
        self.scr_offset = screen.get_offset()
        self.offset = [50, 50]
        self.rect_pos = [self.scr_offset[0] + self.offset[0], self.scr_offset[1] + self.offset[1]]

        # Canva
        self.rect = pygame.Rect(self.rect_pos[0], self.rect_pos[1], self.width, self.height)
        self.canva = pygame.Surface(self.rect.size)
        self.canva.fill(setting['background'])

        # Grids
        self.grid = Grid(screen, width, width, row, col, self.offset)

        # Drawing previews
        self.preview = pygame.Surface((width, height))
        self.preview.fill(setting['preview'])

        # Sprites to draw
        self.sprites_data = []
        self.sprites_draw = pygame.sprite.Group()
        self.index_image = 0

        # Offsets and Coordinates
        self.scroll = [0, 0]
        self.mouse_pos = [0, 0]
        self.draw_pos = [0, 0]
        
        # Actions
        self.hover = False
        self.hold = False
        self.drawing = False
        self.draw_grid = False
        self.snap_grid = False

    def update(self, event_list, mouse):
        self.hover = self.rect.collidepoint(mouse)

        self.drawing = False
        
        for event in event_list:
            # If left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hover:
                self.drawing = True

            # If right click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and self.hover:
                self.hold = not self.hold
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.hold = False

    def display(self):
        # Show Canva background
        self.screen.blit(self.canva, self.offset)

        # Show Grids
        if self.draw_grid: 
            self.grid.display(self.scroll, self.setting)
        # Show drawing previews
        if self.hover and self.sprites_data:
            self.screen.blit(self.preview, self.draw_pos)

        # Show Drawed Sprites
        self.sprites_draw.draw(self.screen)

    def active(self, mouse):
        self.mouse_pos[0], self.mouse_pos[1] = mouse[0], mouse[1]

        if self.hover:
            # Get collumn and row of Canva
            if self.snap_grid:
                snap = self.grid.snap(self.mouse_pos, self.scroll)             
                # Get snap drawing positions
                if 0 <= snap[0] <= self.cell_col-1 and 0 <= snap[1] <= self.cell_row-1:
                    self.colrow_pos = snap
                    # Position in surface
                    self.draw_pos[0] = self.colrow_pos[0] * self.cell_w + self.offset[0]
                    self.draw_pos[1] = self.colrow_pos[1] * self.cell_h + self.offset[1]
                    # debug(self.draw_pos)
            # Get free drawing positions
            else:
                free_Dx = self.mouse_pos[0] - self.scr_offset[0]
                free_Dy = self.mouse_pos[1] - self.scr_offset[1]
                max_posW = self.width + self.offset[0] - self.cell_w
                max_posH = self.height + self.offset[1] - self.cell_h
                # Currently in the canva
                if free_Dx < max_posW and free_Dy < max_posH:
                    self.draw_pos[0] = free_Dx
                    self.draw_pos[1] = free_Dy
                else:
                    # Bottom right
                    if free_Dx >= max_posW and free_Dy >= max_posH:
                        self.draw_pos[0] = max_posW
                        self.draw_pos[1] = max_posH
                    # Rightmost
                    elif free_Dx >= max_posW:
                        self.draw_pos[0] = max_posW
                        self.draw_pos[1] = free_Dy
                    # Bottommost
                    elif free_Dy >= max_posH:
                        self.draw_pos[0] = free_Dx
                        self.draw_pos[1] = max_posH
                # debug(self.draw_pos)
        
        # debug(self.drawing)
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
