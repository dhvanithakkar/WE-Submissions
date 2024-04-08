import pygame
from player_config_additional import *

GREEN = (0, 100, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY  = (50, 50, 50)
RED  = (207, 0, 0)
LIGHT_GREY = (211, 211, 211)
VERMILLION = (173, 75, 64)

BACKGROUND_COLOR = GREEN

def display_final_scores(players, screen):
    font = pygame.font.Font(None, 36)# Use default font
    winners = []
    max_score = 0
    text_y = 50

    # Draw background
    screen.fill(WHITE)

    # Render and display final scores
    text_surface = font.render("Final Scores:", True, BLACK)
    screen.blit(text_surface, (50, text_y))
    text_y += 50

    for player in players:
        text = f"{player.name}: {player.score} points"
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (50, text_y))
        text_y += 50

        if player.score > max_score:
            winners = [player]
            max_score = player.score
        elif player.score == max_score:
            winners.append(player)

    # Render and display winning information
    text_surface = font.render("The winning score is:" , True, BLACK)
    screen.blit(text_surface, (50, text_y))
    text_y += 50
    win_score = font.render(str(max_score), True, BLACK)
    screen.blit(win_score, (50, text_y))
    text_y += 50
    winning_names = ", ".join(winner.name for winner in winners)
    text_surface = font.render(winning_names + " won the game!!", True, BLACK)
    screen.blit(text_surface, (50, text_y))

    # Update the display
    pygame.display.flip()


def display_player_hand(hand, CARD_WIDTH, CARD_HEIGHT, screen, start_y, name):
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    total_cards = len(hand)

    overlap_gap = CARD_WIDTH + 1
    MARGIN = 10
    
    start_x = MARGIN
    # start_y = SCREEN_HEIGHT - CARD_HEIGHT - MARGIN  # 10 pixels above the bottom of the screen

    round_title = font_footer.render(f"{name}, pick your bid:" , True, WHITE)
    screen.blit(round_title, (start_x, start_y - 24))



    for card in hand:
        card.display_card(screen, start_x, start_y, CARD_WIDTH, CARD_HEIGHT)
        start_x += overlap_gap

def human_bid_gui(player, screen ):
    """Allows the player to choose a card for bidding using a graphical interface"""
    
    running = True
    chosen_card = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    for card in player.hand:
                        if card.is_clicked(mouse_pos):
                            chosen_card = card
                            running = False  # Exit loop once card is chosen
                            break

        screen.fill((255, 255, 255))  # Fill the screen with white
        pygame.display.flip()
    
    return chosen_card

def print_round_title(screen, round_no, SCREEN_WIDTH):
    round_title = font.render(f"Round Number: {round_no}" , True, WHITE)
    screen.blit(round_title, (SCREEN_WIDTH/2 - 30, 20))

def display_bids_and_winners(screen, bids, players, winners, highest_bid, round_no, revealed_diamond_value):
    screen.fill(BACKGROUND_COLOR)
    SCREEN_WIDTH = screen.get_width()
    print_round_title(screen, round_no, SCREEN_WIDTH)

    text_y = 50

    for player, bid in zip(players, bids):
        text = f"{player.name}: {bid}"
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 50

    # Render and display winning information
    points_given = revealed_diamond_value / len(winners)
    for winner in winners:
        winner.score += points_given
    
    winning_names = ", ".join(winner.name for winner in winners)

    text_surface = font.render(f"The winning score is: {highest_bid}. \n{points_given} points to {winning_names}" , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50

    text_surface = font.render(f"Scores: " , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50

    for player in players:
        text = f"{player.name}: {player.score}"
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 50


    # Update the display
    pygame.display.flip()
