from settings import Settings
import play_hand as ph
import pygame
import sys
from cards import Deck
import game_functions as gf


def take_bet(chips, player, dealer, deck):
    """

    :param chips:
    :param player:
    :param dealer:
    :param deck:
    :return:
    """
    bj_settings = Settings()

    if chips < 5:
        gf.game_over()
    bets_placed = False

    pygame.display.set_caption("Blackjack Place your Bet")
    bj_settings.game_screen.fill(bj_settings.GREEN)

    # text setting
    font_obj = pygame.font.Font('freesansbold.ttf', 40)
    text_surface_obj = font_obj.render("Place your bet", True, bj_settings.BLACK, bj_settings.GREEN)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (int(bj_settings.screen_width * .5), int(bj_settings.screen_height * .050))

    # text setting
    font_obj1 = pygame.font.Font('freesansbold.ttf', 32)
    text_surface_obj1 = font_obj1.render("CHIPS " + str(chips), True, bj_settings.BLACK, bj_settings.GREEN)
    text_rect_obj1 = text_surface_obj1.get_rect()
    text_rect_obj1.center = (int(bj_settings.screen_width * .5), int(bj_settings.screen_height * .150))

    # draw text to screen
    bj_settings.game_screen.blit(text_surface_obj, text_rect_obj)
    bj_settings.game_screen.blit(text_surface_obj1, text_rect_obj1)

    # bet 5 button
    bet_5_pos = (100, 300)
    bet_5 = pygame.image.load('images/5.png')
    bet_5_rect = bet_5.get_rect()
    bet_5_rect.topleft = bet_5_pos

    # bet 10 button
    bet_10_pos = (300, 150)
    bet_10 = pygame.image.load('images/10.png')
    bet_10_rect = bet_10.get_rect()
    bet_10_rect.topleft = bet_10_pos

    # bet 25 button
    bet_25_pos = (500, 300)
    bet_25 = pygame.image.load('images/25.png')
    bet_25_rect = bet_25.get_rect()
    bet_25_rect.topleft = bet_25_pos

    # bet 50 button
    bet_50_pos = (700, 150)
    bet_50 = pygame.image.load('images/50.png')
    bet_50_rect = bet_50.get_rect()
    bet_50_rect.topleft = bet_50_pos

    # bet 100 button
    bet_100_pos = (900, 300)
    bet_100 = pygame.image.load('images/100.png')
    bet_100_rect = bet_100.get_rect()
    bet_100_rect.topleft = bet_100_pos

    # draw chip buttons on screen
    bj_settings.game_screen.blit(bet_5, bet_5_rect)
    bj_settings.game_screen.blit(bet_10, bet_10_rect)
    bj_settings.game_screen.blit(bet_25, bet_25_rect)
    bj_settings.game_screen.blit(bet_50, bet_50_rect)
    bj_settings.game_screen.blit(bet_100, bet_100_rect)

    pygame.display.update()

    # get events
    while not bets_placed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bet_5_rect.collidepoint(event.pos):
                    if chips >= 5:
                        bet = 5
                        bets_placed = True
                if bet_10_rect.collidepoint(event.pos):
                    if chips >= 10:
                        bet = 10
                        bets_placed = True
                if bet_25_rect.collidepoint(event.pos):
                    if chips >= 25:
                        bet = 25
                        bets_placed = True
                if bet_50_rect.collidepoint(event.pos):
                    if chips >= 50:
                        bet = 50
                        bets_placed = True
                if bet_100_rect.collidepoint(event.pos):
                    if chips >= 100:
                        bet = 100
                        bets_placed = True

    while bets_placed is True:
        deck = Deck()
        deck.shuffle()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        award = ph.play_hand(bet, chips, player, dealer, deck)
        chips += award
        pygame.display.update()
        take_bet(chips, player, dealer, deck)
