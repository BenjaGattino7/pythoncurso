"""def suma (*args):
    total =0

    for arg in args:
        total += arg
    return total


print(suma(5,6,7,8))"""

def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

resultado= numeros_persona("Carlos",10,20,30)
print(resultado)