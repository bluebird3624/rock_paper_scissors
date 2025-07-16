import generate_computer_choice
import get_user_choice
import get_winner
import get_game_opponent

def main():
    horizontal_line = "_________________________________________________________"
    winners_message = "congratulation you win!"
    lossers_message = "sorry you lose"
    tie_message = "It's a tie"

    print(horizontal_line)
    print("Rock Paper Scissors Game")
    print(horizontal_line)

    # ask for game type
    opponent_type = get_game_opponent.get_game_opponent()
    # decide if to ask for input from two players or to generate from player 2
    player_one = ""
    player_two = ""

    player_one_name = "Player 1"
    player_two_name = ""

    print(horizontal_line)
    print(f"Player 1:")
    print(horizontal_line)
    player_one = get_user_choice.get_user_choice()

    if opponent_type == 1:
        player_two = generate_computer_choice.get_computer_choice()
    elif opponent_type == 2:
        print(f"Player 2:\n")
        player_two = get_user_choice.get_user_choice()
    else:
        print(f"{opponent_type} is not a valid option, something went wrong")
    # determine winner
    winner = get_winner.get_winner(player_one,player_two)

    if opponent_type == 1:
        player_two_name = "System Player"
    else:
        player_two_name = "Player 2"

    print(horizontal_line)
    print(f"{player_one_name} Picked {player_one} while {player_two_name} picked {player_two}\n")

    # print winner message
    if winner == 0:
        print(tie_message)
    elif winner == 1:
        if opponent_type == 1:
            print(winners_message)
        else:
            print(f"Player 1 {winners_message}")
    else:
        if opponent_type == 1:
            print(lossers_message)
        else:
            print(f"Player 2 {winners_message}")
    print(horizontal_line)

if __name__ == "__main__":
    main()