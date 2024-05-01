import pygame
import english_text_pygame as lang
from player_config_additional import *

GREEN = (0, 100, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY  = (50, 50, 50)
RED  = (207, 0, 0)
LIGHT_GREY = (211, 211, 211)
VERMILLION = (173, 75, 64)

END_BACKGROUND = VERMILLION
BACKGROUND_COLOR = GREEN
MARGIN = 10

def clear_to_main_background(screen):
    background_image = pygame.image.load("./img/background_image.jpg")  # Replace with your image path
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    # Resize the image to fit the screen 
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Fill the background with the image
    screen.blit(background_image, (0, 0))

    pygame.display.flip()


def display_final_scores(players, screen):
    font = pygame.font.Font(None, 36)# Use default font
    winners = []
    max_score = 0
    text_y = 50

    # Draw background
    screen.fill(END_BACKGROUND)

    # Render and display final scores
    text_surface = font.render(lang.final_scores, True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 40

    for player in players:
        text_surface = font_footer.render(lang.player_points(player), True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 20

        if player.score > max_score:
            winners = [player]
            max_score = player.score
        elif player.score == max_score:
            winners.append(player)

    text_y += 30
    # Render and display winning information
    text_surface = font.render(lang.winning_score(max_score) , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50
    winning_names = ", ".join(winner.name for winner in winners)
    text_surface = font.render(lang.winning_names(winning_names), True, WHITE)
    screen.blit(text_surface, (50, text_y))

    # Update the display

    pygame.display.flip()


def display_player_hand(hand, CARD_WIDTH, CARD_HEIGHT, screen, name):
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    total_cards = len(hand)

    overlap_gap = CARD_WIDTH + 1
    
    start_x = MARGIN
    start_y = SCREEN_HEIGHT - CARD_HEIGHT - MARGIN  # 10 pixels above the bottom of the screen

    round_title = font_footer.render(lang.player_choose_bid(name), True, WHITE)
    screen.blit(round_title, (start_x, start_y - 24))

    for card in hand:
        card.display_card(screen, start_x, start_y, CARD_WIDTH, CARD_HEIGHT)
        start_x += overlap_gap
    
    pygame.display.flip()

def display_scores_on_main(screen, players):
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    text_x = SCREEN_WIDTH - 200
    text_y = 20
    text_surface = font_footer.render(lang.scores, True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 20

    display_score_values(screen, font_footer, players, text_x, text_y)
    
    pygame.display.flip()

def display_score_values(screen, font_style, players, text_x, text_y):
    for player in players:
        text = f"-> {player.name}: {player.score :.2f} points"
        text_surface = font_style.render(text, True, WHITE)
        screen.blit(text_surface, (text_x, text_y))
        text_y += 20

def print_round_title(screen, round_no, SCREEN_WIDTH):
    round_title = font.render(lang.round_no(round_no) , True, WHITE)
    screen.blit(round_title, (SCREEN_WIDTH / 2 - 30, 20))

def display_bids_and_winners(screen, bids, players, winners, highest_bid, round_no, revealed_diamond_value):
    clear_to_main_background(screen)
    SCREEN_WIDTH = screen.get_width()
    print_round_title(screen, round_no, SCREEN_WIDTH)

    text_x = 50
    text_y = 120

    text_surface = font.render(lang.bids, True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 40

    for player, bid in zip(players, bids):
        text = f"-> {player.name}: {bid}"
        text_surface = font_footer.render(text, True, WHITE)
        screen.blit(text_surface, (text_x, text_y))
        text_y += 20

    # Render and display winning information
    points_given = revealed_diamond_value / len(winners)
        
    text_y += 30    
    
    winning_names = ", ".join(winner.name for winner in winners)

    text_surface = font.render(lang.winning_bid(highest_bid), True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 50

    text_surface = font.render(lang.points_given(points_given, winning_names) , True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 50

    text_surface = font.render(lang.scores , True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 40
    
    display_score_values(screen, font_footer, players, text_x, text_y)

    # Update the display
    pygame.display.flip()