def findRelativeRanks(score: list) -> list:
    temp = sorted(score, reverse=True)
    for i in range(len(score)):
        if score[i] == temp[0]:
            score[i] = 'Gold Medal'
        elif score[i] == temp[1]:
            score[i] = 'Silver Medal'
        elif score[i] == temp[2]:
            score[i] = 'Bronze Medal'
        else:
            score[i] = str(temp.index(score[i]) + 1)
    return score


print(findRelativeRanks([10, 3, 8, 9, 4]))
