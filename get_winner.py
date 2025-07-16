def get_winner(player1, player2):
    """
    Determine the winner of a Rock-Paper-Scissors game.

    Args:
        player1 (str): The choice of player 1 ('rock', 'paper', or 'scissors').
        player2 (str): The choice of player 2 ('rock', 'paper', or 'scissors').

    Returns:
        int: 
            - 0 if it's a tie
            - 1 if player1 wins
            - 2 if player2 wins
    """
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if player1 == player2:
        return 0
    elif rules[player1] == player2:
        return 1
    else:
        return 2
