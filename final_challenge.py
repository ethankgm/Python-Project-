import json
import random

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
        print("Congratulations! You've accessed the treasure room!")
    else:
        print("Better luck next time!")