with open("../Data/Input Day3 p2.txt") as f:

    zerocount = 0
    onecoount = 0
    mostCommon = 0
    leastCommon = 0
    list = []
    listOfValue = []
    listOfMostCommon = []
    listOfLeastCommon = []

    for i in f:
        listOfValue = i.strip()  # single list
        list.append(listOfValue) # list of single lists

    def oxygenFunc():
        i = 0
        global list
        while i < len(listOfValue):
            # while there are more than 1 elements in id_list
            count = [0, 0]
            for idx in list:
                count[int(idx[i])] += 1

            new_id_list = []
            if count[1] >= count[0]:

                # drop all elements with 0 at ith position

                for idx in list:
                    if idx[i] == 1:
                        new_id_list.append(idx)

            else:
                # drop all elements with 1 at ith position
                for idx in list:
                    if idx[i] == 0:
                        new_id_list.append(idx)

                # remaining id list
            list = new_id_list
            i += 1

        return list

    # def co2Func(listOfValue):
    #     i = 0
    #     while i < len(listOfValue[0]) and len(list) > 1:
    #         # while there are more than 1 elemnts in id_list
    #         count = [0, 0]
    #         for idx in list:
    #             count[idx[i]] += 1
    #
    #             new_id_list = []
    #         if onecoount <= zerocount:
    #
    #             # drop all elements with 0 at ith position
    #
    #             for idx in list:
    #                 if idx[i] == 1:
    #                     new_id_list.append(idx)
    #
    #         else:
    #             # drop all elements with 1 at ith position
    #             for idx in list:
    #                 if idx[i] == 0:
    #                     new_id_list.append(idx)
    #
    #         # remaining id list
    #         list = new_id_list
    #         i += 1
    #
    #     return int(list[0])


oxygenFunc()


for digit in listOfMostCommon:
    numMC = numMC * 2 + int(digit)

for digit in listOfLeastCommon:
    numLC = numLC * 2 + int(digit)




