"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # store the user input's prompt as a variable
    prompt = "Please enter your weight on Earth: "
    # let the user input zer weight
    w_earth = input(prompt)
    # convert an Earth's weight to a Mars one
    w_mars = float(w_earth) * 0.378
    # print the converted weight:
    # use %.2f to preserve two digits
    # after the decimal point
    print("Your weight on Mars would be: %.2f" % (w_mars))

if __name__ == "__main__":
    main()
