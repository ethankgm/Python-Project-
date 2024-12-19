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

