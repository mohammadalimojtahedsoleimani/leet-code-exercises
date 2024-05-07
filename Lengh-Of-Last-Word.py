def lengthOfLastWord(s):
    temp = s.split()
    return len(temp[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))
