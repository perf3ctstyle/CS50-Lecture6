def uppercase_char_by_char(string):
    i = 0
    new_string = ""
    for c in string:
        c = c.upper()
        new_string += c
        i += 1
    return new_string


def print_string_from(string, index):
    for c in string[index:]:
        print(c, end="")
    print()


def print_string_until(string, slice_off_end):
    for c in string[:-slice_off_end]:
        print(c, end="")
    print()


if __name__ == "__main__":
    before = input("Input a string: ")
    after = uppercase_char_by_char(before)
    print(f"After: {after}")

    before = input("Input another string: ")
    after = before.upper()
    print(f"After: {after}")

    print_string_from(after, 2)
    print_string_until(after, 1)
