import sys
import pygame
import english_text_pygame as lang

# Initialize Pygame
pygame.init()

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


    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if self.text.strip().lower() in lang.quit_words:
                self.active = False

            elif event.key == pygame.K_RETURN:
                self.player_names.append(self.text.strip())
                self.text = ""  # Clear input field

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

def player_configuration(screen):
    # Initialize variables
    player_names = []  # List to store player names
    num_bots = 0
    num_randoms = 0
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
    
    # Create a single player input field initially
    player_input_field = PlayerInput(SCREEN_WIDTH/2 - 90, 100, 200, 30, "")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or len(player_names) >= 3 or not player_input_field.active:
                running = False
            elif event.type == pygame.KEYDOWN:
                player_input_field.handle_input(event)
                player_names = player_input_field.player_names

        # Draw background
        screen.fill(OPTION_SCREEN_COLOUR)

        screen_title = font.render(lang.enter_player_name(len(player_names) + 1) , True, WHITE)
        screen.blit(screen_title, (SCREEN_WIDTH/2 - 110, 20))

        screen_title = font_footer.render(lang.quit_message, True, WHITE)
        screen.blit(screen_title, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))

        # Draw player input field
        player_input_field.draw(screen)

        # Display player names with error handling
        name_y_pos = 50  # Adjust starting y-position
        for i, name in enumerate(player_names):
            try:
                # Attempt to render the name, handle potential exceptions
                name_text = font.render(lang.player_name(i+1, name), True, BLACK)
                screen.blit(name_text, (20, name_y_pos + i * font.get_linesize()))  # Adjust positioning
            except Exception as e:  # Catch generic exceptions for robustness
                print(lang.error_message(e))

        pygame.display.flip()

    if len(player_names) == 1:
        num_bots, num_randoms = button_choices(screen, "Play with Bot", "Play with Random")

    if len(player_names) == 2:
        _, num_randoms, num_bots = button_choices(screen, "Play among 2", "Add Random", "Add Bot")

    

    print(player_names, num_bots, num_randoms)
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

def button_clicked(BUTTON_X_START, BUTTON_START_Y, mouse_pos, BUTTON_WIDTH, BUTTON_HEIGHT):
        return (BUTTON_X_START) < mouse_pos[0] < (BUTTON_X_START + BUTTON_WIDTH) and \
                (BUTTON_START_Y) < mouse_pos[1] < (BUTTON_START_Y + BUTTON_HEIGHT)

# Main function
def button_choices(screen, text1, text2, text3 = ""):
    option1 = False
    option2 = False
    option3 = False

    MARGIN = 20

    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size() 

    LEFT_BUTTON_X_START = SCREEN_WIDTH / 2 - BUTTON_WIDTH - MARGIN/2
    RIGHT_BUTTON_X_START = LEFT_BUTTON_X_START + BUTTON_WIDTH + MARGIN
    END_BUTTON_X_START = RIGHT_BUTTON_X_START + BUTTON_WIDTH + MARGIN

    BUTTON_START_Y = 150


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

        # Draw text1 button
        draw_button(screen, LEFT_BUTTON_X_START, BUTTON_START_Y,
                    BUTTON_WIDTH, BUTTON_HEIGHT, text1, font_footer)

        # Draw text2 button
        draw_button(screen, RIGHT_BUTTON_X_START, BUTTON_START_Y,
                    BUTTON_WIDTH, BUTTON_HEIGHT, text2, font_footer)
        
        if text3 != "":
            draw_button(screen, END_BUTTON_X_START, BUTTON_START_Y,
                    BUTTON_WIDTH, BUTTON_HEIGHT, text3, font_footer)

        # Check if text1 button is clicked
        if button_clicked(LEFT_BUTTON_X_START, BUTTON_START_Y, mouse_pos, BUTTON_WIDTH, BUTTON_HEIGHT):
            if click:
                option1 = True

        # Check if text2 button is clicked
        if button_clicked(RIGHT_BUTTON_X_START, BUTTON_START_Y, mouse_pos, BUTTON_WIDTH, BUTTON_HEIGHT):
            if click:
                option2 = True
        
        # Check if text3 button is clicked
        if button_clicked(END_BUTTON_X_START, BUTTON_START_Y, mouse_pos, BUTTON_WIDTH, BUTTON_HEIGHT):
            if click and text3 != "":
                option3 = True

        # If "text1" button is clicked
        if option1:
            if text3 != "":
                return [1, 0, 0]
            else:
                return [1, 0]

        # If "text2" button is clicked
        if option2:
            if text3 != "":
                return [0, 1, 0]
            else:
                return [0, 1]
        
        # If "text3" button is clicked
        if option3:
            return [0, 0, 1]

        pygame.display.flip()

