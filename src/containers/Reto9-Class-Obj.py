#metodos: chequear expresion
class Expresion:
    def __init__(self, input):
        self.input = input

class Checker(Expresion):
    def __init__(self, input, inicios, finales):
        super().__init__(input)
        self.inicios = inicios
        self.finales = finales

    def getType(self):
        lista = []
        for i in self.input:
            if i in self.inicios:
                lista.append(i)
            elif i in self.finales:
                pos = self.finales.index(i)
                if (len(lista) > 0) and (self.inicios[pos] == lista[len(lista)-1]):
                    lista.pop()
        if len(lista) == 0:
            return("Equilibrada")
        else:
            return("NO equilibrada")    

inicio = ["[","{","("]
final = ["]","}",")"]
exp1 = Checker("(1[2)3]", inicio, final)
print(exp1.getType())
exp2 = Checker("{3+85*(15-6)}", inicio, final)
print(exp2.getType())
