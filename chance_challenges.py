import random

# Shell Game
def shell_game():
    shells = ['A', 'B', 'C']
    attempts = 0
    key_shell = None

    print("Welcome to the Shell Game!")
    print("You have 2 attempts to find the key hidden under one of the shells: A, B, or C.")

    for attempt in range(1, 3):
        key_shell = random.choice(shells)
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
    attempts = 3

    for attempt in range(attempts):
        print(f"Attempts remaining: {attempts - attempt}")
        input("Press 'Enter' to roll the dice...")

        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Player rolled: {player_dice}")

        if 6 in player_dice:
            print("Player wins!")
            return True

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
    return "Challenge One Completed!"

def challenge_two():
    return "Challenge Two Completed!"

def chance_challenge():
    challenges = [challenge_one, challenge_two]
    challenge = random.choice(challenges)
    return challenge()

# Test games
shell_game()
roll_dice_game()