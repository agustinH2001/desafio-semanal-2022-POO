class Recursivo:
    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)

obj1 = Recursivo()
print(obj1.factorial(10))
