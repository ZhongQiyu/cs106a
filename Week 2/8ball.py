"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

# import the module random
import random

def main():
    # the database of answers
    ANS_DB = ["As I see it, yes.", "Ask again later.",
    "Better not to tell you now.", "Cannot predict now.",
    "Concentrate and ask again.", "Don't count on it.",
    "It is certain.", "It is decidedly so.", "Most likely.",
    "My reply is no.", "My sources say no.", "Outlook not so good.",
    "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
    "Very doubtful.", "Without a doubt.", "Yes.", "Yes - definitely.",
    "You may rely on it."]
    CHOICE_COUNT = 8
    # random.sample(range(a), b) non-repeatedly choose b numbers
    # from range 0 to a - 1
    # in this case, we randomly choose 8 answers out of the database
    # as the ones 8-ball will respond with
    ans_indice = random.sample(range(len(ANS_DB)), CHOICE_COUNT)
    # Milestone 1
    INPUT_PROMPT = "Ask a yes or no question: "
    user_question = input(INPUT_PROMPT)
    ans_choice = ANS_DB[random.choice(ans_indice)]
    print(ans_choice)
    print("Milestone 1 achieved.")
    # Milestone 2
    end = False
    while not end:
        user_question = input(INPUT_PROMPT)
        if len(user_question) == 0:
            end = True
            print("Milestone 2 achieved.")
        else:
            ans_choice = ANS_DB[random.choice(ans_indice)]
            print(ans_choice)

if __name__ == "__main__":
    main()
