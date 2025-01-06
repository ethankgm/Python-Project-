import json
import random


def load_tv_game_data(file_path):
    """
    Loads the TV game data from a specified JSON file.
    :param file_path: The path to the JSON file containing the TV game data.
    :return: The parsed JSON data or None if there's an error.
    """
    try:
        with open(file_path) as f:
            tv_game_data = json.load(f)
        return tv_game_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON format.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def select_random_clues(tv_game_data):
    """
    Selects a random year, show, and clues from the TV game data.
    :param tv_game_data: The parsed JSON data containing the TV game information.
    :return: A tuple containing the clues and the correct code word.
    """
    year = random.choice(list(tv_game_data.keys()))
    show = random.choice(tv_game_data[year]['programs'])
    clues = tv_game_data[year]['programs'][show]['clues']
    code_word = tv_game_data[year]['programs'][show]['codeword']

    return clues, code_word


def present_clues(clues):
    """
    Prints the clues to the player.
    :param clues: A list of clues to display to the player.
    """
    print("Clue 1:", clues[0])
    print("Clue 2:", clues[1])
    print("Clue 3:", clues[2])


def guess_code_word(clues, code_word):
    """
    Allows the player to guess the code word, providing clues and tracking attempts.
    :param clues: A list of clues.
    :param code_word: The correct code word.
    :return: True if the player guesses correctly, False otherwise.
    """
    attempts = 3
    while attempts > 0:
        answer = input("Enter your guess for the code word: ").strip()
        if answer.lower() == code_word.lower():
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer! You have {attempts} attempts left.")
                print("Additional clue:", clues[3 - attempts])  # Provide an additional clue
            else:
                print(f"Sorry, the correct code word was: {code_word}")
    return False


def treasure_room():
    """
    Main function for the treasure room challenge. Loads the game data, presents clues, and allows the player
    to guess the code word.
    """
    tv_game_data = load_tv_game_data('TRClues.json')

    if tv_game_data is None:
        return  # Exit if there was an error loading the data

    clues, code_word = select_random_clues(tv_game_data)
    present_clues(clues)

    if guess_code_word(clues, code_word):
        print("Congratulations! You've accessed the treasure room!")
    else:
        print("Better luck next time!")


# Test the function
treasure_room()