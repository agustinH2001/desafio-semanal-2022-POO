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
    veces = 0
    print(f"Primeros {cant} numeros primos:")
    while veces<cant:
        veces += 1
        if primo_check(veces):
            print(veces)
            

if primo_check(6):
    print("Es primo")
else:
    print("No es primo")

primos_print(5)
