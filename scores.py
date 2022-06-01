if __name__ == "__main__":
    scores = []
    for i in range(3):
        score = int(input("Input a score: "))
        # scores.append(score)
        scores = scores + [score]

    average = sum(scores) / len(scores)
    print(f"Average: {average}")