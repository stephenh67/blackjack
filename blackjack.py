import pygame
from pygame.locals import *
import sys
import time
from cards import Hand, Deck
import pysnooper
# import game_functions import add_text
import game_functions as gf
from settings import Settings


pygame.init()
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


@pysnooper.snoop()
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
                    take_bet(10, player, dealer, deck)


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
    clock.tick()

    # get events
    while not bets_placed:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
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
        award = play_hand(bet, chips, player, dealer, deck)
        chips += award
        pygame.display.update()
        take_bet(chips, player, dealer, deck)


def play_hand(bet, chips, player, dealer, deck):
    """

    :param bet:
    :param chips:
    :param player:
    :param dealer:
    :param deck:
    :return:
    """
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")
    bj_settings.game_screen.fill(bj_settings.GREEN)

    font = pygame.font.SysFont(None, 50)

    # text setting for chips
    gf.add_text(('Chips: ' + str(chips - bet)), font, bj_settings.game_screen, 100, 30, bj_settings.BLACK)

    # text setting for bet
    gf.add_text(('Bet: ' + str(bet)), font, bj_settings.game_screen, 600, 30, bj_settings.BLACK)

    pcardx, pcardy = (600, 100)
    # Load the card images into the game.
    for card in player.cards:
        pic = pygame.image.load('images/' + str(card) + '.png')
        bj_settings.game_screen.blit(pic, (pcardx, pcardy))
        pcardx += 75

    gf.add_text('(H) to hit (S) to stand', font, bj_settings.game_screen, 600, 540, bj_settings.BLACK)

    dcardx, dcardy = (100, 100)
    dcard1 = pygame.image.load('images/' + str(dealer.cards[0]) + '.png')
    dcard2 = pygame.image.load('images/' + str(dealer.cards[1]) + '.png')
    dcard_back = pygame.image.load('images/back.png')

    # draw dealer cards
    bj_settings.game_screen.blit(dcard1, (dcardx, dcardy))
    bj_settings.game_screen.blit(dcard_back, (dcardx + 75, dcardy))

    pygame.display.update()

    clock.tick()

    blackjack = False
    double_prize = False
    dealer_bust = False
    player_bust = False

    # for testing blackjack

    # check if player has blackjack
    if player.value == 21:
        # blackjack text
        gf.add_text('Blackjack!!! You WIN!!', font, bj_settings.game_screen, 600, 460, bj_settings.BLACK)
        gf.add_text('Press space to continue', font, bj_settings.game_screen, 600, 500, bj_settings.BLACK)
        pygame.display.update()
        blackjack = True
        double_prize = True

    # dealer has natual 21 and player doesnt
    if dealer.value == 21 and player.value != 21:
        gf.add_text('Dealer just got Blackjack. You lose.', font, bj_settings.game_screen, 100, 460, bj_settings.BLACK)
        gf.add_text('Press space to continue', font, bj_settings.game_screen, 100, 500, bj_settings.BLACK)
        bj_settings.game_screen.blit(dcard2, (dcardx + 75, dcardy))
        pygame.display.update()
        blackjack = True

    stand = False
    hand_done = False
    player_wins = False
    dealer_wins = False
    push = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Game logic to allow to allow button presses on keyboard.
            if event.type == KEYDOWN:
                if event.key == K_SPACE and double_prize is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet * 2
                if (event.key == K_SPACE and dealer.value == 21 or event.key == K_SPACE
                        and player.value > 21 or event.key == K_SPACE and dealer_wins is True):
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return -bet
                if event.key == K_SPACE and dealer.value > 21 or event.key == K_SPACE and player_wins is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet
                if event.key == K_SPACE and push is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return 0
                if event.key == K_h and player.value < 22 and player.value != 21 and stand is False:
                    player.add_card(deck.deal())
                    bj_settings.game_screen.blit(pygame.image.load('images/' + str(player.cards[-1]) + '.png'),
                                                 (pcardx, pcardy))
                    pcardx += 75
                    pygame.display.update()

                    if player.value > 21:
                        gf.add_text('OVER 21! You lose.', font, bj_settings.game_screen, 600, 460, bj_settings.BLACK)
                        gf.add_text('Press space to continue', font, bj_settings.game_screen, 600, 500, bj_settings.BLACK)
                        pygame.display.update()
                        player_bust = True
                if event.key == K_s and player.value < 22 and blackjack is False and stand is False:
                    dcardx += 75
                    bj_settings.game_screen.blit(pygame.image.load('images/' + str(dealer.cards[1]) + '.png'),
                                                 (dcardx, dcardy))
                    pygame.display.update()
                    stand = True

                    # Win conditions
                    while dealer.value < 17 and stand is True and hand_done is False:
                        gf.add_text('Dealer is drawing . . .', font, bj_settings.game_screen, 100, 420, bj_settings.BLACK)
                        time.sleep(1)
                        dcardx += 75
                        dealer.add_card(deck.deal())
                        bj_settings.game_screen.blit(pygame.image.load('images/' + str(dealer.cards[-1]) + '.png'), (
                            dcardx, dcardy))
                        pygame.display.update()

                        if dealer.value > 21:
                            gf.add_text('DEALER BUST! YOU WIN!', font, bj_settings.game_screen, 100, 460,
                                        bj_settings.BLACK)
                            gf.add_text('Press space to continue', font, bj_settings.game_screen, 100, 500,
                                        bj_settings.BLACK)
                            pygame.display.update()
                            dealer_bust = True
                    if dealer.value >= 17:
                        pygame.display.update()
                        hand_done = True
                    if dealer_bust is False and stand is True and player_bust is False \
                            and blackjack is False and hand_done is True:
                        if dealer.value <= 21 and player.value <= 21:
                            if player.value > dealer.value:
                                gf.add_text('YOU WIN!', font, bj_settings.game_screen, 600, 460, bj_settings.BLACK)
                                gf.add_text('Press space to continue', font, bj_settings.game_screen, 600, 500,
                                            bj_settings.BLACK)
                                pygame.display.update()
                                player_wins = True
                            if player.value < dealer.value:
                                gf.add_text('Dealer wins.', font, bj_settings.game_screen, 100, 460, bj_settings.BLACK)
                                gf.add_text('Press space to continue', font, bj_settings.game_screen, 100, 500,
                                            bj_settings.BLACK)
                                pygame.display.update()
                                dealer_wins = True
                            if player.value == dealer.value:
                                gf.add_text('Tie!', font, bj_settings.game_screen, 600, 460, bj_settings.BLACK)
                                gf.add_text('Press space to continue', font, bj_settings.game_screen, 600, 500,
                                            bj_settings.BLACK)
                                pygame.display.update()
                                push = True

if __name__ == '__main__':
    play()
