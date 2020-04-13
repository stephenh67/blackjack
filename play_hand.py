from settings import Settings
import pygame
import sys
import game_functions as gf
import time


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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Game logic to allow to allow button presses on keyboard.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and double_prize is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet * 2
                if (event.key == pygame.K_SPACE and dealer.value == 21 or event.key == pygame.K_SPACE
                        and player.value > 21 or event.key == pygame.K_SPACE and dealer_wins is True):
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return -bet
                if event.key == pygame.K_SPACE and dealer.value > 21 or event.key == pygame.K_SPACE and player_wins \
                        is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return bet
                if event.key == pygame.K_SPACE and push is True:
                    del player.cards[:]
                    del dealer.cards[:]
                    player.value = 0
                    dealer.value = 0
                    return 0
                if event.key == pygame.K_h and player.value < 22 and player.value != 21 and stand is False:
                    player.add_card(deck.deal())
                    bj_settings.game_screen.blit(pygame.image.load('images/' + str(player.cards[-1]) + '.png'),
                                                 (pcardx, pcardy))
                    pcardx += 75
                    pygame.display.update()

                    if player.value > 21:
                        gf.add_text('OVER 21! You lose.', font, bj_settings.game_screen, 600, 460, bj_settings.BLACK)
                        gf.add_text('Press space to continue', font, bj_settings.game_screen, 600, 500,
                                    bj_settings.BLACK)
                        pygame.display.update()
                        player_bust = True
                if event.key == pygame.K_s and player.value < 22 and blackjack is False and stand is False:
                    dcardx += 75
                    bj_settings.game_screen.blit(pygame.image.load('images/' + str(dealer.cards[1]) + '.png'),
                                                 (dcardx, dcardy))
                    pygame.display.update()
                    stand = True

                    # Win conditions
                    while dealer.value < 17 and stand is True and hand_done is False:
                        gf.add_text('Dealer is drawing . . .', font, bj_settings.game_screen, 100, 420,
                                    bj_settings.BLACK)
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
