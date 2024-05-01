from diamonds_game import * 
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


player_name = input("Enter your name:")
human_player_vs_bot(player_name)
