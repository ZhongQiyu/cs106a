"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    prompt = "Number to count to: "
    count_to = int(input(prompt))
    fizz_ct, buzz_ct, fizzbuzz_ct = 0, 0, 0
    for num_idx in range(count_to):
        num = num_idx + 1
        if num % 3 == 0:
            if num % 5 != 0:
                print("Fizz")
                fizz_ct += 1
            else:
                print("FizzBuzz")
                fizzbuzz_ct += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz_ct += 1
        else:
            print(num)
    print()
    print("Num fizzed: %d" % fizz_ct)
    print("Num buzzed: %d" % buzz_ct)
    print("Num fizzbuzzed: %d" % fizzbuzz_ct)
            
if __name__ == '__main__':
    main()
