"""mi_archivo = open('../Prueba.txt', encoding='cp1252', errors='surrogateescape')


unalinea = mi_archivo.readline()
print(unalinea)

unalinea = mi_archivo.readline()
print(unalinea)"""


archivo = open('../Prueba1.txt', 'w')

#archivo.writelines(['Nuevo ', 'texto ','de ','prueba'])
lista = ['Nuevo ', 'texto ','de ','prueba ', 'hola ']

for p in lista:
        archivo.writelines(p + "\n")


archivo.close()
archivo = open('../Prueba1.txt', 'r')
print(archivo.read())
archivo.close()
archivo = open('../Prueba1.txt', 'a')

archivo.write('Bienvenido')