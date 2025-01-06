def introduction():
    print("Welcome to the Fort Boyard Simulator!")
    print("In this game, your team will face various challenges to earn keys.")
    print("Collect 3 keys to access the treasure room and win the game!\n")


def compose_equipe():
    team = []
    while True:
        try:
            num_players = int(input("Enter the number of players in your team (1 to 3): "))
            if 1 <= num_players <= 3:
                break
            else:
                print("Invalid number of players. Please enter between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    for i in range(num_players):
        print(f"\nEnter details for Player {i + 1}:")
        name = input("Name: ")
        profession = input("Profession: ")
        is_leader_input = input("Is this player the team leader? (yes/no): ").strip().lower()

        is_leader = is_leader_input == 'yes'

        player = {
            "name": name,
            "profession": profession,
            "is_leader": is_leader,
            "keys_won": 0
        }
        team.append(player)

    # Check if leader is assigned, otherwise assign the first player
    is_leader_found = any(player["is_leader"] for player in team)
    if not is_leader_found:
        print("No leader was chosen. The first player will be the leader by default.")
        team[0]["is_leader"] = True

    return team


def challenges_menu():
    print("\nSelect a challenge type:")
    print("1. Mathematics Challenge")
    print("2. Logic Challenge")
    print("3. Chance Challenge")
    print("4. Père Fouras' Riddle")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please select a valid challenge.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return choice


def choose_player(team):
    print("\nWho will take on this challenge?")

    # Show all players
    for i, player in enumerate(team):
        leader_tag = " - Team Leader" if player["is_leader"] else ""
        print(f"{i + 1}. {player['name']} ({player['profession']}){leader_tag}")

    while True:
        try:
            choice = int(input("Type a number to choose: "))
            if 1 <= choice <= len(team):
                return team[choice - 1]
            else:
                print("Oops! That's not a valid choice.")
        except ValueError:
            print("Oops! Please enter a valid number.")

def record_history(challenge_name, player, result, keys_obtained):
    with open('output/history.txt', 'a') as file:
        file.write(f"Challenge: {challenge_name}\n")
        file.write(f"Player: {player['name']} ({player['profession']})\n")
        file.write(f"Result: {result}\n")
        file.write(f"Keys Obtained: {keys_obtained}\n")
        file.write("----------\n")

def challenge_result(challenge_type, player):
    # Placeholder for challenges. In a real game, you should implement logic for each challenge type
    if challenge_type == 1:
        print("Mathematics Challenge...")
        player['keys_won'] += 1  # Simulating winning a key
    elif challenge_type == 2:
        print("Logic Challenge...")
        player['keys_won'] += 1  # Simulating winning a key
    elif challenge_type == 3:
        print("Chance Challenge...")
        player['keys_won'] += 1  # Simulating winning a key
    elif challenge_type == 4:
        print("Père Fouras' Riddle...")
        player['keys_won'] += 1  # Simulating winning a key

    print(f"Player {player['name']} won a key!")
    return player['keys_won']

def introduction_and_game():
    introduction()
    team = compose_equipe()
    print("\nYour team:")
    for player in team:
        print(f"{player['name']} ({player['profession']})")

    challenge = challenges_menu()
    print(f"\nYou selected challenge {challenge}.")

    selected_player = choose_player(team)
    print(f"\nPlayer selected: {selected_player['name']} ({selected_player['profession']})")

    keys_obtained = challenge_result(challenge, selected_player)
    print(f"{selected_player['name']} has {keys_obtained} keys.")

    # Record the history of the challenge
    record_history("Sample Challenge", selected_player, "Won", keys_obtained)

    if keys_obtained >= 3:
        print("\nCongratulations! You've unlocked the treasure room!")
    else:
        print("\nKeep trying! You need 3 keys to access the treasure room.")

if __name__ == "__main__":
    introduction_and_game()