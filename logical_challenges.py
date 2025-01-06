import random
def display_sticks(n):
    print("Remaining sticks:", "|" * n)
    print("number of remaining stick:", n)

def player_removal(n):
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
    removal = (n - 1) % 4
    if removal == 0:
        removal = random.randint(1, min(3, n))
    print(f"The game master removes {removal} stick(s).")
    return removal

def nim_game():
    total_sticks = 20
    player_turn = True

    while total_sticks > 0:
        display_sticks(total_sticks)
        if player_turn:
            print("Player's turn.")
            removal = player_removal(total_sticks)
        else:
            print("Game master's turn.")
            removal = master_removal(total_sticks)

        total_sticks -= removal
        if total_sticks == 0:
            if player_turn:
                print("The player removed the last stick. The game master wins!")
                return False
            else:
                print("The game master removed the last stick. The player wins!")
                return True

        player_turn = not player_turn

if __name__ == "__main__":
    if nim_game():
        print("Congratulations! You won the game of Nim!")
    else:
        print("Better luck next time. The game master won.")