
import pygame
import random


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

    def reset(self):
        block.rect.y = 0

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)
braun = ( 148, 100,  83)
yellow =( 255, 255,   0)

pygame.init()

screen_width = 700
screen_height = 400
size = [700, 400]
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(black, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)

player = Block(red, 20, 15)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    for block in blocks_hit_list:
        block.reset()
        score += 1
        print(score)

    all_sprites_list.draw(screen)
    for block in block_list:
        block.rect.y+=1
        if (block.rect.y+15)>= screen_height:
            block.rect.y = 0
    pygame.display.flip()

    clock.tick(60)

pygame.quit()