from random import *



def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    return dado1,dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

    return mensaje

dado1, dado2 = lanzar_dados()


resultado_evaluacion = evaluar_jugada(dado1, dado2)


print(resultado_evaluacion)