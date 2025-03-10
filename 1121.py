import sys 
import random
import pygame

def playgmae():
    global monitor

    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)


    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        print('~',end=' ')

r,g,b = [0] * 3 
swidth,sheight = 500,700
monitor = None 

pygame.init()
monitor = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

playgmae()




