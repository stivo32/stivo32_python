__author__ = 'k_eryomenko'
import pygame



black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)


pygame.init()

size = [255, 255]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

width = 20
height = 20
margin = 5

grid = []

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

grid[1][5] = 1
color = white
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            print("click: ",pos)
            row = y // (margin+height)
            column = x // (margin + width)
            print("row = ", row, " column = ", column)
            grid[row][column] = 1


    screen.fill(black)
    for row in range(10):
        for column in range(10):
            if grid[row][column] == 1:
                color = red
            else:
                color = white
            pygame.draw.rect(screen, color, [margin+column*(width+margin), margin+row*(height+margin), width, height], 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()