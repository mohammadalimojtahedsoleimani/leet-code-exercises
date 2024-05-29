def addBinary(a, b):
    int1 = int(a, 2)
    int2 = int(b, 2)
    int1 = bin(int1 + int2)
    return int1[2:]



print(addBinary('1010', '1011'))
