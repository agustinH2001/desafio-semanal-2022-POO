import re

class Texto:
    def __init__(self, input):
        self.input = str(input).upper()
        self.morse = 0
    
    def checkMorse(self):
        for i in self.input:
            if i != "." and i != "-" and i != " ":
                self.morse += 1
        if self.morse == 0:
            return True
        else:
            return False

    def traducir(self):
        input_mod = self.input + " "
        output = ""
        citext = ""
        morse = self.checkMorse()
        codigo_morse = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        if morse:
            for x in input_mod:
                if (x != " "):
                    i = 0
                    citext += x
                else:
                    i += 1
                    if i == 2 :
                        output += " "
                    else:
                        output += list(codigo_morse.keys())[list(codigo_morse.values()).index(citext)]
                        citext = ""
        elif not morse:
            for i in input_mod:
                if i != " ":
                    output += codigo_morse[i] + " "
                else:
                    output += " "
        return output


texto1 = Texto("-... ..- . -. .- ...  - .- .-. -.. . ...")
print(f"Texto: {texto1.input}")
print(texto1.checkMorse())
print(texto1.traducir())

print("")

texto2 = Texto("Buenas noches")
print(f"Texto: {texto2.input}")
print(texto2.checkMorse())
print(texto2.traducir())
            