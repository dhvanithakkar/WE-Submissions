import pygame

GREEN = (0, 100, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY  = (50, 50, 50)
RED  = (207, 0, 0)

BACKGROUND_COLOR = GREEN

pygame.init() 
font = pygame.font.Font(None, 36)# Use default font

# Define player input field class
class PlayerInput:
    def __init__(self, x, y, width, height, default_text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = default_text
        self.active = True  # Make the input field active initially
        self.player_names = []

    def draw(self, screen):
        color = WHITE if self.active else BLACK
        pygame.draw.rect(screen, color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    # def handle_click(self):
    #     self.active = not self.active

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if self.text.strip().lower() in ['quit', 'stop']:
                self.active = False

            elif event.key == pygame.K_RETURN:
                self.player_names.append(self.text.strip())
                self.text = ""  # Clear input field

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

def player_configuration(screen):
    # Initialize Pygame

    pygame.display.set_caption("Player Input")

    # Initialize variables
    player_names = []  # List to store player names
    num_bots = 0
    num_randoms = 0
    # Create a single player input field initially
    player_input_field = PlayerInput(100, 150, 200, 30, "")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or len(player_names) >= 3 or not player_input_field.active:
                running = False
            elif event.type == pygame.KEYDOWN:
                player_input_field.handle_input(event)
                player_names = player_input_field.player_names

            # Handle player input field click (activate/deactivate)
            # if player_input_field.rect.collidepoint(pygame.mouse.get_pos()):
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         player_input_field.handle_click()

        # Draw background
        screen.fill(BACKGROUND_COLOR)

        # Draw player input field
        player_input_field.draw(screen)

        # Display player names with error handling
        name_y_pos = 50  # Adjust starting y-position
        for i, name in enumerate(player_names):
            try:
                # Attempt to render the name, handle potential exceptions
                name_text = font.render(f"Player {i+1}: {name}", True, BLACK)
                screen.blit(name_text, (20, name_y_pos + i * font.get_linesize()))  # Adjust positioning
            except Exception as e:  # Catch generic exceptions for robustness
                print(f"Error rendering name: {e}")

        pygame.display.flip()
    #------------------------
    # if len(player_names) == 1:
    #     num_bots, num_randoms = bot_or_random(screen)

    # if len(player_names) == 2:
    #     num_randoms = add_random(screen)
    
    print(player_names)
    return [player_names, num_bots, num_randoms]


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


def display_player_hand(hand, CARD_WIDTH, CARD_HEIGHT, screen, start_y):
    screen.fill(BLACK)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    total_cards = len(hand)

    overlap_gap = CARD_WIDTH + 1
    MARGIN = 10

    start_x = MARGIN
    # start_y = SCREEN_HEIGHT - CARD_HEIGHT - MARGIN  # 10 pixels above the bottom of the screen


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
            screen.blit(round_title, (SCREEN_WIDTH/2, 20))

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
