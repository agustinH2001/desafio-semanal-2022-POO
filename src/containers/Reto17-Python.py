class Carrera:
    def comprobar(self, atleta, pista):
        array1 = atleta.split()
        array2 = []
        sigue = True
        for i in pista:
            array2.append(i)
        for n, m in zip(array1, array2):
            if (n == "run" and m == "_") or (n == "jump" and m == "|"):
                sigue = True
            else:
                sigue = False
                break
        if sigue:
            print("El atleta completo la carrera")
        else:
            print("El atleta no logro completar la carrera")

atleta1 = "run run jump run jump run jump run jump run jump run jump run run run"
atleta2 = "run run jump run jump run run run jump run jump run jump run run run"
pista = "__|_|___|_|_|__"
test = Carrera()
test.comprobar(atleta1, pista)
test.comprobar(atleta2, pista)