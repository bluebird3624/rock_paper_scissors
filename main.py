import generate_computer_choice
import get_user_choice
import get_winner
import get_game_opponent


def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    horizontal_line = "_________________________________________________________"
    winners_message = "Congratulations, you win!"
    losers_message = "Sorry, you lose."
    tie_message = "It's a tie."

    print(horizontal_line)
    print("Rock Paper Scissors Game")
    print(horizontal_line)

    # Ask for game type
    opponent_type = get_game_opponent.get_game_opponent()

    # Prepare player names
    player_one_name = "Player 1"
    player_two_name = "Player 2" if opponent_type == 2 else "System Player"

    # Get choices
    print(horizontal_line)
    print(f"{player_one_name}:")
    print(horizontal_line)
    player_one = get_user_choice.get_user_choice()

    if opponent_type == 1:
        player_two = generate_computer_choice.get_computer_choice()
    elif opponent_type == 2:
        print(f"{player_two_name}:")
        player_two = get_user_choice.get_user_choice()
    else:
        print(f"{opponent_type} is not a valid option. Exiting.")
        return

    # Determine winner
    winner = get_winner.get_winner(player_one, player_two)

    # Display results
    print(horizontal_line)
    print(f"{player_one_name} picked {player_one} "
          f"while {player_two_name} picked {player_two}.\n")

    if winner == 0:
        print(tie_message)
    elif winner == 1:
        print(f"{player_one_name} {winners_message}")
    else:
        print(f"{player_two_name} {winners_message if opponent_type == 2 else losers_message}")
    print(horizontal_line)


if __name__ == "__main__":
    main()
