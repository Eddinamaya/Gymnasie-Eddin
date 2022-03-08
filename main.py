import pygame, sys
from button import Button
from obstacle import *
from player import *
import time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("moto sport")

menubackground = pygame.image.load("assets/mainmenubackground.png")
playbackground = pygame.image.load("assets/playbackground.png")

# frames per second for play
clock = pygame.time.Clock()
fps = 60


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        SCREEN.blit(playbackground, (0, 0))
        clock.tick(fps)

        Obstacle.update()
        Player.update()

        pygame.display.update()
        collide = pygame.Rect.colliderect(Player.rect, Obstacle.rect)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        if collide:
            Obstacle.rect.bottom = Player.rect.top
            Player.back()
            Obstacle.back_obsticle()
            restart_menu()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
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

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
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
        SCREEN.blit(menubackground, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

       #MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        RESTART_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 180),
                             text_input="RESTART", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        MAIN_MENU = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 340),
                             text_input="MAIN MENU", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 500),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        #SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [RESTART_BUTTON, QUIT_BUTTON, MAIN_MENU]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MAIN_MENU.checkForInput(MENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()


main_menu()