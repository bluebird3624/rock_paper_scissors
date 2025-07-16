def get_game_opponent():
    while True:
        try:
            player_type = int(input(f"\nSelect game player Type:\n  1.Singleplayer\n  2.Multiplayer\n\nSelected: "))

            if 1 <= player_type <= 2:
                return player_type
            else:
                print("Please enter the number 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")