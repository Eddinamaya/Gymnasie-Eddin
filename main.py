import pygame, sys
import pygame.image

import obstacle
from button import Button
from obstacle import *
from player import *
import time

pygame.init()

# Screensize
SCREEN = pygame.display.set_mode((900, 720))
pygame.display.set_caption("moto sport")

# Screen-images
menubackground = pygame.image.load("assets/mainmenubackground.png")
playbackground = pygame.image.load("assets/Finalbackground.png")
playbackground = pygame.transform.scale(playbackground, (900, 720))
restartmenu = pygame.image.load("assets/Gameover.jpg")
restartmenu = pygame.transform.scale(restartmenu, (400, 300))

# Frames per second for play
clock = pygame.time.Clock()
fps = 60

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        SCREEN.blit(playbackground, (0, 0))
        clock.tick(fps)

        Obstacle.score_display()
        Obstacle.update()
        Obstacle2.update()
        Obstacle3.update()
        Obstacle4.update()
        Obstacle5.update()
        Obstacle6.update()
        Obstacle7.update()
        Obstacle8.update()
        Obstacle9.update()
        Player.update()

        pygame.display.update()
        collide = pygame.Rect.colliderect(Player.rect, Obstacle.rect)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Check for collision in x direction
        if Obstacle.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle.obsticle_speed_reset()
            restart_menu()

        # Check for collision in y direction
        if Obstacle.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle.obsticle_speed_reset()
            restart_menu()

        if Obstacle2.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle2.obsticle2_speed_reset()
            restart_menu()

        if Obstacle2.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle2.obsticle2_speed_reset()
            restart_menu()

        if Obstacle3.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle3.obsticle3_speed_reset()
            restart_menu()

        if Obstacle3.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle3.obsticle3_speed_reset()
            restart_menu()

        if Obstacle4.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle4.obsticle4_speed_reset()
            restart_menu()

        if Obstacle4.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle4.obsticle4_speed_reset()
            restart_menu()

        if Obstacle5.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle5.obsticle5_speed_reset()
            restart_menu()

        if Obstacle5.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle5.obsticle5_speed_reset()
            restart_menu()

        if Obstacle6.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle6.obsticle6_speed_reset()
            restart_menu()

        if Obstacle6.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle6.obsticle6_speed_reset()
            restart_menu()

        if Obstacle7.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle7.obsticle7_speed_reset()
            restart_menu()

        if Obstacle7.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle7.obsticle7_speed_reset()
            restart_menu()

        if Obstacle8.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle8.obsticle8_speed_reset()
            restart_menu()

        if Obstacle8.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle8.obsticle8_speed_reset()
            restart_menu()

        if Obstacle9.rect.colliderect(Player.rect.x + dx, Player.rect.y, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle9.obsticle9_speed_reset()
            restart_menu()

        if Obstacle9.rect.colliderect(Player.rect.x, Player.rect.y + dy, Player.width, Player.height):
            Player.reset_boat_position()
            Obstacle.reset_Obstacle_position()
            Obstacle2.reset_Obstacle2_position()
            Obstacle3.reset_Obstacle3_position()
            Obstacle4.reset_Obstacle4_position()
            Obstacle5.reset_Obstacle5_position()
            Obstacle6.reset_Obstacle6_position()
            Obstacle7.reset_Obstacle7_position()
            Obstacle8.reset_Obstacle8_position()
            Obstacle9.reset_Obstacle9_position()
            Obstacle9.obsticle9_speed_reset()
            restart_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

#<<<<<<< HEAD
        OPTIONS_TEXT = get_font(60).render("How To Play", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(460, 100))
#=======
        OPTIONS_TEXT = get_font(60).render("How To Play", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 100))
#>>>>>>> fc7305deafe0ec168b1a2dbda220c447da65c405
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #Bild på pilarna här

        OPTIONS_BACK = Button(image=None, pos=(460, 600),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(menubackground, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(450, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(450, 400),
                                text_input="How to Play", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(450, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def restart_menu():
    while True:
        screen.fill((0, 0, 0))
        SCREEN.blit(restartmenu, (250, 50))
        Obstacle.score_display(SCORE_TEXT)
        SCORE_RECT = SCORE_TEXT.get_rect(center=(400, 40))
        screen.blit(SCORE_TEXT, SCORE_RECT)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        RESTART_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(450, 450),
                             text_input="RESTART", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        MAIN_MENU = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(450, 600),
                             text_input="MAIN MENU", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        #QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(450, 100),
                            # text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


        for button in [RESTART_BUTTON, MAIN_MENU]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Obstacle.reset_score()
                    play()
                #if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #pygame.quit()
                   # sys.exit()
                if MAIN_MENU.checkForInput(MENU_MOUSE_POS):
                    Obstacle.reset_score()
                    main_menu()


        pygame.display.update()


main_menu()