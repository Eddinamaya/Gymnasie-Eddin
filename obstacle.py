import pygame
import random
import time

# variables for obstacle
x2 = 80
y2 = 80
screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))

#clock = pygame.time.Clock()
#current_time = 0
#print("start")
#button_press_time = 0
#print("button")

class Obstacle():

    def __init__(Kam, x, y):
        kamel = pygame.image.load(r'assets/pixelart_logs_3.png')
        Kam.image = pygame.transform.scale(kamel, (40, 70))
        Kam.rect = Kam.image.get_rect()
        Kam.rect.x = x
        Kam.rect.y = y
        Kam.startt = 5

        # ändring
    def update(Kam):

        # if current_time - button_press_time > 2000:
        # print("now")

        dx = 0
        dy = 6

        Kam.rect.x += dx
        Kam.rect.y += dy

        number = random.randint(0, 1280)

        if Kam.rect.top > 720:
            Kam.rect.top = 0

        if Kam.rect.top == 0:
            Kam.rect.right = number

        screen.blit(Kam.image, Kam.rect)


Obstacle = Obstacle(x2, y2)
