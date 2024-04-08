import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
VERMILLION = (173, 75, 64)

# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

OPTION_SCREEN_COLOUR = VERMILLION

pygame.init() 
font = pygame.font.Font(None, 36)# Use default font
font_footer = pygame.font.Font(None, 24)# Use default font

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
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
    
    # Create a single player input field initially
    player_input_field = PlayerInput(SCREEN_WIDTH/2 - 20, 100, 200, 30, "")

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
        screen.fill(OPTION_SCREEN_COLOUR)

        screen_title = font.render(f"Enter Name of Player {len(player_names) + 1}:" , True, WHITE)
        screen.blit(screen_title, (SCREEN_WIDTH/2 - 40, 20))

        screen_title = font_footer.render(f"Write 'quit' if finished" , True, WHITE)
        screen.blit(screen_title, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))

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

    if len(player_names) == 1:
        num_bots, num_randoms = bot_or_random(screen)

    if len(player_names) == 2:
        num_randoms = add_random(screen)
    
    print(player_names)
    return [player_names, num_bots, num_randoms]


# Function to draw text on button
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# Function to draw button
def draw_button(screen, x, y, width, height, text, font):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    draw_text(screen, text, font, BLACK, x + width / 2, y + height / 2)

# Main function
def bot_or_random(screen):

    play_with_bot = False
    play_with_random = False

    while True:
        # Get mouse position and click events
        mouse_pos = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Draw "Play with bot" button
        draw_button(screen, SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 - 50,
                    BUTTON_WIDTH, BUTTON_HEIGHT, "Play with bot", font_footer)

        # Draw "Play with random" button
        draw_button(screen, SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 + 50,
                    BUTTON_WIDTH, BUTTON_HEIGHT, "Play with random", font_footer)

        # Check if "Play with bot" button is clicked
        if (SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2) < mouse_pos[0] < (SCREEN_WIDTH / 2 + BUTTON_WIDTH / 2) and \
                (SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 - 50) < mouse_pos[1] < (SCREEN_HEIGHT / 2 + BUTTON_HEIGHT / 2 - 50):
            if click:
                play_with_bot = True

        # Check if "Play with random" button is clicked
        if (SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2) < mouse_pos[0] < (SCREEN_WIDTH / 2 + BUTTON_WIDTH / 2) and \
                (SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 + 50) < mouse_pos[1] < (SCREEN_HEIGHT / 2 + BUTTON_HEIGHT / 2 + 50):
            if click:
                play_with_random = True

        # Display "Playing with bot" if "Play with bot" button is clicked
        if play_with_bot:
            return [1,0]
            draw_text(screen, "Playing with bot", font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)

        # Display "Playing with random" if "Play with random" button is clicked
        if play_with_random:
            return [0,1]
            draw_text(screen, "Playing with random", font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)

        pygame.display.flip()

def add_random(screen):

    play_among_2 = False
    play_with_random = False

    while True:
        # Get mouse position and click events
        mouse_pos = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Draw "Play among 2" button
        draw_button(screen, SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 - 50,
                    BUTTON_WIDTH, BUTTON_HEIGHT, "Play among two", font_footer)

        # Draw "Play with random" button
        draw_button(screen, SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 + 50,
                    BUTTON_WIDTH, BUTTON_HEIGHT, "Add Random Player", font_footer)

        # Check if "Play with bot" button is clicked
        if (SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2) < mouse_pos[0] < (SCREEN_WIDTH / 2 + BUTTON_WIDTH / 2) and \
                (SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 - 50) < mouse_pos[1] < (SCREEN_HEIGHT / 2 + BUTTON_HEIGHT / 2 - 50):
            if click:
                play_among_2 = True

        # Check if "Play with random" button is clicked
        if (SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2) < mouse_pos[0] < (SCREEN_WIDTH / 2 + BUTTON_WIDTH / 2) and \
                (SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2 + 50) < mouse_pos[1] < (SCREEN_HEIGHT / 2 + BUTTON_HEIGHT / 2 + 50):
            if click:
                play_with_random = True

        # Display "Playing with bot" if "Play with bot" button is clicked
        if play_among_2:
            return 0
            draw_text(screen, "Playing with bot", font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)

        # Display "Playing with random" if "Play with random" button is clicked
        if play_with_random:
            return 1
            draw_text(screen, "Playing with random", font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)

        pygame.display.flip()
