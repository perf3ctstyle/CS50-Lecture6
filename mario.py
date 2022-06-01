def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print("That's not an integer!")
    return n


def print_horizontal(number):
    print("#" * number)


def print_horizontal_and_vertical(number):
    for i in range(number):
        print("#" * number)


def print_recursively(number):
    if number <= 0:
        return
    print_recursively(number-1)
    print("#" * number)


if __name__ == "__main__":
    height = get_height()
    print_horizontal(height)
    print()
    print_horizontal_and_vertical(height)
    print()
    print_recursively(height)
