def reducir_lista(lista):
    listasinduplicados = list(set(lista))

    listasinduplicados.remove(max(listasinduplicados))
    return listasinduplicados
def promedio(lista):
    suma=sum(lista)
    cantidadelementos=len(lista)
    return suma / cantidadelementos

lista_numeros=[1,2,15,7,2]
listareducida=reducir_lista(lista_numeros)
resultadopromedio=promedio(listareducida)

print(listareducida)
print(resultadopromedio)