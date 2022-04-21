import pygame
import random

# The reset coordinates for the obstacles
# 1
x2 = 100
y2 = -50
# 2
x3 = 200
y3 = -100
# 3
x4 = 300
y4 = -150
# 4
x5 = 400
y5 = -200
# 5
x6 = 500
y6 = -400
# 6
x7 = 600
y7 = -250
# 7
x8 = 700
y8 = 0
# 8
x9 = 800
y9 = -300
# 9
x10 = 850
y10 = 0

# The size of the screen
screen_height = 720
screen_width = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# The speed variables of the obstacles
dy = 2
dx = 0

score = 0

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)



def score_displaymenu():
    global score

    SCORE_TEXT = get_font(45).render("SCORE:" + str(score), True, "White")
    SCORE_RECT = SCORE_TEXT.get_rect(center=(450, 350))
    screen.blit(SCORE_TEXT, SCORE_RECT)



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

    def reset_Obstacle_position(Kam):
        Kam.rect.x = 100
        Kam.rect.y = -50

    def reset_score(Kam):
        global score
        score = 0

    def update(Kam):

        global dy
        global dx
        global score

        Kam.rect.x += dx
        Kam.rect.y += dy

        number = random.randint(20, 900)

        if Kam.rect.top > 720:
            Kam.rect.top = 0
            dy += 0.05
            score = score + 1
            print(score)

        if Kam.rect.top == 0:
            Kam.rect.right = number

        screen.blit(Kam.image, Kam.rect)

    def score_display(Kam):

        SCORE_TEXT = get_font(20).render("SCORE:" + str(score), True, "White")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(100, 40))
        screen.blit(SCORE_TEXT, SCORE_RECT)



Obstacle = Obstacle(x2, y2)


class Obstacle2():

    def __init__(Ham, x, y):
        log2 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Ham.image = pygame.transform.scale(log2, (40, 70))
        Ham.rect = Ham.image.get_rect()
        Ham.rect.x = x
        Ham.rect.y = y

    def reset_Obstacle2_position(Ham):
        Ham.rect.x = 200
        Ham.rect.y = -100

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

        number = random.randint(20, 900)

        if Ham.rect.top > 720:
            Ham.rect.top = 0
            dy += 0.05

        if Ham.rect.top == 0:
            Ham.rect.right = number

        screen.blit(Ham.image, Ham.rect)


Obstacle2 = Obstacle2(x3, y3)


class Obstacle3():

    def __init__(Dam, x, y):
        log3 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam.image = pygame.transform.scale(log3, (40, 70))
        Dam.rect = Dam.image.get_rect()
        Dam.rect.x = x
        Dam.rect.y = y

    def reset_Obstacle3_position(Dam):
        Dam.rect.x = 300
        Dam.rect.y = -150

    def obsticle3_speed_reset(Dam):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam):

        global dy
        global dx

        Dam.rect.x += dx
        Dam.rect.y += dy

        number = random.randint(20, 900)

        if Dam.rect.top > 720:
            Dam.rect.top = 0
            dy += 0.05

        if Dam.rect.top == 0:
            Dam.rect.right = number

        screen.blit(Dam.image, Dam.rect)


Obstacle3 = Obstacle3(x4, y4)


class Obstacle4():

    def __init__(Dam1, x, y):
        log4 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam1.image = pygame.transform.scale(log4, (40, 70))
        Dam1.rect = Dam1.image.get_rect()
        Dam1.rect.x = x
        Dam1.rect.y = y

    def reset_Obstacle4_position(Dam1):
        Dam1.rect.x = 400
        Dam1.rect.y = -200

    def obsticle4_speed_reset(Dam1):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam1):

        global dy
        global dx

        Dam1.rect.x += dx
        Dam1.rect.y += dy

        number = random.randint(20, 900)

        if Dam1.rect.top > 720:
            Dam1.rect.top = 0
            dy += 0.05

        if Dam1.rect.top == 0:
            Dam1.rect.right = number

        screen.blit(Dam1.image, Dam1.rect)


Obstacle4 = Obstacle4(x5, y5)


