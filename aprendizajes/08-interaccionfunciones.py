from random import *

palitos =['-','--','---','----']

def mezclar(lista):
    shuffle(lista)
    return lista

print(mezclar(palitos))

def probar_suerte():
    intento=''

    while intento not in ['1','2','3','4']:
        intento=input("Elige un numero del uno al cuatro: ")

    return int(intento)



def checkintento(lista,intento):
    if lista[intento - 1]=='-':
        print("Te toco el palito mas corto, has perdido")
    else:
        print("te has salvado")
    print(f"te ha tocado {lista[intento-1]}")

palitosmezclados =mezclar(palitos)
eleccion=probar_suerte()
checkintento(palitosmezclados, eleccion)