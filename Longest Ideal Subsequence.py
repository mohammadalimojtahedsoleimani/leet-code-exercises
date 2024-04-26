def longest_ideal_string(s, k):
    dp = [0] * 27
    n = len(s)

    for i in range(n - 1, -1, -1):
        cc = s[i]
        idx = ord(cc) - ord('a')
        maxi = float('-inf')

        left = max((idx - k), 0)
        right = min((idx + k), 26)

        for j in range(left, right + 1):
            maxi = max(maxi, dp[j])

        dp[idx] = maxi + 1

    return max(dp)


print(longest_ideal_string("acfgbd", 2))
