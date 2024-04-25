def longestCommonPrefix(strs):
    shortest = min(strs, key=len)
    for i, c in enumerate(shortest):
        for other in strs:
            if c != other[i]:
                return shortest[:i]
    return shortest


print(longestCommonPrefix(["flower", "flow", "flight"]))
