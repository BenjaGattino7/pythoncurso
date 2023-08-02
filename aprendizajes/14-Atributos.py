class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print(f"pio, mi color es {format(self.color)}")

    @staticmethod
    def volar(metros):
        print(f"el pajaro ha volado {metros} metros")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")

Pajaro.poner_huevos(3)
mi_pajaro = Pajaro('Rojo', 'Hornero')

mi_pajaro.volar(50)
mi_pajaro.piar()