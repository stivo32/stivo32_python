__author__ = 'k_eryomenko'
import pygame

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)
yellow =( 255, 255,   0)

pi = 3.141592653

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)

    pygame.draw.rect(screen, blue, [0, 0, 700, 500], 0) #draw a rectangle
    pygame.draw.rect(screen, green, [0, 350, 700, 150], 0) #draw a rectangle
    pygame.draw.rect(screen, white, [200, 150, 300, 200], 0) #draw a rectangle
    pygame.draw.rect(screen, black, [320, 270, 60, 80], 0) #draw a rectangle
    for i in range(2):
        pygame.draw.rect(screen, black, [240+i*190, 190, 30, 30], 0)
    pygame.draw.polygon(screen, red, [[180, 150], [520, 150], [350, 30]], 0)
    pygame.draw.ellipse(screen, yellow, [30,30,60,60], 0) #draw ellipse
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

__author__ = 'k_eryomenko'
