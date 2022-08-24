# El programa necesita las librerias "pillow" y "requests" para python (las cuales no pude instalar en VS Code
# pero si en Pycharm, y el programa funciona perfectamente ahi al menos
# Use una segunda funcion para hallar el maximo comun divisor (mcd) y dividir ambas medidas por ese numero para sacar
# el aspect ratio

from PIL import Image
import requests
from io import BytesIO

def aspect_ratio(url):
    contenido = requests.get(url)
    img = Image.open(BytesIO(contenido.content))
    alto = img.width
    ancho = img.height
    print("La altura de la imagen es: ", alto)
    print("El ancho de la imagen es: ", ancho)
    div = (mcd(alto, ancho))
    print(f"El aspect ratio de la imagen es {int(alto/div)} x {int(ancho/div)}")

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

aspect_ratio("https://www.jhstoys.com/uploads/6/1/3/7/61377571/s737619424575262359_p1042_i943_w894.jpeg")