class Obstacle5():

    def __init__(Dam2, x, y):
        log5 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam2.image = pygame.transform.scale(log5, (40, 70))
        Dam2.rect = Dam2.image.get_rect()
        Dam2.rect.x = x
        Dam2.rect.y = y

    def reset_Obstacle5_position(Dam2):
        Dam2.rect.x = 500
        Dam2.rect.y = 0

    def obsticle5_speed_reset(Dam2):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam2):

        global dy
        global dx

        Dam2.rect.x += dx
        Dam2.rect.y += dy

        number = random.randint(20, 900)

        if Dam2.rect.top > 720:
            Dam2.rect.top = 0
            dy += 0.05

        if Dam2.rect.top == 0:
            Dam2.rect.right = number

        screen.blit(Dam2.image, Dam2.rect)


Obstacle5 = Obstacle5(x6, y6)


class Obstacle6():

    def __init__(Dam3, x, y):
        log6 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam3.image = pygame.transform.scale(log6, (40, 70))
        Dam3.rect = Dam3.image.get_rect()
        Dam3.rect.x = x
        Dam3.rect.y = y

    def reset_Obstacle6_position(Dam3):
        Dam3.rect.x = 600
        Dam3.rect.y = 0

    def obsticle6_speed_reset(Dam3):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam3):

        global dy
        global dx

        Dam3.rect.x += dx
        Dam3.rect.y += dy

        number = random.randint(20, 900)

        if Dam3.rect.top > 720:
            Dam3.rect.top = 0
            dy += 0.05

        if Dam3.rect.top == 0:
            Dam3.rect.right = number

        screen.blit(Dam3.image, Dam3.rect)


Obstacle6 = Obstacle6(x7, y7)


class Obstacle7():

    def __init__(Dam4, x, y):
        log7 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam4.image = pygame.transform.scale(log7, (40, 70))
        Dam4.rect = Dam4.image.get_rect()
        Dam4.rect.x = x
        Dam4.rect.y = y

    def reset_Obstacle7_position(Dam4):
        Dam4.rect.x = 700
        Dam4.rect.y = -250

    def obsticle7_speed_reset(Dam4):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam4):

        global dy
        global dx

        Dam4.rect.x += dx
        Dam4.rect.y += dy

        number = random.randint(20, 900)

        if Dam4.rect.top > 720:
            Dam4.rect.top = 0
            dy += 0.05

        if Dam4.rect.top == 0:
            Dam4.rect.right = number

        screen.blit(Dam4.image, Dam4.rect)


Obstacle7 = Obstacle7(x8, y8)


class Obstacle8():

    def __init__(Dam5, x, y):
        log8 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam5.image = pygame.transform.scale(log8, (40, 70))
        Dam5.rect = Dam5.image.get_rect()
        Dam5.rect.x = x
        Dam5.rect.y = y

    def reset_Obstacle8_position(Dam5):
        Dam5.rect.x = 800
        Dam5.rect.y = 0

    def obsticle8_speed_reset(Dam5):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam5):

        global dy
        global dx

        Dam5.rect.x += dx
        Dam5.rect.y += dy

        number = random.randint(20, 900)

        if Dam5.rect.top > 720:
            Dam5.rect.top = 0
            dy += 0.05

        if Dam5.rect.top == 0:
            Dam5.rect.right = number

        screen.blit(Dam5.image, Dam5.rect)


Obstacle8 = Obstacle8(x9, y9)


class Obstacle9():

    def __init__(Dam6, x, y):
        log9 = pygame.image.load(r'assets/pixelart_logs_3.png')
        Dam6.image = pygame.transform.scale(log9, (40, 70))
        Dam6.rect = Dam6.image.get_rect()
        Dam6.rect.x = x
        Dam6.rect.y = y

    def reset_Obstacle9_position(Dam6):
        Dam6.rect.x = 850
        Dam6.rect.y = -300

    def obsticle9_speed_reset(Dam6):

        global dy
        global dx
        dy = 2
        dx = 0

        # ändring
    def update(Dam6):

        global dy
        global dx

        Dam6.rect.x += dx
        Dam6.rect.y += dy

        number = random.randint(20, 900)

        if Dam6.rect.top > 720:
            Dam6.rect.top = 0
            dy += 0.05

        if Dam6.rect.top == 0:
            Dam6.rect.right = number

        screen.blit(Dam6.image, Dam6.rect)


Obstacle9 = Obstacle9(x10, y10)

