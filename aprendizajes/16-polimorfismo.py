class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice bee")

vaca1=Vaca("Carla")
oveja1=Oveja("Sandra")

animales =[vaca1, oveja1]

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)