import json
import random


def load_riddles(file):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():
    riddles = load_riddles('PFRiddles.json')
    riddle = random.choice(riddles)
    print(riddle['question'])

    attempts = 3
    while attempts > 0:
        answer = input("Your answer: ").lower()
        if answer == riddle['answer'].lower():
            print("Correct! You win a key!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left.")
            else:
                print(f"Defeat! The correct answer was: {riddle['answer']}")
                return False