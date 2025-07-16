def get_user_choice():
    """
    Prompt the user to select Rock, Paper, or Scissors.

    Returns:
        str: The user's choice as a lowercase string ('rock', 'paper', or 'scissors').

    Continues to prompt until a valid input (1, 2, or 3) is entered.
    """
    choices = {1: "rock", 2: "paper", 3: "scissors"}

    while True:
        try:
            input_choice = int(input(
                "Pick one:\n  1. Rock\n  2. Paper\n  3. Scissors\n\nYour choice: "
            ))
            if 1 <= input_choice <= 3:
                return choices[input_choice]
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
