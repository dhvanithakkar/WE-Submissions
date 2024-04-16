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

def clear_to_main_background(screen):
    background_image = pygame.image.load("./img/background_image.jpg")  # Replace with your image path
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    # Resize the image to fit the screen (optional)
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
    screen.fill(VERMILLION)

    # Render and display final scores
    text_surface = font.render("Final Scores:", True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 40

    for player in players:
        text = f"-> {player.name}: {player.score :.2f} points"
        text_surface = font_footer.render(text, True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 20

        if player.score > max_score:
            winners = [player]
            max_score = player.score
        elif player.score == max_score:
            winners.append(player)

    text_y += 30
    # Render and display winning information
    text_surface = font.render(f"The winning score is: {player.score :.2f}" , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50
    winning_names = ", ".join(winner.name for winner in winners)
    text_surface = font.render(winning_names + " won the game!!", True, WHITE)
    screen.blit(text_surface, (50, text_y))

    # Update the display

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
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

# def human_bid_gui(player, screen ):
    # """Allows the player to choose a card for bidding using a graphical interface"""
    
    # running = True
    # chosen_card = None

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             if event.button == 1:  # Left mouse button
    #                 mouse_pos = pygame.mouse.get_pos()
    #                 for card in player.hand:
    #                     if card.is_clicked(mouse_pos):
    #                         chosen_card = card
    #                         running = False  # Exit loop once card is chosen
    #                         break

    #     screen.fill(WHITE)  # Fill the screen with white
    #     pygame.display.flip()
    
    # return chosen_card

def display_scores_on_main(screen, players):
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    text_x = SCREEN_WIDTH - 150
    text_y = 20
    text_surface = font_footer.render(f"Scores: " , True, WHITE)
    screen.blit(text_surface, (text_x, text_y))
    text_y += 20

    for player in players:
        text = f"-> {player.name}: {player.score}"
        text_surface = font_footer.render(text, True, WHITE)
        screen.blit(text_surface, (text_x, text_y))
        text_y += 20
    pygame.display.flip()

def print_round_title(screen, round_no, SCREEN_WIDTH):
    round_title = font.render(f"Round Number: {round_no}" , True, WHITE)
    screen.blit(round_title, (SCREEN_WIDTH/2 - 30, 20))

def display_bids_and_winners(screen, bids, players, winners, highest_bid, round_no, revealed_diamond_value):
    clear_to_main_background(screen)
    SCREEN_WIDTH = screen.get_width()
    print_round_title(screen, round_no, SCREEN_WIDTH)

    text_y = 120

    text_surface = font.render(f"Bids: " , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 40

    for player, bid in zip(players, bids):
        text = f"-> {player.name}: {bid}"
        text_surface = font_footer.render(text, True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 20

    # Render and display winning information
    points_given = revealed_diamond_value / len(winners)
    for winner in winners:
        winner.score += points_given
    
    text_y += 30    
    
    winning_names = ", ".join(winner.name for winner in winners)

    text_surface = font.render(f"The winning score is: {highest_bid}." , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50

    text_surface = font.render(f"{points_given:.2f} points to {winning_names}!" , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 50

    text_surface = font.render(f"Scores: " , True, WHITE)
    screen.blit(text_surface, (50, text_y))
    text_y += 40

    for player in players:
        text = f"-> {player.name}: {player.score:.2f}"
        text_surface = font_footer.render(text, True, WHITE)
        screen.blit(text_surface, (50, text_y))
        text_y += 20


    # Update the display
    pygame.display.flip()

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                
        pygame.display.flip()
