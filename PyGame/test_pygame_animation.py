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

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
rect_offset_x = 1
rect_offset_y = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    if rect_y > 450 or rect_y < 0:
        rect_offset_y *= -1
        n = random.randrange(1, 5)
    if rect_x > 650 or rect_x < 0:
        rect_offset_x *= -1
        n = random.randrange(1, 5)
    pygame.draw.rect(screen, colors[n], [rect_x, rect_y, 50, 50])

    rect_x += 5 * rect_offset_x
    rect_y += 5 * rect_offset_y



    pygame.display.flip()

    clock.tick(30)

pygame.quit()
