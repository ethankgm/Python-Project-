from random import randint
from math import factorial as math_factorial

def factorial(n):
    if n < 0:
        raise ValueError("The factorial is not defined for the negative numbers")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def math_challenge_factorial():
    n = randint(1, 10)
    print(f"Math Challenge: Calculate the factorial of {n}.")

    try:
        n_player=int(input("Your answer: "))
        if n_player == factorial(n):
            print("Correct! You win a key.")
        else:
            print("No, the correct answer is:", factorial(n) )
    except ValueError:
        print("Invalid input. Please enter a valid number")
        return False

math_challenge_factorial()

import random

def solve_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    solution = -b / a
    return a, b, solution

def math_challenge_equation():
    a, b, solution = solve_linear_equation()
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")
    user_answer = float(input("What is the value of x: "))

    if user_answer == solution:
        print("Correct! You win a key.")
        return True
    else:
        print(f"Incorrect! The correct answer is {solution}.")
        return False

math_challenge_equation()

from random import randint

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n

from random import randint

def math_challenge_prime():
    n = randint(10, 20)
    print(f"Math Challenge: What is the nearest prime number greater than or equal to {n}?")

    correct_answer = nearest_prime(n)

    try:
        player_answer = int(input("Your answer: "))

        if player_answer == correct_answer:
            print("Correct! You win a key.")
            return True
        else:
            print(f"No, the correct answer is: {correct_answer}")
            return False
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

math_challenge_prime()

import random

def challenge_one():
    # Example challenge logic
    return True

def challenge_two():
    # Example challenge logic
    return False

def challenge_three():
    # Example challenge logic
    return True

def math_challenge():
    challenges = [challenge_one, challenge_two, challenge_three]
    challenge = random.choice(challenges)
    return challenge()