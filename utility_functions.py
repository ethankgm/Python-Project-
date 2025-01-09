import random


def introduction():
    print("Welcome to the Fort Boyard Simulator!")
    print("In this game, your team will face various challenges to earn keys.")
    print("Collect 3 keys to access the treasure room and win the game!\n")


def compose_equipe():
    team = []
    num_players = int(input("Enter the number of players in your team (1 to 3): "))

    while num_players < 1 or num_players > 3:
        print("Invalid number of players. Please enter between 1 and 3.")
        num_players = int(input("Enter the number of players in your team (1 to 3): "))

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

    is_leader_found = False

    for player in team:

        if player["is_leader"]:
            is_leader_found = True
            break

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

    choice = int(input("Enter the number of your choice: "))

    while choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please select a valid challenge.")
        choice = int(input("Enter the number of your choice: "))

    return choice


def choose_player(team):
    print("\nWho will take on this challenge?")

    # Show all players
    for i in range(len(team)):
        player = team[i]
        if player["is_leader"]:
            print(f"{i + 1}. {player['name']} - Team Leader")
        else:
            print(f"{i + 1}. {player['name']}")

    # Get player choice
    choice = int(input("Type a number to choose: "))

    while choice < 1 or choice > len(team):
        print("Oops! That's not a valid choice.")
        choice = int(input("Try again! Type a number: "))

    return team[choice - 1]


if __name__ == "_main_":
    introduction()
    team = compose_equipe()
    print("\nYour team:")
    for player in team:
        print(player)

    challenge = challenges_menu()
    print(f"\nYou selected challenge {challenge}.")

    selected_player = choose_player(team)
    print(f"\nPlayer selected: {selected_player['name']} ({selected_player['profession']})")