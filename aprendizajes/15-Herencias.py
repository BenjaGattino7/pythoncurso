class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("jajaja")

class Hijo(Padre,Madre):
    pass


class Nieto(Hijo):
    pass

miNieto= Nieto()
miNieto.hablar()