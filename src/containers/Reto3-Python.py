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
    

primo_check(73)