def main():
    prompt = "What's your favorite animal? "
    fav_animal = input(prompt)
    # we use %s as the same mechanism as we use %d
    # when printing the contents of a string.
    # %s needs to be replaced by a string (variable)
    # after the modulo operator.
    print("My favorite animal is also %s!" % fav_animal)

if __name__ == "__main__":
    main()
