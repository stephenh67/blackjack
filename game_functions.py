import pysnooper
import pygame
from settings import Settings
import sys


@pysnooper.snoop()
def add_text(text, font, surface, x, y, text_color):
    """

    :param text:
    :param font:
    :param surface:
    :param x:
    :param y:
    :param text_color:
    :return:
    """
    textobject = font.render(text, 1, text_color)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect)


def game_over():
    """

    :return:
    """
    bj_settings = Settings()
    bj_settings.game_screen = pygame.display.set_mode((bj_settings.screen_width, bj_settings.screen_width))

    pygame.display.set_caption("Blackjack Game Over")
    bj_settings.game_screen.fill(bj_settings.GREEN)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()