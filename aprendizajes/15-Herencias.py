class animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")

    pass


class pajaro(animal):
    pass

mipajaro= pajaro(2, 'amarillo')

print(mipajaro.color)