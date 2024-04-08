from cards import *

class Player:
  """Represents a player in the game"""
  def __init__(self, name, isBot = False, isRandom = False):
    self.name = name
    self.hand = []
    self.score = 0
    self.isBot = isBot
    self.isRandom = isRandom

  def receive_cards(self, suit_name):
    """Gives the player a set of cards"""
    self.hand = Suits(suit_name).cards

  def get_hand_values(self):
    hand_values = []
    for card in self.hand:
        hand_values.append(card.value)
    return hand_values

  def choose_bid(self):
    """Prompts the player to choose a card for bidding (abstract method)"""
    pass  # Implement this method in subclasses

  def update_score(self, points):
    """Updates the player's score"""
    self.score += points

class HumanPlayer(Player):
  """Player subclass that takes bidding input from the user"""

  def choose_bid(self):
    """Prompts the user to choose a card for bidding"""
    while True:
      try:
        chosen_value = int(input(lang.ENTER_BID(self.name, self.get_hand_values())))
        for card in self.hand:
            if card.value == chosen_value:
              self.hand.remove(card)
              return card
        print(lang.CARD_NOT_IN_HAND_ERROR(chosen_value, self.get_hand_values()))

      except ValueError:
        print(lang.INVALID_INPUT_ERROR)

class BotPlayer(Player):
  def __init__(self, bot_no):
    name = lang.BOT_NAME + str(bot_no)
    super().__init__(name, True)  # Call parent class constructor

  def choose_bid(self, revealed_diamond, revealed_diamonds, opponent_cards):
    chosen_value = decide_bid(revealed_diamond.value, revealed_diamonds, self.get_hand_values(), opponent_cards)
    for card in self.hand:
        if card.value == chosen_value:
            self.hand.remove(card)
            return card
    

class RandomPlayer(Player):
    def __init__(self):
        super().__init__(lang.RANDOM_NAME, False, True)  # Call parent class constructor

    def choose_bid(self):
        card_chosen = random.choice(self.hand)
        self.hand.remove(card_chosen)
        return card_chosen

def divide_median(cards, revealed_diamond, higher_lower = "higher") -> int:
    cards = sorted(cards)
    if higher_lower == "higher":
        considered_cards = [card for card in cards if card >= revealed_diamond]
    else:
        considered_cards = [card for card in cards if card < revealed_diamond]

    n = len(considered_cards)
    if n == 0:
        if higher_lower == "higher":
            return max(cards)
        else:
            return min(cards)

    if n % 2 == 1:
        return considered_cards[(n - 1)//2]
    else:
        return considered_cards[(n + 1)//2]

def decide_bid(revealed_diamond, revealed_diamonds, my_cards, opponent_cards):
    """
    This function suggests a bid based on a given strategy, considering potential opponent cards.

    Args:
        revealed_diamond (int): Value of the diamond being bid on this round.
        revealed_diamonds (list): List of diamond values already won.
        my_cards (list): List of cards (integers) remaining in your hand.
        opponent_cards (list): List of cards (integers) remaining in the opponent's hand (all same suit) - This is a theoretical analysis considering possible scenarios.

    Returns:
        int: Suggested card value to bid with.
    """
    # print(revealed_diamond, revealed_diamonds, my_cards, opponent_cards)
    # Estimate remaining high-value diamonds
    all_diamonds = set(range(2, 15))
    remaining_diamonds = list(all_diamonds - set(revealed_diamonds)) + [revealed_diamond]
    highest_remaining_diamond = max(remaining_diamonds)
    lowest_remaining_diamond = min(remaining_diamonds)

    if revealed_diamond == highest_remaining_diamond:
    # Play aggressive if your max card is higher than opponent's max (assumed)
        if max(my_cards) > max(opponent_cards):
            return max(my_cards)
        else:
            # Play defensive, minimize point loss with lowest card
            return min(my_cards)

    if revealed_diamond == lowest_remaining_diamond:
        return min(my_cards)

    # Analyze potential opponent strategies based on their remaining cards (theoretical)
    opponent_card_estimate = "unknown"
    opponent_card_average = sum(opponent_cards) / len(opponent_cards)
    my_card_average = sum(my_cards) / len(my_cards)

    if abs(opponent_card_average - my_card_average) <= 2:
        opponent_card_estimate = "medium"
    elif opponent_card_average > my_card_average:  # Opponent likely has only low cards
        opponent_card_estimate = "high"
    else:
        opponent_card_estimate = "low"
    # print(opponent_card_estimate)
    # Bidding Strategy
    # Consider relative value and opponent strategy
    relative_value = (revealed_diamond - lowest_remaining_diamond + 1) / (highest_remaining_diamond - lowest_remaining_diamond + 1)
    # print(relative_value)
    bid_thresholds = {"high": 0.4, "medium": 0.6, "low": 0.75}
    bid_threshold = bid_thresholds.get(opponent_card_estimate, 0.6)  # Default to medium

    # Use higher cards for high relative value diamonds (priority)
    if relative_value >= bid_threshold:
        return divide_median(my_cards, revealed_diamond, "higher")
    else:
    # Use lower cards otherwise
        return divide_median(my_cards, revealed_diamond, "lower")
