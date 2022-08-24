# C = Cuadrado
# R = Rectangulo
# T = Triangulo

def area_poligono(tipo, altura, base):
    tipo = tipo.upper()
    if tipo == "R":
        return altura*base
    elif tipo == "T":
        return altura*base/2
    elif tipo == "C":
        return altura*altura

pol = "r"
h = 10
w = 20
print(area_poligono(pol, h, w))

pol = "t"
h = 10
w = 20
print(area_poligono(pol, h, w))

pol = "c"
h = 30
w = 30
print(area_poligono(pol, h, w))