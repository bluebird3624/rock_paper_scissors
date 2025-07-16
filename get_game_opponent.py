def get_game_opponent():
    """
    Prompt the user to select the game mode (singleplayer or multiplayer).

    Returns:
        int: 
            - 1 for Singleplayer
            - 2 for Multiplayer

    Continues to prompt until valid input is entered.
    """
    while True:
        try:
            player_type = int(input(
                "\nSelect game player type:\n  1. Singleplayer\n  2. Multiplayer\n\nSelected: "
            ))

            if 1 <= player_type <= 2:
                return player_type
            else:
                print("Please enter the number 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
