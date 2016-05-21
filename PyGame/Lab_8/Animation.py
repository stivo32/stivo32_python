__author__ = 'k_eryomenko'
import pygame
import random
import math
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

def person(deg):
    alfa = 0
    head_x = 150
    head_y = 100
    scale = 0.5
    head_radius = int(20*scale)
    body_start_y = int(head_y+head_radius)
    body_end_y = int(body_start_y + 100*scale)
    leg_left_end_x = int(head_x-20*scale)
    leg_right_end_x = int(head_x+20*scale)
    leg_end_y = int(body_end_y+120*scale)
    hand_start_y = int(body_start_y+20*scale)
    hand_length = int(90*scale)
    #draw head
    pygame.draw.circle(screen, white, (head_x, head_y), head_radius, 4)
    #draw body
    pygame.draw.line(screen, white, (head_x, body_start_y), (head_x, body_end_y) , 4)
    #draw left leg
    pygame.draw.line(screen, white, (head_x, body_end_y), (leg_left_end_x, leg_end_y), 4)
    #draw right leg
    pygame.draw.line(screen, white, (head_x, body_end_y), (leg_right_end_x, leg_end_y), 4)
    if deg<30:
        alfa = (60-deg*4)*math.pi/180
    else:
        alfa = (-180+deg*4)*math.pi/180
    pygame.draw.line(screen, white, (head_x, hand_start_y), (head_x-hand_length*math.cos(alfa), hand_start_y+hand_length*math.sin(alfa)), 4)
    pygame.draw.line(screen, white, (head_x, hand_start_y), (head_x+hand_length*math.cos(alfa), hand_start_y+hand_length*math.sin(alfa)), 4)



pygame.init()

size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False
color = black
clock = pygame.time.Clock()
hour=0
deg=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(color)
    color = skyColor(hour)
    person(deg)
    pygame.display.flip()

    clock.tick(5)
    hour+=1
    if hour==96:
        hour=0
    deg+=1
    if deg==60:
        deg=0
pygame.quit()


