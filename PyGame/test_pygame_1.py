__author__ = 'k_eryomenko'
import pygame



black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)
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

    pygame.draw.line(screen, green, [0,0], [100,100], 5)
    #lines with offset
    for y_offset in range(0,100,10):
        pygame.draw.line(screen, red, [0, 10+y_offset], [100, 110+y_offset], 5)
    #draw a rectangle
    pygame.draw.rect(screen, black, [20, 20, 250, 100], 2) #draw a rectangle
    #draw ellipse
    pygame.draw.ellipse(screen, black, [300,300,250,100], 2) #draw ellipse
    #draw ellipse with arcs
    pygame.draw.arc(screen, green, [100, 100, 350, 200], pi/2, pi, 2)
    pygame.draw.arc(screen, red, [100, 100, 350, 200], 0, pi/2, 2)
    pygame.draw.arc(screen, black, [100, 100, 350, 200], 3*pi/2, 2*pi, 2)
    pygame.draw.arc(screen, green, [100, 100, 350, 200], pi, 3*pi/2, 2)
    #draw poligon
    pygame.draw.polygon(screen, black, [[100, 100], [0, 200], [200, 200]], 5)
    #draw text
    #choose font
    font = pygame.font.Font(None, 25)
    text = font.render("My text", True, black)
    screen.blit(text, [300, 300])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

