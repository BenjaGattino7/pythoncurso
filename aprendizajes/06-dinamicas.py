"""def chequearcifras(numero):

    return numero in range(100,1000)

resultado = chequearcifras(100)
print(resultado)"""

def chequearcifras(lista):
    lista3cifras =[]
    for n in lista:
        if n in range(100,1000):
            lista3cifras.append((n))
        else:
            pass
    return lista3cifras
resultado = chequearcifras([55,100,320])
print(resultado)

