if __name__ == "__main__":
    before = input("Input a string: ")
    print(f"After: ", end="")
    for c in before:
        print(c.upper(), end="")
    print()

    before = input("Input another string: ")
    after = before.upper()
    print(f"After: {after}")
