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

import json

def treasure_room():
    with open('TRClues.json') as f:
        tv_game = json.load(f)

    year = random.choice(list(tv_game.keys()))
    show = random.choice(tv_game[year]['programs'])
    clues = tv_game[year]['programs'][show]['clues']
    code_word = tv_game[year]['programs'][show]['codeword']

    print("Clue 1:", clues[0])
    print("Clue 2:", clues[1])
    print("Clue 3:", clues[2])

    attempts = 3
    answer_correct = False

    while attempts > 0:
        answer = input("Enter your guess for the code word: ")
        if answer.lower() == code_word.lower():
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer! You have {attempts} attempts left.")
                print("Additional clue:", clues[3 - attempts])  # Provide an additional clue
            else:
                print(f"Sorry, the correct code word was: {code_word}")

    if answer_correct:
        print("Congratulations! You've unlocked the treasure room!")
    else:
        print("Better luck next time!")