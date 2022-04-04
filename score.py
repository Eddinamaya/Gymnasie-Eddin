import pygame
import time

screen_height = 720
screen_width = 900
screen = pygame.display.set_mode((screen_width, screen_height))

score_value = 0
font_type = pygame.font.match_font("font.ttf")

textX = 10
textY = 10

def shoescore(x, y):

    score_text = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))




            #font = pygame.font.Font(font_type, size)
            #text_surface = font.render(text, True, (0, 0, 0))
            #text_rect = text_surface.get_rect()
            #text.rect.midtop = (x, y)
            #surf.blit(text_surface, text_rect)

