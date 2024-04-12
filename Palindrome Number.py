x = str(10)
reversed_x = ''
for i in range(len(x) - 1, -1, -1):
    reversed_x += x[i]
if reversed_x == x:
    print(True)
else:
    print(False)

    # faster way:
