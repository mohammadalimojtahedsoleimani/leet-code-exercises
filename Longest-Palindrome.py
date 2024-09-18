

def longestPalindrome(s):
    if len(s) == 1:
        return 1
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    lengh = 0
    odd_found = False
    for count in char_count.values():
        if count % 2 == 0:
            lengh += count
        else:
            lengh += count - 1
            odd_found = True
    if odd_found:
        lengh += 1
    return lengh
