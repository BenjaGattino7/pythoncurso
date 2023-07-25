def palabrasinrepetir (palabra):
    letrasunicas =sorted(set(palabra))
    return letrasunicas

resultado = palabrasinrepetir(input("ingrese una palabra "))
print(resultado)