class Mayusculas:
    def convertir(self, input):
        texto = input.split()
        for i in texto:
            texto[texto.index(i)] = i.title()
        texto = " ".join(texto)
        print(texto)

str1 = "muy buenas tardes, como les va"
text = Mayusculas()
text.convertir(str1)