def validar_exp(exp):
    inicios = ["[","{","("]
    finales = ["]","}",")"]
    lista = []
    for i in exp:
        if i in inicios:
            lista.append(i)
        elif i in finales:
            pos = finales.index(i)
            if (len(lista) > 0) and (inicios[pos] == lista[len(lista)-1]):
                lista.pop()
    if len(lista) == 0:
        print("Expresion equilibrada")
    else:
        print("Expresion NO equilibrada")

expresion1 = "(1[2)3]"
expresion2 = "{3+85*(15-6)}"
validar_exp(expresion1)
validar_exp(expresion2)