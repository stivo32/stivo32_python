__author__ = 'k_eryomenko'
import pygame
import random

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)


pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
done = True
clock = pygame.time.Clock()

star_list = []
for i in range(70):
        x = random.randrange(0, 700)
        y = random.randrange(0, 500)
        star_list.append([x, y])

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.fill(black)

    for i in range(len(star_list)):
        pygame.draw.circle(screen, white, star_list[i], 2)
        star_list[i][1]+= 1
        if star_list[i][1] > size[1]:
            y = random.randrange(-50, -10)
            star_list[i][1] = y
            x = random.randrange(0, size[0])
            star_list[i][0] = x

    pygame.display.flip()

    clock.tick(30)

pygame.quit()


