from cs50 import get_string

if __name__ == '__main__':
    print("hello, world")

    answer = get_string("What's your name? ")
    print("hello, " + answer)
    print(f"hello, {answer}")

    answer = input("What's your name? ")
    print(f"hello, {answer}")
