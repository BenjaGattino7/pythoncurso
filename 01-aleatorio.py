from random import *

#numero aleatorio en rango asignado sin decimales
aleatorio =randint(1,30)
print(aleatorio)

#numero aleatorio en rango asignado con decimales
aleatorio =round(uniform(1,10),2)
print(aleatorio)


#numero aleatorio entre 0 y 1
aleatorio =random()
print(aleatorio)

#random string
colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
print (aleatorio)

#mezclar numeros
numeros=list(range(5,51,5))
shuffle(numeros)
print(numeros)