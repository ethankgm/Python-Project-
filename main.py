import math_challenges
import chance_challenges
import logical_challenges
import final_challenge


def game():
    print("Welcome to the Adventure Game!")
    print("You will create a team of players and face various challenges.")

    team = []
    while len(team) < 3:
        player_name = input(f"Enter the name of player {len(team) + 1}: ").strip()
        if not player_name:
            print("Player name cannot be empty! Try again.")
            continue
        team.append({"name": player_name, "keys": 0})

    keys_needed = 3
    event_history = []

    while all(player["keys"] < keys_needed for player in team):
        print("\nSelect a challenge type:")
        print("1. Math Challenge")
        print("2. Chance Challenge")
        print("3. Logical Challenge")

        # Validate challenge type input
        challenge_type = input("Enter the number of the challenge type (1-3): ").strip()
        if challenge_type not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        print("\nSelect a player:")
        for idx, player in enumerate(team):
            print(f"{idx + 1}. {player['name']} (Keys: {player['keys']})")

        # Validate player choice
        try:
            player_choice = int(input("Choose a player by number: ").strip()) - 1
            if player_choice not in range(len(team)):
                raise ValueError
        except ValueError:
            print("Invalid player choice. Please try again.")
            continue

        # Run the selected challenge
        if challenge_type == '1':
            result = math_challenges.run_challenge(team[player_choice])
        elif challenge_type == '2':
            result = chance_challenges.run_challenge(team[player_choice])
        elif challenge_type == '3':
            result = logical_challenges.run_challenge(team[player_choice])

        # Record the event
        event_history.append({
            "challenge_type": challenge_type,
            "player": team[player_choice]["name"],
            "result": result
        })

        # Update keys and notify the player
        if result:
            team[player_choice]["keys"] += 1
            print(f"{team[player_choice]['name']} won the challenge! Keys: {team[player_choice]['keys']}")
        else:
            print(f"{team[player_choice]['name']} lost the challenge.")

    print("\nAll players have won 3 keys! Time for the final challenge.")
    final_result = final_challenge.run_final_challenge()

    # Write event history to a file
    with open('output/history.txt', 'w') as f:
        for event in event_history:
            f.write(f"{event}\n")

    if final_result:
        print("Congratulations! You've unlocked the treasure room!")
    else:
        print("Sorry, you couldn't unlock the treasure room. Better luck next time!")


if __name__ == "__main__":
    game()
