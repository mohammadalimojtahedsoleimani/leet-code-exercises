def isValid(s):
    stack = []
    flag = True
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack and stack[-1] == '{':
            stack.pop()
        else:
            flag = False
    if stack:
        flag = False
    return flag


print(isValid('()'))
