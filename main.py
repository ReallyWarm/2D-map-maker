import pygame, sys
from Engine import Canva

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Map Maker')
screen = pygame.display.set_mode([1280, 960], 0, 32)
canva = Canva(32, 32, 15, 15)

def displayAll(screen):
    screen.fill((0,0,0))
    canva.draw(screen)

if __name__ == '__main__':
    draw_grid = 0

    run = 1
    while run:
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
            
            if pygame.mouse.get_pressed()[0]:
                pass
        
        canva.isDrag(event_list, mouse)

        clock.tick(60)
        displayAll(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()