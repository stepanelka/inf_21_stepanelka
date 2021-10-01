import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2500, 1500))

#colors 
black = (0, 0, 0)
skyblue = (178, 239, 255)
green = (0, 232, 87)
red = (255, 55, 53)
orange = (255, 206, 25)
pink = (255, 181, 245)
skin = (255, 237, 218)
white = (255, 255, 255)
blue = (139, 153, 255)
brown = (155, 27, 0)

#background
rect(screen, skyblue, (0, 0, 3000, 1000)) #sky
rect(screen, green, (0, 750, 3000, 1000)) #grass
#ice cream
polygon(screen, orange, [(2350, 1010), (2290, 950), (2250, 1060)])
circle(screen, brown, (2350, 985), 29)
circle(screen, red, (2310, 955), 29)
circle(screen, white, (2350, 940), 29)
#balloon
line(screen, black, (260, 1082), (230, 930), 2)
polygon(screen, red, [(230, 930), (260, 850), (175, 880)])
circle(screen, red, (232, 840), 29)
circle(screen, red, (190, 855), 29)
#лох слева
line(screen, black, (500, 800), (250, 1050), 2) #arm left
line(screen, black, (500, 800), (750, 1050), 2) #arm right
lines(screen, black, False, [(470, 1150), (420, 1400), (360, 1420)], 2) #leg left
lines(screen, black, False, [(530, 1150), (550, 1400), (610, 1420)], 2) #leg right
ellipse(screen, blue, (410, 800, 180, 400)) #body left
circle(screen, skin, (500, 750), 75) #башка 
#отраженный лох слева 
line(screen, black, (2000, 800), (2250, 1050), 2) #arm left
line(screen, black, (2000, 800), (1750, 1050), 2) #arm right
lines(screen, black, False, [(2030, 1150), (2080, 1400), (2140, 1420)], 2) #leg right
lines(screen, black, False, [(1970, 1150), (1950, 1400), (1890, 1420)], 2) #leg left
ellipse(screen, blue, (1910, 800, 180, 400)) #body left
circle(screen, skin, (2000, 750), 75) #башка 
#лох справа
line(screen, black, (750, 1050), (1000, 830), 2) #arm left
lines(screen, black, False, [(1000, 830), (1150, 930), (1250, 800)], 2) #arm right
lines(screen, black, False, [(950, 1200), (950, 1400), (890, 1410)], 2) #leg left
lines(screen, black, False, [(1050, 1200), (1050, 1400), (1110, 1410)], 2) #leg right
polygon(screen, pink, [(1000, 800), (800, 1200), (1200, 1200)]) #body right 
circle(screen, skin, (1000, 750), 75) #башка 
#отраженный лох справа
line(screen, black, (1750, 1050), (1500, 830), 2) #arm left
lines(screen, black, False, [(1500, 830), (1350, 930), (1250, 800)], 2) #arm right
lines(screen, black, False, [(1550, 1200), (1550, 1400), (1610, 1410)], 2) #leg right
lines(screen, black, False, [(1450, 1200), (1450, 1400), (1390, 1410)], 2) #leg left
polygon(screen, pink, [(1500, 800), (1700, 1200), (1300, 1200)]) #body right 
circle(screen, skin, (1500, 750), 75) #башка 
#ice cream balloon 
line(screen, black, (1240, 950), (1260, 300), 2)
polygon(screen, orange, [(1200, 190), (1260, 320), (1310, 190)])
circle(screen, brown, (1225, 175), 40)
circle(screen, red, (1295, 175), 40)
circle(screen, white, (1260, 140), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
