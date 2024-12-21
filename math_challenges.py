from random import randint

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

def solve_linear_equation():
        # It generates two random values for a and b between 1 and 10
        a = randint(1, 10)
        b = randint(1, 10)

        # We show them the equation
        print(f"Math Challenge: Solve the linear equation {a}x + {b} = 0.")

        try:
            # Ask the player for their answer
            player_answer = float(input("Your answer (value of x): "))

            correct_answer = -b / a

            # Is the answer correct ?
            if player_answer == correct_answer:
                print("Correct! You win a key.")
                return a, b, correct_answer
            else:
                print("No, the correct answer is: ", correct_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False