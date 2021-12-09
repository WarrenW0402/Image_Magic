# Advant of Code 2021 Day 1

with open("./data/Input Day1.txt") as f:
    depths = []
    numOfIncrese = 0

    for line in f:
        depths.append(int(line))

for i in range(len(depths)-1):
    if depths[i] < depths[i + 1]:
        numOfIncrese += 1

print(numOfIncrese)


