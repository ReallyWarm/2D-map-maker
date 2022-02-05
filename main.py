import pygame, sys
import yaml
from Engine import Canva

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Map Maker')

with open('./setting.yaml') as f:
    setting = yaml.safe_load(f.read())

screen = pygame.display.set_mode([1280, 960], 0, 32)
canva = Canva(32, 32, 15, 15, setting['canva'])
color = setting['color']
tile = setting['tile']

file_path = "./image/Tile32.bmp"

def displayAll(screen):
    # screen.fill(color['black'])
    canva.display()

if __name__ == '__main__':
    draw_grid = 0

    run = 1
    while run:
        screen.fill(color['black'])
        mouse = pygame.mouse.get_pos()
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                run = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = 0
                if event.key == pygame.K_q:
                    canva.toggleGrid()
                if event.key == pygame.K_n:
                    canva.snapGrid()
                if event.key == pygame.K_o:
                    canva.loadSprite(file_path, tile['size'], 2, 9, tile['colorkey'])

                # test key
                if event.key == pygame.K_1:
                    canva.test_1()
                if event.key == pygame.K_2:
                    canva.test_2()
            
            if pygame.mouse.get_pressed()[0]:
                pass

        canva.update(event_list, mouse)
        canva.active(mouse)
        displayAll(screen)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    sys.exit()