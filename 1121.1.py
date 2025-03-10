import pygame 
import random 
import sys 

def painEntity(entity,x,y):
    monitor.blit(entity,(int(x),int(y)))

def playgame():
    global monitor,ship 
    r = random.randrange(0,256)
    g = random.randrange(0,256) 
    b = random.randrange(0,256) 

    shipX = swidth / 2 
    shipY = sheight * 0.8
    dx , dy = 0,0

    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT: dx = -5
                elif e.key == pygame.K_RIGHT: dx = +5 
                elif e.key == pygame.K_UP: dy = -5 
                elif e.key == pygame.K_DOWN: dy = +5 

            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or e.key == pygame.K_UP or e.key == pygame.K_DOWN: dx,dy = 0,0 
            if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) and (sheight / 2 < shipY + dy <= sheight - shipSize[1]):

                shipX += dx 
                shipY += dy 
            painEntity(ship,shipX,shipY)

            pygame.display.update()
            print('~',end='')

r,g,b = [0] * 3 
swidth, sheight = 500 , 700 
monitor = None 
ship , shipSize = None , 0

pygame.init()
monitor = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load("file/ship02.png")
shipSize = ship.get_rect().size

playgame()