from random import randint

def factorial(n):
    if n < 0:
        raise ValueError("The factorial is not defined for the negative numbers")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#def math_challenge_factorial(n):
#nn  = randit(1, 10)
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

from random import randint


def solve_linear_equation():
    # Generate random values for a and b
    a = randint(1, 10)
    b = randint(1, 10)

    # Calculate the correct solution
    x_correct = -b / a

    # Return the values and solution
    return a, b, x_correct


def math_challenge_equation():
    # Generate the equation and solution
    a, b, x_correct = solve_linear_equation()

    # Display the equation
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")

    try:
        # Ask the player for their answer
        x_player = float(input("What is the value of x: "))

        # Is its answer correct ?
        if x_player == x_correct:
            print("Correct! You win a key.")
            return True
        else:
            print(f"No, the correct answer is: {x_correct}")
            return False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

from random import randint

def is_prime(n):
    if n <= 1:
        return False

    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            return False
    return True

def nearest_prime(n):
    prime_found = False
    while not prime_found:
        if is_prime(n):
            prime_found = True
        else:
            n = n + 1
    return n

# Prime Number Math Challenge
def math_challenge_prime():
    # Random number between 10 and 20
    n = randint(10, 20)
    print(f"Math Challenge: What is the nearest prime number greater than or equal to {n}?")

    # Correct solution using nearest_prime
    correct_answer = nearest_prime(n)

    try:
        # Player's answer
        player_answer = int(input("Your answer: "))

        # Validate answer
        if player_answer == correct_answer:
            print("Correct! You win a key.")
            return True
        else:
            print(f"No, the correct answer is: {correct_answer}")
            return False
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False