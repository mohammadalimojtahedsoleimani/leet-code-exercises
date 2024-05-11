def maximumHappinessSum(happiness: list, k: int):
    temp = 0
    i = 0
    happiness = sorted(happiness, reverse=True)
    while k > 0:
        happiness[i] = max(happiness[i] - i, 0)
        temp += happiness[i]
        i += 1
        k -= 1
    return temp


print(maximumHappinessSum([1, 1, 1, 1], 2))
