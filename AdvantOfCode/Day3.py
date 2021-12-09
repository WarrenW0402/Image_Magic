with open("../Data/Input Day3.txt") as f:
    zerocount = 0
    onecoount = 0
    mostCommon = 0
    leastCommon = 0
    list = []
    listOfValue = []
    listOfMostCommon = []
    listOfLeastCommon = []

    for i in f:
        listOfValue = i.strip()
        list.append(listOfValue)

    for i in range(len(listOfValue)):
        zerocount = 0
        onecoount = 0
        for j in range(len(list)):
            num = list[j][i]
            if num == '0':
                zerocount += 1
            elif num == '1':
                onecoount += 1

        if zerocount > onecoount:
            mostCommon = 0
            leastCommon = 1

        elif zerocount < onecoount:
            mostCommon = 1
            leastCommon = 0

        listOfMostCommon.append(mostCommon)
        listOfLeastCommon.append(leastCommon)

    numLC = 0
    numMC = 0
    for digit in listOfMostCommon:
        numMC = numMC * 2 + int(digit)

    for digit in listOfLeastCommon:
        numLC = numLC * 2 + int(digit)

    print(numLC * numMC)



