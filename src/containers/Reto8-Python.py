def binario(num):
    lstNum = []
    while num != 0:
        lstNum.append(str(num%2))
        num = num//2
    num = "".join(lstNum)
    return num

print(binario(43))
