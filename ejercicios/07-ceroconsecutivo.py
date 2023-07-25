def cerorepetido(*args):
    contadorcero= 0
    for n in args:
        if n == 0:
            contadorcero+=1
            if contadorcero == 2:
                return True
        else:
            contadorcero = 0

    return False
resultado1 = cerorepetido(5,3,0,0,5,7,8)
resultado2 =cerorepetido(5,3,4,5,6,2)
print(resultado1)
print(resultado2)


