import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 1000))

 #rect(screen, (color), (x , y , width, height))
 #circle(screen, (color), (x c, y c), radius)
 #polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)])

#backgr
rect(screen, (178, 239, 255), (0, 0, 1500, 500)) #sky
rect(screen, (0, 232, 87), (0, 500, 1500, 500)) #grass
#ice cream
polygon(screen, (255, 206, 25), [(150, 510), (210, 450), (250, 560)])
circle(screen, (155, 27, 0), (150, 485), 29)
circle(screen, (255, 55, 53), (190, 455), 29)
circle(screen, (255, 255, 255), (150, 440), 29)
#balloon
line(screen, (0, 0, 0), (1240, 332), (1270, 180), 2)
polygon(screen, (255, 55, 53), [(1270, 180), (1240, 100), (1325, 130)])
circle(screen, (255, 55, 53), (1268, 90), 29)
circle(screen, (255, 55, 53), (1310, 105), 29)
#лох слева
line(screen, (0, 0, 0), (500, 300), (250, 550), 2) #arm left left
line(screen, (0, 0, 0), (500, 300), (750, 550), 2) #arm left right
lines(screen, (0, 0, 0), False, [(470, 650), (420, 900), (360, 920)], 2) #leg l l
lines(screen, (0, 0, 0), False, [(530, 650), (550, 900), (610, 920)], 2) #leg l r
ellipse(screen, (139, 153, 255), (410, 300, 180, 400)) #body left
#лох справа
line(screen, (0, 0, 0), (750, 550), (1000, 330), 2) #arm right left
lines(screen, (0, 0, 0), False, [(1000, 330), (1150, 430), (1250, 300)], 2) #arm right right
lines(screen, (0, 0, 0), False, [(950, 700), (950, 900), (890, 910)], 2) #leg r l
lines(screen, (0, 0, 0), False, [(1050, 700), (1050, 900), (1110, 910)], 2) #leg r r
polygon(screen, (255, 181, 245), [(1000, 300), (800, 700), (1200, 700)]) #body right 
circle(screen, (255, 237, 218), (500, 250), 75) #башка слева
circle(screen, (255, 237, 218), (1000, 250), 75) #башка справа





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
