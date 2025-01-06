from random import randint
from math import factorial as math_factorial


def math_challenge_factorial():
    n = randint(1, 10)
    print(f"Math Challenge: Calculate the factorial of {n}.")

    try:
        n_player = int(input("Your answer: "))
        if n_player == math_factorial(n):
            print("Correct! You win a key.")
        else:
            print(f"No, the correct answer is: {math_factorial(n)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False


def solve_linear_equation():
    a = randint(1, 10)
    b = randint(1, 10)
    solution = -b / a
    return a, b, solution


def math_challenge_equation():
    a, b, solution = solve_linear_equation()
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")

    try:
        user_answer = float(input("What is the value of x: "))
        if user_answer == solution:
            print("Correct! You win a key.")
            return True
        else:
            print(f"Incorrect! The correct answer is {solution}.")
            return False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n


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

def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_equation, math_challenge_prime]
    challenge = randint(0, 2)  # Randomly choose a challenge index
    challenges[challenge]()  # Execute the chosen challenge

math_challenge()