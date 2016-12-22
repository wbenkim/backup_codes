def manipulate_data(data):
    sumNegatives = 0
    countPositives = 0

    if type(data) is list:
        for x in data:
            if x < 0:
                sumNegatives = sumNegatives + x
            else:
                countPositives = countPositives + 1

        answer = [countPositives, sumNegatives]
        return answer
    else:
        return "Only lists allowed"

print manipulate_data([1, -9, 2, 3, 4, -5])
