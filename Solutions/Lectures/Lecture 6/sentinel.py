"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

def main():
    end = False
    total = 0
    while not end:
        prompt = "Type a number: "
        # notice the type cast
        num = int(input(prompt))
        if num == -1:
            end = True
        else:
            total += num
    # we use %d in a string, followed by an module operator
    # in print() so that whatever after the operator could
    # replace the %d in the string
    print("Total is %d." % total)

if __name__ == '__main__':
    main()
