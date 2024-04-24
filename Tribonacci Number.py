def tribonacci(n, memo={}):
    if n in memo: return memo[n]
    if n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0

    memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return memo[n]


print(tribonacci(25))
