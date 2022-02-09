import pygame, sys
import yaml
from Engine import Canva

pygame.init()
pygame.display.set_caption('Map Maker')
clock = pygame.time.Clock()

# Get settings
with open('./setting.yaml') as f:
    setting = yaml.safe_load(f.read())

win_size = setting['display']
color = setting['color']
tile = setting['tile']

# Display surface
display = pygame.display.set_mode(win_size, 0, 32)
screen = pygame.display.get_surface()

# Subsurface in sections
sect1 = pygame.Rect(0, 0, win_size[0] // 5, win_size[1])
sect2 = pygame.Rect(win_size[0] // 5, 0, int(win_size[0]*4 / 5), win_size[1])
scr1 = screen.subsurface(sect1) # Menu
scr2 = screen.subsurface(sect2) # Canva

# bg2 = scr2.copy()
# bg2.fill(color['white'])

canva = Canva(scr2, 32, 32, 15, 15, setting['canva'])

file_path = "./image/Tile32.bmp"

def displayAll():
    # screen.fill(color['black'])
    
    # screen.blit(scr2, (int(win_size[0]*4 / 5), win_size[1]))
    canva.display()

def main():
    run = 1
    while run:
        # screen.fill(color['black'])
        scr2.fill(color['white'])
        # screen.blit(bg2, (win_size[0] // 5, 0))

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

        # scr1 = scr1.copy()
        # scr2 = scr2.copy()
        displayAll()
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()