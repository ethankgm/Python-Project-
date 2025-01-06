import random

# Shell Game
def shell_game():
    """
    Function to play the shell game where the key is hidden under one of the shells.
    The player has 2 attempts to guess the correct shell.
    """
    shells = ['A', 'B', 'C']
    attempts = 0
    key_shell = random.choice(shells)  # Randomly choose the shell hiding the key

    print("Welcome to the Shell Game!")
    print("You have 2 attempts to find the key hidden under one of the shells: A, B, or C.")

    # Loop through the 2 attempts
    for attempt in range(1, 3):
        print(f"\nRemaining attempts: {2 - attempts}")
        player_choice = input("Choose a shell (A, B, or C): ").upper()

        if player_choice in shells:
            if player_choice == key_shell:
                print(f"Congratulations! You found the key under shell {player_choice}.")
                return True
            else:
                print(f"Sorry, the key was not under shell {player_choice}.")
        else:
            print("Invalid choice. Please choose A, B, or C.")

        attempts += 1

    print(f"You've lost! The key was under shell {key_shell}.")
    return False

# Dice Game
def roll_dice_game() -> bool:
    """
    Function to play the dice game where both the player and the game master roll dice.
    The player wins if they roll a 6, and the game master wins if they roll a 6.
    The player has 3 attempts.
    """
    attempts = 3

    for attempt in range(attempts):
        print(f"Attempts remaining: {attempts - attempt}")
        input("Press 'Enter' to roll the dice...")

        # Rolling dice for the player
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Player rolled: {player_dice}")

        if 6 in player_dice:
            print("Player wins!")
            return True

        # Rolling dice for the game master
        game_master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Game Master rolled: {game_master_dice}")

        if 6 in game_master_dice:
            print("Game Master wins!")
            return False

        print("No winner this attempt, moving to the next one.")

    print("No player scored a 6 after three tries. It's a draw.")
    return False

# Chance Challenge
def challenge_one():
    """
    Sample challenge one.
    """
    return "Challenge One Completed!"

def challenge_two():
    """
    Sample challenge two.
    """
    return "Challenge Two Completed!"

def chance_challenge():
    """
    Randomly selects a challenge from the available ones.
    """
    challenges = [challenge_one, challenge_two]
    challenge = random.choice(challenges)
    return challenge()

# Test games
print("Starting Shell Game:")
shell_game()

print("\nStarting Dice Game:")
roll_dice_game()