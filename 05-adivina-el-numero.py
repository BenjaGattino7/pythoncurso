from random import *

intentos=0
numero=randint(1,100)


nombre=input("ingrese su nombre: ")


while intentos<=7:
    numeroelegido=int (input("ingrese un numero: "))
    intentos+=1

    if numeroelegido == numero:
        print(f"Felicidades {nombre}! has ganado en {intentos} intentos")
        break
    elif numeroelegido< numero:
        print(f"El numero {numeroelegido} es menor al numero secreto. te quedan {8-intentos} intentos")
    elif numeroelegido > numero:
        print(f"El numero {numeroelegido} es mayor al numero secreto. te quedan {8 - intentos} intentos")

if numeroelegido != numero:
    print(f"Te has quedado sin intentos, el numero secreto era {numero}")
