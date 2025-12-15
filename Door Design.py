height, weight = map(int, input().split())

design = ".|."
lines = []
for i in range(0, height - 1, 2):
    line = ""
    line += (design * (1 + i)).center(weight, "-")
    lines.append(line)

center = "WELCOME".center(weight, "-")

for line in lines:
    print(line)
print(center)
lines.reverse()
for line in lines:
    print(line)

