enter_player_name = lambda player_no: f"Enter Name of Player {player_no}:"
quit_words = ['quit', 'stop', 'exit']
quit_message = "Write 'quit' if finished" 
player_name = lambda player_no, player_name: f"Player {player_no}: {player_name}"

error_message = lambda e: f"Error rendering name: {e}"

final_scores = "Final Scores:"
scores = "Scores: " 
bids = "Bids: "

player_choose_bid = lambda name: f"{name}, pick your bid:" 
winning_bid = lambda highest_bid: f"The winning bid is: {highest_bid}." 
points_given = lambda points_given, winning_names: f"{points_given:.2f} points to {winning_names}!"

player_points= lambda player: f"-> {player.name}: {player.score :.2f} points"

round_no = lambda round_no: f"Round Number: {round_no}"

winning_score = lambda max_score: f"The winning score is: {max_score :.2f}"
winning_names = lambda winning_names: winning_names + " won the game!!"