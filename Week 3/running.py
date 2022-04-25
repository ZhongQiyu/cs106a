"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    end = False
    total = 0
    while not end:
        prompt = "Enter a value: "
        user_val = int(input(prompt))
        if user_val == 0:
            end = True
        else:
            total += user_val
            print("Running total is %d" % total)
            print("--------------------")

if __name__ == '__main__':
    main()
