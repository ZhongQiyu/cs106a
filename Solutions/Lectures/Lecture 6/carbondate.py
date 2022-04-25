import math

# The constant K in the half life formula
K = -8266.64258429376

def main():
    calculate_age_single_sample()

# helper of main() in this case
def calculate_age_single_sample():
    # Ask the user to enter the percent of c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    # Calculate the age: https://en.wikipedia.org/wiki/Radiocarbon_dating
    age = K * math.log(pct_left / 100)
    # Print the result: recall that age would always be positive,
    # so we need to multiply by (-1) before converting to string
    print("Sample is " + str((-1)*age) + " years old.")

if __name__ == '__main__':
    main()
