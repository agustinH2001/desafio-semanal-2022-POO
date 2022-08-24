def primo_check(num):
    cont = 0
    for i in range(1,num):
        if num%i == 0 and cont<3:
            cont += 1
    if cont<2:
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")

def primos(cant):
    veces = 1
    print(f"Primeros {cant} numeros primos:")
    while veces<cant:
        cont = 0
        for i in range(1,cant):
            if veces%i == 0:
                cont += 1
        if cont<2:
            print(veces)
            veces += 1

primo_check(73)
primos(7)