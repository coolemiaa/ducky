import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.update()


duck=pygame.image.load('duckcollecting.py/duck.png')
fish=pygame.image.load('duckcollecting.py/fishie.png')
duckx=200
ducky=400


pygame.display.update()



run=True #zodat het scherm blijft en quit=false als je sluit sluit het
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False

        if i.type==pygame.KEYDOWN:#PRESS ANY KEYS KEY DOWN WILL BE GENERATED
            if i.key==K_UP:
                ducky=ducky-10

            elif i.key==K_DOWN:
                ducky=ducky+10

            elif i.key==K_LEFT:
                duckx=duckx-10

            elif i.key==K_RIGHT:
                duckx=duckx+10




    ducky=ducky+0.1
    screen.fill('pink')
    screen.blit(fish,(300,300))
    screen.blit(duck,(duckx,ducky))

    pygame.display.update()




