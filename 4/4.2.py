import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 1000))

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
rect(screen, skyblue, (0, 0, 1500, 500)) #sky
rect(screen, green, (0, 500, 1500, 500)) #grass
#ice cream
polygon(screen, orange, [(150, 510), (210, 450), (250, 560)])
circle(screen, brown, (150, 485), 29)
circle(screen, red, (190, 455), 29)
circle(screen, white, (150, 440), 29)
#balloon
line(screen, black, (1240, 332), (1270, 180), 2)
polygon(screen, red, [(1270, 180), (1240, 100), (1325, 130)])
circle(screen, red, (1268, 90), 29)
circle(screen, red, (1310, 105), 29)
#лох слева
line(screen, black, (500, 300), (250, 550), 2) #arm left
line(screen, black, (500, 300), (750, 550), 2) #arm right
lines(screen, black, False, [(470, 650), (420, 900), (360, 920)], 2) #leg left
lines(screen, black, False, [(530, 650), (550, 900), (610, 920)], 2) #leg right
ellipse(screen, blue, (410, 300, 180, 400)) #body left
circle(screen, skin, (500, 250), 75) #башка
#лох справа
line(screen, black, (750, 550), (1000, 330), 2) #arm left
lines(screen, black, False, [(1000, 330), (1150, 430), (1250, 300)], 2) #arm right
lines(screen, black, False, [(950, 700), (950, 900), (890, 910)], 2) #leg left
lines(screen, black, False, [(1050, 700), (1050, 900), (1110, 910)], 2) #leg right
polygon(screen, pink, [(1000, 300), (800, 700), (1200, 700)]) #body right 
circle(screen, skin, (1000, 250), 75) #башка

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
