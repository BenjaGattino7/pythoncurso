
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado


def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("la lista se autodestruira")
        return []

    else:
        print("La lista se ha salvado")
        return lista_numeros

lista_numeros = [1, 2, 3, 4, 5]

resultado_moneda=lanzar_moneda()
resultante=probar_suerte(resultado_moneda,lista_numeros)
print("Resultado del lanzamiento de la moneda:", resultado_moneda)
print("Lista resultante:", resultante)