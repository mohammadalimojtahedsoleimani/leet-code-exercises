def reversePrefix(word, ch):
    temp = ""
    flag = False
    for i in range(len(word)):
        if word[i] == ch:
            temp += word[i::-1] + word[i::]
            flag = True
            break
    if not flag:
        return word
    return temp


print(reversePrefix("abcdef", 'z'))
