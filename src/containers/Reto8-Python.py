def binario(num):
    lstNum = []
    while num != 0:
        lstNum.append(str(num%2))
        num = num//2
    num = "".join(lstNum)
    print(num)

binario(43)
