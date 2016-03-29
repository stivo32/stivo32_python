import pygame

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)


def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, white, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, white, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, white, [0+x, 65+y, 100, 100])


pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
done = True
clock = pygame.time.Clock()


x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    x_coord = x_coord+x_speed
    y_coord = y_coord+y_speed

    screen.fill(black)

    # mouse coord

    # pygame.mouse.set_visible(0)
    # pos = pygame.mouse.get_pos()
    # x = pos[0]
    # y = pos[1]

    #keyboard coord
    draw_snowman(screen, x_coord, y_coord)


    pygame.display.flip()

    clock.tick(30)

pygame.quit()
