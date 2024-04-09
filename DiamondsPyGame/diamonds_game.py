from players import *
import english_text as lang

class DiamondsGame:
    """Represents a game of Diamonds"""
    def __init__(self):
        self.players = []
        self.bots_added = 0
        self.diamond_pile = DiamondSuit().cards  # Complete diamond pile
        self.revealed_diamonds = []
        
    def add_human_player(self, name):
        """Adds a player to the game"""
        self.players.append(HumanPlayer(name))

    def add_bot(self):
        """Adds a player to the game"""
        self.bots_added += 1
        self.players.append(BotPlayer(self.bots_added))
    
    def add_random(self):
        """Adds a player to the game"""
        self.players.append(RandomPlayer())

    def setup_game(self):
        """Deals cards to players and sets up the diamond pile"""
        if not 2 <= len(self.players) <= 3:
            raise ValueError(lang.PLAYERS_NUMBER_ERROR)

		# Create card sets for players (spades or hearts)
        suits_available = [lang.SPADES, lang.HEARTS, lang.CLUBS]
        suit_given = 0
        
        for player in self.players:
            player.receive_cards(suits_available[suit_given])
            suit_given += 1
            
    def play_round(self, round_no, opponent = None):
        """Plays a single round of the game"""
        revealed_diamond = self.diamond_pile.pop(0)
        print(lang.round_details(round_no, revealed_diamond))
        self.revealed_diamonds.append(revealed_diamond.value)

        if opponent:
            opponent_hand = opponent.get_hand_values()
        
        bids = []
        highest_bid = 0
        winners = []
        
        for player in self.players:
            if player.isBot and opponent_hand:
                bid = player.choose_bid(revealed_diamond, self.revealed_diamonds, opponent_hand)
            else:
                bid = player.choose_bid()
			
            bids.append(bid)
			
            if bid.value > highest_bid:
                winners = [player]
                highest_bid = bid.value
            elif bid.value == highest_bid:
                winners.append(player)
        
        lang.print_bids_made(self.players, bids)

        if len(winners) > 1:
            # Tie
            points = revealed_diamond.value / len(winners)  # Split points equally
            for player in winners:
                player.update_score(points)
        else:
            # Single Winner
            points = revealed_diamond.value
            winners[0].update_score(points)
        
        lang.print_round_winners(winners, points, highest_bid)
        lang.print_round_scores(self.players)
    


# Function for testing ability of Bot
def diamonds_bot_vs_random():
    game = DiamondsGame()

    # Add players to the game
    game.add_bot()
    game.add_random()
    # Setup the game (deal cards, shuffle diamond pile)
    game.setup_game()
    opponent = game.players[1]

    # Play multiple rounds (adjust number of rounds as desired)
    for round_no in range(13):  # Play until all diamonds are revealed
        game.play_round(round_no + 1, opponent)

    # Display final scores
    max_score = 0
    winners = []
    for player in game.players:
        if player.score > max_score:
            winners = [player]
            max_score = player.score
        elif player.score == max_score:
            winners.append(player)

    bot_win, random_win = 0, 0

    for winner in winners:
        if winner.name == "Bot1":
            bot_win += 1
        else:
            random_win += 1
    return [bot_win, random_win]


def human_player_vs_bot(name1, name2="", name3=""):
    # Create a game instance
    game = DiamondsGame()
    
    # Add players to the game
    game.add_bot()
    game.add_human_player(name1)
    
    opponent = game.players[1]

    # if name2 != "":
    #     game.add_human_player(name2)
    #     if name3 != "":
    #         game.add_human_player(name3)

    # Setup the game (deal cards, shuffle diamond pile)
    game.setup_game()

    # Play multiple rounds (adjust number of rounds as desired)
    for round_no in range(13):  # Play until all diamonds are revealed
        game.play_round(round_no + 1, opponent)

    # Display final scores
    lang.print_final_scores(game.players)

# human_player_vs_bot("Dhvani")