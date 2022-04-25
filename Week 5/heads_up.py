import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'  # the files are locally stored
NEW_LINE = '\n'  # this may be different when you run on your machine

def main():
    # load the file
    file_data = open(FILE_NAME)
    # EXTENSION HERE: STATISTICS
    # parse into a list of items
    cs_words = [word.strip(NEW_LINE) for word in file_data]
    # loop controller
    end = False
    while not end:
        # prompt the user to run the game
        prompt = input("Press enter to continue, and input anything to stop: ")
        if len(prompt) != 0:
            end = True
            print("GAME ENDS")
        else:
            # choose an element randomly from the word list
            chosen_value = random.choice(cs_words) # comes with ‘import random’
            print(chosen_value)

if __name__ == '__main__':
    main()
