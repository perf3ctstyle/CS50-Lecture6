if __name__ == "__main__":
    people = {
        "Carter": "+375-29-333-55-11",
        "David": "+375-33-122-13-95"
    }

    name = input("Name: ")
    if name in people:
        number = people[name]
        print(f"Number: {number}")
