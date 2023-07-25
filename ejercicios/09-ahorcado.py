import random


palabras = ["python", "programacion", "inteligencia", "computadora", "teclado", "raton", "pantalla", "monitor"]


def obtener_palabra_al_azar():
    return random.choice(palabras)


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero


def adivinar_letra():
    while True:
        letra = input("Adivina una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Por favor, ingresa una única letra válida.")


def jugar():
    palabra_secreta = obtener_palabra_al_azar()
    letras_adivinadas = set()
    intentos_maximos = 6

    print("¡Bienvenido al juego del ahorcado!")

    while True:
        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(tablero)

        if tablero.replace(" ", "") == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        if len(letras_adivinadas) >= intentos_maximos:
            print("¡Lo siento! Te has quedado sin intentos. La palabra era:", palabra_secreta)
            break

        letra = adivinar_letra()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra antes. Intenta con otra.")
        elif letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Adivinaste una letra!")
        else:
            letras_adivinadas.add(letra)
            print("La letra no está en la palabra. Pierdes un intento.")


if __name__ == "__main__":
    jugar()
