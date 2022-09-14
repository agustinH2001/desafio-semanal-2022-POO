class Texto:
    def __init__(self, input):
        self.input = input
    
    def check_palindrome(self):
        array1 = []
        array2 = []
        for i in self.input:
            if i.isalnum():
                array1.insert(0, i.lower())
                array2.append(i.lower())
            return True
        else:
            return False

texto1 = "¿Son robos o sobornos?"
obj1 = Texto(texto1)
print(obj1.check_palindrome())
