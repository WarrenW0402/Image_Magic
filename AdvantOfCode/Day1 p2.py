with open("../Data/Input Day1 p2.txt") as f:
    depths = []
    numOfIncrese = 0

    for line in f:
        depths.append(int(line))

for i in range(len(depths)-3):
    num1 = depths[i] + depths[i + 1] + depths[i + 2]
    num2 = depths[i + 1] + depths[i + 2] + depths[i + 3]
    if  num1 < num2:
        numOfIncrese += 1

print(numOfIncrese)