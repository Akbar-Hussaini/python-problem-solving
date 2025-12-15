num_of_words = int(input())
words = []
for _ in range(num_of_words):
    words.append(input())
for word in words:
    if len(word) <= 10:
        print(word)
    elif len(word) > 10:
        first_char = word[0]
        last_char = word[-1]
        number = len(word) - 2
        print(f"{first_char}{number}{last_char}")