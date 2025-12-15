if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

    min_score = min(scores)

    for i in range(0, len(scores)):
        if scores[i] == min_score:
            scores[i] = float('inf')

    min_score = min(scores)
    second_lowest = []

    for i in range(0, len(scores)):
        if scores[i] == min_score:
            second_lowest.append(names[i])

    second_lowest.sort()

    for i in range(0, len(second_lowest)):
        print(second_lowest[i])


