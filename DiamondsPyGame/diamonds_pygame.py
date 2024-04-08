import pygame
from diamonds_game import *

HEIGHT = 720
WIDTH = 1280


GREEN = (0, 100, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY  = (50, 50, 50)
RED  = (207, 0, 0)


class Diamonds_PyGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Diamonds Card Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = DiamondsGame()

    def main_game_loop(self):
       
       
       self.game.setup_game()

       while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            


            
  # Handle game logic here (dealing cards, bidding, rounds, scores)
  # Update game state based on user interaction (clicks, selections)

  # Clear the screen
  screen.fill((0, 128, 0))

  # Draw game elements (cards, text, buttons)
  # Use Card.draw() or similar methods to draw cards on the screen

  # Update the display
  pygame.display.flip()

pygame.quit()

pygame.quit()
