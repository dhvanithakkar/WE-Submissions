import pygame
from cards import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
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
    # def round_tester(self, round_no, opponent = None):
    #     clear_to_main_background(self.screen)
        
    #     print_round_title(self.screen, round_no, SCREEN_WIDTH)
        
    #     diam = Card("Diamonds", 11)
    #     diam.display_card(self.screen, 100, 100, CARD_WIDTH, CARD_HEIGHT)
    #     chosen_card = ""

    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #             elif event.type == pygame.MOUSEBUTTONDOWN:
    #                 if event.button == 1:  # Left mouse button
    #                     mouse_pos = pygame.mouse.get_pos()
    #                     print(mouse_pos)
    #                     if diam.is_clicked(mouse_pos):
    #                         chosen_card = diam
    #                         return chosen_card
    #                         running = False  # Exit loop once card is chosen
    #                         break
        
    #     print(chosen_card)



diam = Card("Diamonds", 14)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    pygame.draw.circle(screen, "red", player_pos, 40)

    # diam.display_card(screen, 150, 150)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
