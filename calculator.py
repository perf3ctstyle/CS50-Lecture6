import cs50

if __name__ == '__main__':
    x = cs50.get_int("x: ")
    y = cs50.get_int("y: ")
    print(x + y)

    z = x / y
    print(f"{z:.50f}")
