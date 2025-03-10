import pygame
import random
import sys


##함수 선언 부분##
#@기능 2-5
def paintEntity(entity, x, y) :
    monitor.blit(entity,(int(x), int(y)))
#@기능 5-4
def writeScore(score) :
    myfont = pygame.font.Font('NanumGothic.ttf',20)
    txt = myfont.render(u'파괴한 우주괴물 수 :' + str(score), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight - 40))


def playGame() :
    global monitor, ship, monster, missile

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    #@기능 2-2
    shipX = swidth / 2
    shipY = sheight * 0.8
    dx, dy = 0,0
    #@기능 3-2
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size
    monsterX = 0
    monsterY = random.randrange(0, int(swidth * 0.3))
    monsterSpeed = random.randrange(1, 5)
    #@기능 4-2
    missileX, missileY = None, None
    #@기능 5-1
    fireCount = 0

    #무한 반복
    while True :
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get() :
            if e.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()
            
            #@기능 2-3
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = -5
                elif e.key == pygame.K_DOWN : dy = +5
                #@기능 4-3
                elif e.key == pygame.K_SPACE :
                    if missileX == None :
                        missileX = shipX + shipSize[0] / 2
                        missileY = shipY

                if e.type in [pygame.KEYUP] :   
                    if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                        or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0.0
        #@기능 2-4
        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
            and (sheight / 2 < shipY + dy and shipY + dy <=sheight - shipSize[1]) :

            shipX += dx
            shipY += dy
        paintEntity(ship, shipX, shipY)

        #@기능 3-3
        monsterX += monsterSpeed
        if monsterX > swidth :
            monsterX = 0
            monsterY = random.randrange(0, int(swidth * 0.3))
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1,5)
        
        paintEntity(monster, monsterX, monsterY)
        #@기능 4-4
        if missileX != None :
            missileY -= 10
            if missileY < 0 :
                missileX, missileY = None, None
        if missileX != None :
            paintEntity(missile, missileX, missileY)
            #@기능 5-2
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and\
                (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                fireCount += 1

                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = 0
                monsterY = random.randrange(0, int(swidth * 0.3))
                monsterSpeed = random.randrange(1, 5)

                missileX, missileY = None, None

        #@기능 5-3
        writeScore(fireCount)
        
        
        pygame.display.update()
        

r,g,b = [0] * 3
swidth, sheight = 500,700
monitor = None
ship, shipSize = None,0

monsterImage = ['monster01.png', 'monster02.png','monster03.png','monster04.png'\
                'monster05.png','monster06.png','monster07.png','monster08.png'\
                'monster09.png','monster10.png']
monster = None

missile = None

pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load('ship02.png')
shipSize = ship.get_rect().size

missile = pygame.image.load('missile.png')


playGame()