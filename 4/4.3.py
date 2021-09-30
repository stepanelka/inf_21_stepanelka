import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2500, 1500)) #1500/1000

 #rect(screen, (color), (x , y , width, height))
 #circle(screen, (color), (x c, y c), radius)
 #polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)])

#backgr
rect(screen, (178, 239, 255), (0, 0, 3000, 1000)) #sky
rect(screen, (0, 232, 87), (0, 750, 3000, 1000)) #grass
#ice cream отразить отн 1250 у+500
polygon(screen, (255, 206, 25), [(2350, 1010), (2290, 950), (2250, 1060)])
circle(screen, (155, 27, 0), (2350, 985), 29)
circle(screen, (255, 55, 53), (2310, 955), 29)
circle(screen, (255, 255, 255), (2350, 940), 29)
#balloon отразить отн 750 у+250
line(screen, (0, 0, 0), (260, 1082), (230, 930), 2)
polygon(screen, (255, 55, 53), [(230, 930), (260, 850), (175, 880)])
circle(screen, (255, 55, 53), (232, 840), 29)
circle(screen, (255, 55, 53), (190, 855), 29)
#лох слева
line(screen, (0, 0, 0), (500, 800), (250, 1050), 2) #arm left left
line(screen, (0, 0, 0), (500, 800), (750, 1050), 2) #arm left right
lines(screen, (0, 0, 0), False, [(470, 1150), (420, 1400), (360, 1420)], 2) #leg l l
lines(screen, (0, 0, 0), False, [(530, 1150), (550, 1400), (610, 1420)], 2) #leg l r
ellipse(screen, (139, 153, 255), (410, 800, 180, 400)) #body left
circle(screen, (255, 237, 218), (500, 750), 75) #башка слева
#отраженный лох слева отразить отн 1250
line(screen, (0, 0, 0), (2000, 800), (2250, 1050), 2) #arm left left
line(screen, (0, 0, 0), (2000, 800), (1750, 1050), 2) #arm left right
lines(screen, (0, 0, 0), False, [(2030, 1150), (2080, 1400), (2140, 1420)], 2) #leg l l
lines(screen, (0, 0, 0), False, [(1970, 1150), (1950, 1400), (1890, 1420)], 2) #leg l r
ellipse(screen, (139, 153, 255), (1910, 800, 180, 400)) #body left
circle(screen, (255, 237, 218), (2000, 750), 75) #башка слева
#лох справа
line(screen, (0, 0, 0), (750, 1050), (1000, 830), 2) #arm right left
lines(screen, (0, 0, 0), False, [(1000, 830), (1150, 930), (1250, 800)], 2) #arm right right
lines(screen, (0, 0, 0), False, [(950, 1200), (950, 1400), (890, 1410)], 2) #leg r l
lines(screen, (0, 0, 0), False, [(1050, 1200), (1050, 1400), (1110, 1410)], 2) #leg r r
polygon(screen, (255, 181, 245), [(1000, 800), (800, 1200), (1200, 1200)]) #body right 
circle(screen, (255, 237, 218), (1000, 750), 75) #башка справа
#отраженный лох справа отразить отн 1250
line(screen, (0, 0, 0), (1750, 1050), (1500, 830), 2) #arm right left
lines(screen, (0, 0, 0), False, [(1500, 830), (1350, 930), (1250, 800)], 2) #arm right right
lines(screen, (0, 0, 0), False, [(1550, 1200), (1550, 1400), (1610, 1410)], 2) #leg r l
lines(screen, (0, 0, 0), False, [(1450, 1200), (1450, 1400), (1390, 1410)], 2) #leg r r
polygon(screen, (255, 181, 245), [(1500, 800), (1700, 1200), (1300, 1200)]) #body right 
circle(screen, (255, 237, 218), (1500, 750), 75) #башка справа
#ice cream in the air
line(screen, (0, 0, 0), (1240, 950), (1260, 300), 2)
polygon(screen, (255, 206, 25), [(1200, 190), (1260, 320), (1310, 190)])
circle(screen, (155, 27, 0), (1225, 175), 40)
circle(screen, (255, 55, 53), (1295, 175), 40)
circle(screen, (255, 255, 255), (1260, 140), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
