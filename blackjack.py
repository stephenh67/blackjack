import pygame
from pygame.locals import *
import sys
from cards import Hand, Deck
import take_bet as tb
from settings import Settings


pygame.init()


def play():
    """

    :return:
    """
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")

    # create play button rect
    play_button = pygame.image.load('images/play.png')
    play_rect = play_button.get_rect()
    play_rect.topleft = (475, 100)

    # draw screen and add objects
    bj_settings.game_screen.fill(bj_settings.GREEN)
    bj_settings.game_screen.blit(play_button, (475, 50))

    pygame.display.update()

    # get events
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    player = Hand()
                    dealer = Hand()
                    deck = Deck()
                    tb.take_bet(10, player, dealer, deck)


if __name__ == '__main__':
    play()
