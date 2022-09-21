from datetime import datetime

class Fechas:
    def checkFechas(self, input1, input2):
        formato = "%d/%m/%Y"
        try:
            fecha1 = datetime.strptime(input1, formato)
            valido1 = bool(fecha1)
        except ValueError:
            print(f"La fecha {input1} no está en el formato correcto")
            valido1 = False
        try:
            fecha2 = datetime.strptime(input2, formato)
            valido2 = bool(fecha2)
        except ValueError:
            print(f"La fecha {input2} no está en el formato correcto")
            valido2 = False
        if valido1 and valido2:
            delta = abs(fecha1 - fecha2)
            print(f"Hay {delta.days} días entre ambas fechas")
            

str1 = "15/06/2001"
str2 = "15/02/2015"
fecha = Fechas()
fecha.checkFechas(str1, str2)
