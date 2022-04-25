"""
Generates a random number between 1 and 99.
Has the user keep guessing until they figure out 
what the number is. Tells the user after each guess
if their guess was too high or too low.
"""

# this is the module of random
import random

def main():
    # random.randint(a,b) generates a random
    # number between a and b, inclusively
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        # True if guess is less than secret number
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print("") # an empty line
        guess = int(input("Enter a new guess: "))
    print("Congrats! The number was: " + str(secret_number))

# there is a way to use only one time of
# guess = int(input("Enter a new guess: ")).
# do you know what it is?

if __name__ == '__main__':
    main()
