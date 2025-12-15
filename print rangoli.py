import string

def print_rangoli(N):
    letters = string.ascii_lowercase[:N]
    width = 4 * N - 3

    rows = []
    for i in range(N):
        left = [letters[N-1 -k] for k in range(i + 1)]
        right = left[:-1][::-1]
        row = "-".join(left + right)
        rows.append(row.center(width, "-"))

    for r in rows:
        print(r)
    for r in rows[-2 :: -1]:
        print(r)


if __name__ == '__main__':
    n = int(input().strip())
    print_rangoli(n)