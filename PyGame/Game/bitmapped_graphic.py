import pygame

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

click_sound = pygame.mixer.Sound("mouseclick.mp3")
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
#сделать черный цвет прозрачным для данного изображения
player_image.set_colorkey(black)
x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    screen.blit(background_image, [0,0])
    pygame.mouse.set_visible(0)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    screen.blit(player_image, [x, y])


    pygame.display.flip()

    clock.tick(30)

pygame.quit()