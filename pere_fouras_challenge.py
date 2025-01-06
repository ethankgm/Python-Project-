import json
import random

def load_riddles(file):
    """
    Loads riddles from a specified JSON file.
    :param file: The path to the JSON file containing riddles.
    :return: A list of riddles loaded from the file.
    """
    try:
        with open(file, 'r') as f:
            riddles = json.load(f)
        return riddles
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON format.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def pere_fouras_riddles():
    """
    Selects a random riddle from the loaded riddles and starts the riddle challenge.
    The player has 3 attempts to answer the riddle correctly.
    :return: True if the player answers correctly, False otherwise.
    """
    riddles = load_riddles('PFRiddles.json')

    # Check if riddles were loaded successfully
    if not riddles:
        print("No riddles available to play.")
        return False

    riddle = random.choice(riddles)
    print(f"Riddle: {riddle['question']}")

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

# Test the function
pere_fouras_riddles()