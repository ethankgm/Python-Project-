def game():
    print("Welcome to the Adventure Game!")
    print("You will create a team of players and face various challenges.")

    team = []
    while len(team) < 3:
        player_name = input(f"Enter the name of player {len(team) + 1}: ")
        team.append({"name": player_name, "keys": 0})

    keys_needed = 3
    while True:
        print("\nSelect a challenge type:")
        challenge_types = ["Physical", "Mental", "Mystery"]
        for i, challenge in enumerate(challenge_types, 1):
            print(f"{i}. {challenge}")

        challenge_choice = int(input("Choose a challenge type (1-3): ")) - 1
        if challenge_choice not in range(len(challenge_types)):
            print("Invalid choice. Please try again.")
            continue

        print("\nSelect a player:")
        for i, player in enumerate(team, 1):
            print(f"{i}. {player['name']} (Keys: {player['keys']})")

        player_choice = int(input("Choose a player (1-3): ")) - 1
        if player_choice not in range(len(team)):
            print("Invalid choice. Please try again.")
            continue

        # Simulate a challenge (randomly chosen)
        import random
        challenge_result = random.choice([True, False])  # Simulating win/lose
        if challenge_result:
            team[player_choice]['keys'] += 1
            print(f"{team[player_choice]['name']} won the challenge! Keys: {team[player_choice]['keys']}")
        else:
            print(f"{team[player_choice]['name']} lost the challenge.")

        if any(player['keys'] >= keys_needed for player in team):
            print("\nAll keys obtained! Time for the final challenge.")
            break

    # Final challenge
    print("You have entered the treasure room!")
    code_word = "treasure"
    guess = input("Guess the code word to unlock the room: ")

    if guess.lower() == code_word:
        print("Congratulations! You've unlocked the treasure room and won the game!")
    else:
        print("Sorry, that's not the correct code word. You lost the game.")