__author__ = 'k_eryomenko'
import pygame
import random
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)
colors = [white, green, red, blue, braun]
pi = 3.141592653
n = 1
x_offset = random.randrange(1, 6)
y_offset = random.randrange(1, 6)

def skyColor(hour):
    if hour>47:
        sky_color = (   0,   0,   0)
    else:
        if hour<=12*2:
            sky_color = (0, 2.5*(hour), 10*(hour))
            solarDraw(hour)
        else:
            sky_color = (0, 60-(2.5*(hour-24)), 240-(10*(hour-24)))
    print(hour, sky_color)
    return sky_color

def solarDraw(hour):
    YELLOW = (255, 255, 0)
    x = 0+size[0]/2/24*(hour)
    y = 0+x
    print(x,y)
    pygame.draw.circle(screen, YELLOW, (int(x), int(y)) , 20)


pygame.init()

size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False
color = black
clock = pygame.time.Clock()
hour=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(color)
    color = skyColor(hour)
    pygame.display.flip()

    clock.tick(5)
    hour+=1
    if hour==96:
        hour=0
pygame.quit()


