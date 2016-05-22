# -*- coding: utf-8 -*-
import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
SOME = (230, 230, 230)

class Player_1(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, image, pos):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.change_x = 0
        self.change_y = 0

        self.image = pygame.image.load(image)
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def changespeed(self, x, y):
        self.change_x = x
        self.change_y = y

    def move(self):
        self.gravity()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def jump(self):
        self.change_y-=10

    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y+=.35
        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height





# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Create a RED player block
player_1 = Player_1("dragon.png", [100, 500])
player_2 = Player_1("princess.png", [400, 500])
all_sprites_list.add(player_1)
all_sprites_list.add(player_2)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                player_2.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player_2.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player_2.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player_2.changespeed(0, 5)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_2.changespeed(0, 0)
            if event.key == pygame.K_RIGHT:
                player_2.changespeed(0, 0)
            if event.key == pygame.K_UP:
                player_2.changespeed(0, 0)
            if event.key == pygame.K_DOWN:
                player_2.changespeed(0, 0)
            if event.key == pygame.K_SPACE:
                player_2.jump()

    # Clear the screen
    screen.fill(SOME)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
    player_1.setPosition(pos[0], pos[1])
    player_2.move()
    print(player_2.rect.bottom)
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location



    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()