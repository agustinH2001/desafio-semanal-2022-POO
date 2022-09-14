class Armstrong:
    def check(self, n1):
        n1 = str(n1)
        n2 = 0
        for i in n1:
            n2 += int(i)**len(n1)
        if int(n1) == n2:
            return True
        else:
            return False

obj1 = Armstrong()
print(obj1.check(153))
print(obj1.check(123))