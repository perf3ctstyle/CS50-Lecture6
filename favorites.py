import csv

titles = dict()


def get_value(title):
    return titles[title]


if __name__ == "__main__":
    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["title"].strip().upper()
            if title not in titles:
                titles[title] = 0
            titles[title] += 1
