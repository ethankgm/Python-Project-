import random


def game():
    print("Welcome to the Adventure Game!")
    print("You will create a team of players and face various challenges.")

    team = []
    while len(team) < 3:
        player_name = input(f"Enter the name of player {len(team) + 1}: ").strip()

        # Ensure player names are unique and not empty
        if not player_name:
            print("Player name cannot be empty! Try again.")
            continue
        if any(player['name'].lower() == player_name.lower() for player in team):
            print(f"The name '{player_name}' is already taken. Please choose a different name.")
            continue

        team.append({"name": player_name, "keys": 0})

    keys_needed = 3
    while True:
        print("\nSelect a challenge type:")
        challenge_types = ["Physical", "Mental", "Mystery"]
        for i, challenge in enumerate(challenge_types, 1):
            print(f"{i}. {challenge}")

        # Challenge type selection with input validation
        try:
            challenge_choice = int(input("Choose a challenge type (1-3): ")) - 1
            if challenge_choice not in range(len(challenge_types)):
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        print("\nSelect a player:")
        for i, player in enumerate(team, 1):
            print(f"{i}. {player['name']} (Keys: {player['keys']})")

        # Player selection with input validation
        try:
            player_choice = int(input("Choose a player (1-3): ")) - 1
            if player_choice not in range(len(team)):
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        # Simulate a challenge (randomly chosen result with narrative)
        challenge_result = random.choice([True, False])  # Simulating win/lose
        challenge_type = challenge_types[challenge_choice]

        if challenge_result:
            team[player_choice]['keys'] += 1
            print(
                f"{team[player_choice]['name']} won the {challenge_type} challenge! Keys: {team[player_choice]['keys']}")
        else:
            print(f"{team[player_choice]['name']} lost the {challenge_type} challenge.")

        # Ensure no player has more than 3 keys
        if team[player_choice]['keys'] > keys_needed:
            team[player_choice]['keys'] = keys_needed

        # Check if any player has obtained all the keys
        if any(player['keys'] >= keys_needed for player in team):
            print("\nAll keys obtained! Time for the final challenge.")
            break

    # Final challenge
    print("You have entered the treasure room!")
    code_word = "treasure"
    attempts = 3
    while attempts > 0:
        guess = input(f"Guess the code word to unlock the room (Attempts left: {attempts}): ")
        if guess.lower() == code_word:
            print("Congratulations! You've unlocked the treasure room and won the game!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect. Try again!")
            else:
                print("Sorry, that's not the correct code word. You lost the game.")


# Run the game
if __name__ == "__main__":
    game()