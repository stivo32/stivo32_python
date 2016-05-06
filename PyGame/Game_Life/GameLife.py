__author__ = 'k_eryomenko'
import pygame
import random



black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)

def step(grid):
    grid_final = []
    for row in range(len(grid)):
        grid_final.append([])
        for column in range(len(grid[row])):
            grid_final[row].append(0)

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            neighbour = 0
            alive = grid[row][column]
            if (row == 0 and column == 0):
                if (grid[len(grid)-1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[len(grid)-1][column]== 1):
                    neighbour+=1
                if (grid[len(grid)-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[row+1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row+1][column] == 1):
                    neighbour+=1
                if (grid[row+1][column+1]== 1):
                    neighbour+=1

            elif (row == len(grid)-1 and column == 0):
                if (grid[row-1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[1][column] == 1):
                    neighbour+=1
                if (grid[1][column+1]== 1):
                    neighbour+=1

            elif (column == 0):
                if (grid[row-1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[row+1][len(grid[row])-1]== 1):
                    neighbour+=1
                if (grid[row+1][column]== 1):
                    neighbour+=1
                if (grid[row+1][column+1]== 1):
                    neighbour+=1

            elif (row == 0 and column == len(grid[row])-1):
                if (grid[len(grid)-1][column-1] == 1):
                    neighbour+=1
                if (grid[len(grid)-1][column] == 1):
                    neighbour+=1
                if (grid[len(grid)-1][1] == 1):
                    neighbour+=1
                if (grid[row][column-1] == 1):
                    neighbour+=1
                if (grid[row][1] == 1):
                    neighbour+=1
                if (grid[row+1][column-1] == 1):
                    neighbour+=1
                if (grid[row+1][column] == 1):
                    neighbour+=1
                if (grid[row+1][1] == 1):
                    neighbour+=1

            elif (row == 0):
                if (grid[len(grid)-1][column-1]== 1):
                    neighbour+=1
                if (grid[len(grid)-1][column]== 1):
                    neighbour+=1
                if (grid[len(grid)-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][column-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[row+1][column-1]== 1):
                    neighbour+=1
                if (grid[row+1][column]== 1):
                    neighbour+=1
                if (grid[row+1][column+1]== 1):
                    neighbour+=1

            elif (row == len(grid)-1 and column == len(grid[row])-1):
                if (grid[row-1][column-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][1]== 1):
                    neighbour+=1
                if (grid[row][column-1]== 1):
                    neighbour+=1
                if (grid[row][1]== 1):
                    neighbour+=1
                if (grid[1][column-1]== 1):
                    neighbour+=1
                if (grid[1][column]== 1):
                    neighbour+=1
                if (grid[1][1]== 1):
                    neighbour+=1

            elif (column == len(grid[row])-1):
                if (grid[row-1][column-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][1]== 1):
                    neighbour+=1
                if (grid[row][column-1]== 1):
                    neighbour+=1
                if (grid[row][1]== 1):
                    neighbour+=1
                if (grid[row+1][column-1]== 1):
                    neighbour+=1
                if (grid[row+1][column]== 1):
                    neighbour+=1
                if (grid[row+1][1]== 1):
                    neighbour+=1

            elif (row == len(grid)-1):
                if (grid[row-1][column-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][column-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[1][column-1]== 1):
                    neighbour+=1
                if (grid[1][column]== 1):
                    neighbour+=1
                if (grid[1][column+1]== 1):
                    neighbour+=1
            else:
                if (grid[row-1][column-1]== 1):
                    neighbour+=1
                if (grid[row-1][column]== 1):
                    neighbour+=1
                if (grid[row-1][column+1]== 1):
                    neighbour+=1
                if (grid[row][column-1]== 1):
                    neighbour+=1
                if (grid[row][column+1]== 1):
                    neighbour+=1
                if (grid[row+1][column-1]== 1):
                    neighbour+=1
                if (grid[row+1][column]== 1):
                    neighbour+=1
                if (grid[row+1][column+1]== 1):
                    neighbour+=1

            if alive == 1 and neighbour < 2:
                grid_final[row][column] = 0
            elif alive == 1 and neighbour > 3:
                grid_final[row][column] = 0
            elif alive == 1 and neighbour >= 2 and neighbour <= 3:
                grid_final[row][column] = grid[row][column]
            elif alive == 0 and neighbour == 3:
                grid_final[row][column] = 1
            else:
                grid_final[row][column] = 0
    return grid_final



pygame.init()

size = [1000, 1000]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

width = 10
height = 10
margin = 5

grid = []

for row in range(100):
    grid.append([])
    for column in range(100):
        grid[row].append(0)

for row in range(100):
        for column in range(100):
            if random.randint(0,4) == 3:
                grid[row][column] = 1


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
            row = y // (height)
            column = x // (width)
            print("row = ", row, " column = ", column)
            grid[row][column] = 1

    grid = step(grid)

    screen.fill(black)
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                color = blue
            else:
                color = white
            pygame.draw.rect(screen, color, [column*(width), row*(height), width, height], 0)

    pygame.display.flip()

    clock.tick(10)



pygame.quit()