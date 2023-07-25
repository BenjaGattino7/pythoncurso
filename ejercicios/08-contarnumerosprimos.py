def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def contar_primos(numero):
    cantidad_primos = 0

    for num in range(2, numero + 1):
        if es_primo(num):
            print(num)
            cantidad_primos += 1

    return cantidad_primos



num = 20
cantidad_primos_encontrados = contar_primos(num)
print(f"La cantidad de números primos hasta {num} es: {cantidad_primos_encontrados}")
