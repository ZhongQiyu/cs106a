def main():
    x = 1
    plus_five(x)
    print(x)
    # the output is still 1 because the argument x in
    # plus_five() is a temporary variable: when the
    # function ends, the value of x will lose if it is
    # not returned

def plus_five(x):
    x += 5

if __name__ == '__main__':
    main()
