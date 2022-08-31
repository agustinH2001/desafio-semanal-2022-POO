import string

def contador_palabras(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i not in palabras:
            palabras[i] = 1
        elif i in palabras:
            palabras[i] += 1
    palabras = dict(sorted(palabras.items()))
    for i, x in palabras.items():
        print(i, ":", x)

texto = "Para crear un programa y que la computadora lo interprete y ejecute, las instrucciones deben escribirse en un\
        lenguaje de programación. El lenguaje entendido por una computadora se conoce como código máquina. Consiste en \
        secuencias de instrucciones básicas que el procesador reconoce, codificadas como cadenas de números 1 y 0\
        (sistema binario). En los primeros tiempos de la computación se programaba directamente en código máquina.\
        Escribir programas así resultaba demasiado complicado, también era difícil entenderlos y mantenerlos una\
        vez escritos. Con el tiempo, se fueron desarrollando herramientas para facilitar el trabajo."
contador_palabras(texto)
