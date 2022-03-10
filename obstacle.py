import pygame
import random

# The reset coordinates for the obstacles
x2 = 80
y2 = 80
x3 = 1000
y3 = 60

# The size of the screen
screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))

# The speed variables of the obstacles
dy = 4
dx = 0


class Obstacle():

    def __init__(Kam, x, y):
        log = pygame.image.load(r'assets/pixelart_logs_3.png')
        Kam.image = pygame.transform.scale(log, (40, 70))
        Kam.rect = Kam.image.get_rect()
        Kam.rect.x = x
        Kam.rect.y = y

    def obsticle_speed_reset(Kam):

        global dy
        global dx
        dy = 2
        dx = 0

    def update(Kam):

        global dy
        global dx

        Kam.rect.x += dx
        Kam.rect.y += dy

        number = random.randint(0, 1280)

        if Kam.rect.top > 720:
            Kam.rect.top = 0
            dy += 1

        if Kam.rect.top == 0:
            Kam.rect.right = number

        screen.blit(Kam.image, Kam.rect)


Obstacle = Obstacle(x2, y2)


class Obstacle2():

    def __init__(Ham, x, y):
        log2 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Ham.image = pygame.transform.scale(log2, (40, 70))
        Ham.rect = Ham.image.get_rect()
        Ham.rect.x = x
        Ham.rect.y = y

    def obsticle2_speed_reset(Ham):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Ham):

        global dy
        global dx

        Ham.rect.x += dx
        Ham.rect.y += dy

        number = random.randint(0, 1280)

        if Ham.rect.top > 720:
            Ham.rect.top = 0
            dy += 1

        if Ham.rect.top == 0:
            Ham.rect.right = number

        screen.blit(Ham.image, Ham.rect)


Obstacle2 = Obstacle2(x3, y3)

class Obstacle3():

    def __init__(Dam, x, y):
        log3 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Ham.image = pygame.transform.scale(log3, (40, 70))
        Ham.rect = Ham.image.get_rect()
        Ham.rect.x = x
        Ham.rect.y = y

    def obsticle2_speed_reset(Ham):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Ham):

        global dy
        global dx

        Ham.rect.x += dx
        Ham.rect.y += dy

        number = random.randint(0, 1280)

        if Ham.rect.top > 720:
            Ham.rect.top = 0
            dy += 1

        if Ham.rect.top == 0:
            Ham.rect.right = number

        screen.blit(Ham.image, Ham.rect)


Obstacle2 = Obstacle2(x3, y3)



