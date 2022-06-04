import csv
import re

title = input("Title: ").strip().upper()
counter = 0

if __name__ == "__main__":
    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            current_title = row["title"].strip().upper()

            # easier to check equality with == so that's just solely for practice
            if re.search("^" + "(" + title + ")" + "$", current_title):
                counter += 1

    print(f"Number of people who like {title}: {counter}")
