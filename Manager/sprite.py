import pygame
from .spritesheet import SpriteSheet

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file_path, size, row, col, colorkey):
        super().__init__()
        self.sprites = []
        self.load(file_path, size, row, col, colorkey)

    def load(self, file_path, size, row, col, colorkey):
        full_sprite = SpriteSheet(file_path)
        for r in range(row):
            for c in range(col):
                self.sprites.append(full_sprite.sprite_at((size[0]*c, size[1]*r, size[0], size[1]), colorkey))

    def get(self):
        return self.sprites

    def getAt(self, index):
        try:
            return self.sprites[index]
        except IndexError:
            return None