import random as rand

def get_computer_choice():
    """
    Randomly select and return the computer's choice in Rock-Paper-Scissors.

    Returns:
        str: One of 'rock', 'paper', or 'scissors'.
    """
    choices = ["rock", "paper", "scissors"]
    return rand.choice(choices)
