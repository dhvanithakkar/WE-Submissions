SPADES = "Spades"
HEARTS = "Hearts"
CLUBS = "Clubs"
DIAMONDS = "Diamonds"
HIGHER_CARD_NAMES = ("Jack", "Queen", "King", "Ace")

def suit_name(name: str):
    return f"{name} suit"

def card_name(face_value, suit: str):
    return f"{face_value} of {suit}"

RANDOM_NAME = "Random"
BOT_NAME = "Bot"

PLAYERS_NUMBER_ERROR = "Diamonds requires 2 or 3 players"
INVALID_CARD_ERROR = "Invalid card suit or value"
INVALID_INPUT_ERROR = "Invalid input. Please enter a number."

def CARD_NOT_IN_HAND_ERROR(chosen_value: int, hand_values: list[int]):
    return f"Card with value {chosen_value} not found in your hand {hand_values}. Try again."

ENTER_BID = lambda name, hand_values: f"{name}, choose a card value to bid among {hand_values}: "

def print_bids_made(players, bids):
    print("Bids made:")
    for player, bid in zip(players, bids):
        print(f"{player.name} : {bid}")

round_details = lambda round_no, revealed_diamond: f"\nRound {round_no}: Revealed Diamond - {revealed_diamond}"


def print_final_scores(players):
    winners = []
    max_score = 0
    
    print("\nFinal Scores:")
    for player in players:
        print(f"{player.name}: {player.score} points")
        if player.score > max_score:
            winners = [player]
            max_score = player.score
        elif player.score == max_score:
            winners.append(player)

    print(f"\nThe winning score is: {max_score}")
    for winner in winners:
        print(winner.name, end=" ")
    print("won the game!!")

def print_round_winners(winners, points: int, highest_bid: int):
    if len(winners) > 1:
        print(f"\nTie. Diamond points: {points:.1f} split between:", end=" ")
        for player in winners:
            print(player.name, end = " ")
    else:
        print(f"\n{winners[0].name} wins the round with {highest_bid}! Earns {points} points.")

def print_round_scores(players):
    print("Scores: ")
    for player in players:
        print(player.name, ":", player.score)
