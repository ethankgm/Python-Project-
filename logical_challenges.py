import random

def display_sticks(n):
    """
    Displays the remaining number of sticks visually and numerically.
    :param n: The current number of sticks remaining in the game.
    """
    print("Remaining sticks:", "|" * n)
    print("Number of remaining sticks:", n)

def player_removal(n):
    """
    Allows the player to remove a certain number of sticks (1, 2, or 3) during their turn.
    Ensures valid input and checks that the player doesn't remove more sticks than remaining.
    :param n: The current number of sticks remaining in the game.
    :return: The number of sticks the player decides to remove.
    """
    while True:
        try:
            removal = int(input("How many sticks do you want to remove (1, 2, or 3)? "))
            if 1 <= removal <= 3 and removal <= n:
                return removal
            else:
                print("Invalid number. Please choose between 1 and 3, and no more than the remaining sticks.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def master_removal(n):
    """
    The game master's logic for removing sticks. The master removes (n - 1) % 4 sticks, ensuring
    it plays strategically. If no optimal move, it removes a random number of sticks.
    :param n: The current number of sticks remaining in the game.
    :return: The number of sticks the game master decides to remove.
    """
    removal = (n - 1) % 4
    if removal == 0:
        removal = random.randint(1, min(3, n))  # Randomize if no strategic move is available.
    print(f"The game master removes {removal} stick(s).")
    return removal

def nim_game():
    """
    Main game loop for the Nim game. The game continues until all sticks are removed. The player and the
    game master alternate turns to remove between 1 and 3 sticks.
    :return: Boolean value indicating if the player wins (True) or loses (False).
    """
    total_sticks = 20
    player_turn = True  # Player starts first.

    while total_sticks > 0:
        display_sticks(total_sticks)  # Display the current number of sticks.
        if player_turn:
            print("Player's turn.")
            removal = player_removal(total_sticks)
        else:
            print("Game master's turn.")
            removal = master_removal(total_sticks)

        total_sticks -= removal  # Update the total number of sticks.

        # Check if the game is over.
        if total_sticks == 0:
            if player_turn:
                print("The player removed the last stick. The game master wins!")
                return False
            else:
                print("The game master removed the last stick. The player wins!")
                return True

        player_turn = not player_turn  # Switch turns after each removal.

if __name__ == "__main__":
    if nim_game():
        print("Congratulations! You won the game of Nim!")
    else:
        print("Better luck next time. The game master won.")