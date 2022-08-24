from re import I


def primo_check(num):
    cont = 0
    for i in range(1,num):
        if num%i == 0 and cont<3:
            cont += 1
    if cont<2:
        return True
    else:
        return False

def primos_print(cant):
    numprimos = []
    cont = 0
    print(f"Primeros {cant} numeros primos:", end=" ")
    while len(numprimos)!=cant:
        cont += 1
        if primo_check(cont):
            numprimos.append(cont)
    print(numprimos)
            

if primo_check(4):
    print("Es primo")
else:
    print("No es primo")

primos_print(10)
