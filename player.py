import pygame
import random

# variables for player
x1 = 500
y1 = 500

# screen size
screen_height = 720
screen_width = 900
screen = pygame.display.set_mode((screen_width, screen_height))

class Player():
    def __init__(self, x, y):
        boat = pygame.image.load(r'assets/Pixelart_boat_3.png')
        self.image = pygame.transform.scale(boat, (40, 100))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x
        self.rect.y = y

    def reset_boat_position(self):
        self.rect.x = 500
        self.rect.y = 500

    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            dy -= 7
        if key[pygame.K_DOWN]:
            dy += 7
        if key[pygame.K_LEFT]:
            dx -= 7
        if key[pygame.K_RIGHT]:
            dx += 7

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        screen.blit(self.image, self.rect)

Player = Player(x1, y1)
