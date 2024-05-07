def lengthOfLastWord(s):
    temp = ''
    flag = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            temp += s[i]
        elif s[-1] == ' ' and len(temp) == 0:
            continue
        else:
            break
    return len(temp)


print(lengthOfLastWord("   fly me   to   the moon  "))
