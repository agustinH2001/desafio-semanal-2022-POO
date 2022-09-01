from re import S
import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

#se crean 2 clases para almacenar valores, se usa NamedTuple en vez de dict porque es mas eficiente para almacenar solo valores
#ej dict1 = {"key1": "str1", "key2": "str2"} /// namedtuple1 = Nombre1("str1", "str2")
#tuple es un conjunto ordenado de valores
# _abc indica que un atributo o metodo solo se usa internamente en esa clase (solo para mejor claridad)
# __abc el interprete lo lee como _classname__abc para asegurarse q el nombre no choque con otro similar
class Jugador(NamedTuple):
    label: str
    color: str

class Movimiento(NamedTuple):
    fila: int
    col: int
    label: str = ""

TAMAÑO_TABLERO = 3
JUGADORES = (Jugador(label="X", color="red"), Jugador(label="O", color="yellow"))

class TaTeTiJuego:
    #se usa cycle en jugadores para ponerles un iterador que se puede utilizar mas adelante
    def __init__(self, jugadores=JUGADORES, size=TAMAÑO_TABLERO):
        self._jugadores = cycle(jugadores)
        self.tamaño = size
        self.jugador_actual = next(self._jugadores)
        self.combo_ganador = []
        self._mov_actuales = []
        self._hay_ganador = False
        self._combos_ganadores = []
        self._config_tablero()
    
    #_mov_actuales crea una lista de listas con objetos Movimiento vacio (que contienen "")
    def _config_tablero(self):
        self._mov_actuales = [[Movimiento(fila, col) for col in range(self.tamaño)] for fila in range(self.tamaño)]
        self._combos_ganadores = self._ver_combos_ganadores()
    
    #zip combina los elementos de una lista con el correspondiente en otra
    #enumerate() es una forma mas facil que for de enumerar los elementos de una lista
    def _ver_combos_ganadores(self):
        filas = [[(movimiento.fila, movimiento.col) for movimiento in fila] for fila in self._mov_actuales]
        columnas = [list(col) for col in zip(*filas)]
        primer_diagonal = [fila[i] for i, fila in enumerate(filas)]
        segunda_diagonal = [col[j] for j, col in enumerate(reversed(columnas))]
        return filas + columnas + [primer_diagonal, segunda_diagonal]
    
    #un movimiento es valido si aun no hay un ganador y si aun no se ha jugado ese movimiento
    #fila, col saca las coordenadas .fila y .col de la entrada Movimiento
    #no_jugado checkea si es que las coordenadas actuales aun tienen "" como string (sin movimientos registrados)
    def movimiento_valido(self, Movimiento):
        fila, col = Movimiento.fila, Movimiento.col
        no_jugado = self._mov_actuales[fila][col].label == ""
        sin_ganador = not self._hay_ganador
        return sin_ganador and no_jugado
    
    #cada celda en el tablero tiene un objeto Movimiento asociada
    #cada Movimiento tiene un atributo .label (string) que identifica el jugador q hizo esa jugada
    #se usan sets ya que no admiten varias instancias del mismo valor, por lo q al meterle el .label de un jugador X tres veces (XXX), resultara en un solo set(X)
    def revisar_movimiento(self, movimiento):
        fila, col = movimiento.fila, movimiento.col
        self._mov_actuales[fila][col] = movimiento
        for combo in self._combos_ganadores:
            resultados = set(self._mov_actuales[x][y].label for x, y in combo)
            victoria = (len(resultados)==1 and ("" not in resultados))
            if victoria:
                self._hay_ganador = True
                self.combo_ganador = True
                break

    def hay_ganador(self):
        return self._hay_ganador
    
    #jugadas crea una lista con el contenido de los .label de los movimientos actuales
    #all() retorna True si todos los items de la lista son verdaderos o si estan vacios, caso contrario retorna False
    def empate(self):
        sin_ganador = not self._hay_ganador
        jugadas = (movimiento.label for fila in self._mov_actuales for movimiento in fila)
        return sin_ganador and all(jugadas)
    
    #_jugadores contiene un iterador que va ciclando por ambos jugadores, por lo que se puede usar next() para pasar al siguiente cuando se necesite
    def cambiar_jugador(self):
        self.jugador_actual = next(self._jugadores)

#super() hace que nuestra nueva clase herede lo que pusimos como parametro
#self. bindea el atributo con los parametros dados // permite acceder a los atributos y metodos de una clase
#fill=tk.X es para cuando se cambia el tamaño de la ventana que el frame vaya llenando
class TaTeTiTablero(tk.Tk):
    def __init__(self, juego):
        super().__init__()
        self.title("Juego Ta Te Ti")
        self._celdas = {}
        self._juego = juego
        self._crear_display()
        self._crear_grilla_tablero()
    
    def _crear_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.config(background="black")
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Listos?",
            font=font.Font(size=28, weight="bold"),
            bg="black",
            fg="white"
        )
        self.display.pack()
    
    def _crear_grilla_tablero(self):
        grilla_frame = tk.Frame(master=self)
        grilla_frame.pack()
        for fila in range(self._juego.tamaño):
            self.rowconfigure(fila, weight=1, minsize=50)
            self.columnconfigure(fila, weight=1, minsize=75)
            for col in range(self._juego.tamaño):
                boton = tk.Button(
                    master=grilla_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=1,
                    highlightbackground="blue"
                )
                self._celdas[boton] = (fila,col)
                boton.grid(row=fila, column=col, padx=5, pady=5, sticky="nsew")
                #aca se bindea el presionar un boton con el comando jugar, bind bindea un evento (click) a un widget (boton)
                boton.bind("<ButtonPress-1>", self.jugar)

    #click seria un evento de tkinter (objeto)
    #boton_presionado es el widget o boton q causo este evento
    #se crea un nuevo movimiento con el .label del jugador actual
    def jugar(self, click):
        boton_presionado = click.widget
        fila, col = self._celdas[boton_presionado]
        movimiento = Movimiento(fila, col, self._juego.jugador_actual.label)
        if self._juego.movimiento_valido(movimiento):
            self._actualizar_boton(boton_presionado)
            self._juego.revisar_movimiento(movimiento)
            if self._juego.empate():
                self._actualizar_display(msg="EMPATE!", color="red")
            elif self._juego.hay_ganador():
                msg = f"Ha ganado el jugador {self._juego.jugador_actual.label}!"
                color = self._juego.jugador_actual.color
                self._actualizar_display(msg, color)
            else:
                self._juego.cambiar_jugador()
                msg = f"Es el turno de {self._juego.jugador_actual.label}"
                self._actualizar_display(msg)

    def _actualizar_boton(self, boton_presionado):
        boton_presionado.config(text=self._juego.jugador_actual.label)
        boton_presionado.config(fg=self._juego.jugador_actual.color)

    #(((revisar funcionamiento)))
    def _actualizar_display(self, msg, color="white"):
        self.display.config(text=msg)
        self.display.config(fg=color)
    
def main():
    juego = TaTeTiJuego()
    tablero = TaTeTiTablero(juego)
    tablero.mainloop()
    
main()