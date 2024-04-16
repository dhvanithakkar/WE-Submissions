import pygame
from diamonds_game import *
from pygame_display import *

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 600
CARD_WIDTH, CARD_HEIGHT = 80, 120
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50

MARGIN = 20

CARDS_START_Y = SCREEN_HEIGHT - CARD_HEIGHT - MARGIN

GREEN = (0, 100, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY  = (50, 50, 50)
RED  = (207, 0, 0)

BACKGROUND_COLOR = GREEN

class Diamonds_PyGame:
    
    def __init__(self, screen):   
        self.NUM_ROUNDS = 13
        self.game = DiamondsGame()
        self.screen = screen
        clear_to_main_background(self.screen)
    
    def add_players(self, num_bots: int, num_randoms: int, human_names: list[str]):
        if num_bots > 0:
            self.game.add_bot()
            self.game.add_human_player(human_names[0])
            return
        
        for random in range(num_randoms):
            self.game.add_random()
        
        for human_name in human_names:
            self.game.add_human_player(human_name)
    
    def choose_bid_human_GUI(self, player, screen):
        """Allows the player to choose a card for bidding using a graphical interface"""
        
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        for card in player.hand:
                            if card.is_clicked(mouse_pos):
                                player.hand.remove(card)
                                return card

            pygame.display.flip()
    
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


    def play_GUI_round(self, round_no, opponent = None):
        """Display the game state on the screen"""
        clear_to_main_background(self.screen)
        
        print_round_title(self.screen, round_no, SCREEN_WIDTH)
        display_scores_on_main(screen, self.game.players)
        
        # player = self.game.players[0]
        # display_player_hand(player.hand, CARD_WIDTH, CARD_HEIGHT, self.screen, CARDS_START_Y, player.name)

        revealed_diamond = self.game.diamond_pile.pop(0)
        self.game.revealed_diamonds.append(revealed_diamond.value)


        if opponent:
            opponent_hand = opponent.get_hand_values()
        
        bids = []
        highest_bid = 0
        winners = []

        for player in self.game.players:
            if player.isBot and opponent_hand:
                bid = player.choose_bid(revealed_diamond, self.game.revealed_diamonds, opponent_hand)
            elif player.isRandom:
                bid = player.choose_bid()
            else:
                # Display cards in the players' hands
                clear_to_main_background(self.screen)
                print_round_title(self.screen, round_no, SCREEN_WIDTH)
                display_scores_on_main(screen, self.game.players)

                revealed_diamond.display_card(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT, )
                display_player_hand(player.hand, CARD_WIDTH, CARD_HEIGHT, self.screen, CARDS_START_Y, player.name)

                bid = self.choose_bid_human_GUI(player, screen)
			
            bids.append(bid)
			
            if bid.value > highest_bid:
                winners = [player]
                highest_bid = bid.value
            elif bid.value == highest_bid:
                winners.append(player)
                
        display_bids_and_winners(self.screen, bids, self.game.players, winners, highest_bid, round_no, revealed_diamond.value)    
        
##################  MAIN
        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
running = True

human_names, num_bots, num_randoms = player_configuration(screen)

py_game = Diamonds_PyGame(screen)

py_game.add_players(num_bots, num_randoms, human_names)
py_game.game.setup_game()

opponent = py_game.game.players[1]
on_round = 1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    py_game.play_GUI_round(on_round, opponent) # on_round, opponent

    on_round += 1

    if on_round > py_game.NUM_ROUNDS:
            display_final_scores(py_game.game.players, screen)
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # flip() the display to put your work on screen
    # pygame.display.flip()
    
    # screen.fill(BACKGROUND_COLOR)


pygame.quit()

