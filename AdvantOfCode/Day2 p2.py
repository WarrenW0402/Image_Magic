with open("../Data/Input Day2 p2.txt") as f:
    list = []
    depth = 0
    horiDis = 0
    aim = 0

    for i in f:
        list.append(i.strip()) # ["forward", 0]

    for i in range(len(list)):
        string = int(list[i][-1])

        if "forward" in list[i]:
            horiDis += string
            depth += aim * string
        elif "up" in list[i]:
            aim -= string
        elif "down" in list[i]:
            aim += string

    print(horiDis * depth)