from cs50 import get_int

if __name__ == '__main__':
    points = get_int("How many points did you lose: ")
    if points < 2:
        print("You lost fewer points than me")
    elif points > 2:
        print("You lost more points than me")
    else:
        print("You lost the same number of points as me")

    if points % 2 == 0:
        print("Number of points is even")
    else:
        print("Number of points is odd")