import cs50

if __name__ == '__main__':
    x = cs50.get_int("x: ")
    y = cs50.get_int("y: ")
    print(x + y)

    try:
        a = int(input("a: "))
        b = int(input("b: "))
    except ValueError:
        print("Not an int!")
        exit()
    print(a + b)
