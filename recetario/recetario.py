
from pathlib import  Path
from os import system
import os



mi_ruta= Path("/home/ingenierira/Escritorio/cursoPython/curso/recetario/Recetas")

def contarRecetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():

    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contarRecetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)


def mostrarCategorias(ruta):
    print("Categorias:")
    rutaCategorias = Path(ruta)
    listaCategorias = []
    contador = 1
    for carpeta in rutaCategorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        listaCategorias.append(carpeta)
        contador += 1
    return listaCategorias

def elegirCategoria(lista):
    eleccionCorrecta ='x'

    while not eleccionCorrecta.isnumeric() or int(eleccionCorrecta) not in range (1, len(lista)+1):
        eleccionCorrecta = input("\n Elige una categoria: ")
    return lista[int(eleccionCorrecta)-1]

def mostrarRecetas (ruta):
    print("Recetas: ")
    rutaRecetas = Path(ruta)
    listaRecetas =[]
    contador = 1

    for receta in rutaRecetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] -{receta_str}")
        listaRecetas.append(receta)
        contador += 1
    return listaRecetas

def elegirRecetas(lista):
    eleccionReceta ='x'

    while not eleccionReceta.isnumeric() or int(eleccionReceta) not in range(1, len(lista) + 1):
        eleccionReceta= input("\n Elige una receta")
        return lista[int(eleccionReceta)-1]

def leerReceta(receta):
    print(Path.read_text(receta))


def crearReceta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombreReceta= input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenidoReceta = input()
        rutaNueva = Path(ruta, nombreReceta)

        if not os.path.exists(rutaNueva):
            Path.write_text(rutaNueva, contenidoReceta)
            print(f"Tu receta {nombreReceta} ha sido creada")
            existe= True
        else:
            print("Esa receta ya existe")
def crearCategoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombreCategoria= input()
        rutaNueva =Path(ruta, nombreCategoria)


        if not os.path.exists(rutaNueva):
            Path.mkdir(rutaNueva)
            print(f"Tu nueva categoria {nombreCategoria} ha sido creada")
            existe= True
        else:
            print("Esa categoria ya existe")
def eliminarReceta (receta):
     Path(receta).unlink()
     print(f"La receta {receta.name} ha sido eliminada")

def eliminarCategoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria} ha sido eliminada")

def volverInicio():
    eleccionRegresar = 'x'
    while eleccionRegresar.lower() != 'v':
        eleccionRegresar = input("\n presione v para volver al menu")


finalizarPrograma = False

while not finalizarPrograma:
    menu = inicio()

    if menu ==1:
        misCategorias=mostrarCategorias(mi_ruta)
        miCategoria =elegirCategoria(misCategorias)
        misRecetas = mostrarRecetas(miCategoria)
        if len(misRecetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            miReceta= elegirRecetas(misRecetas)
            leerReceta(miReceta)
        volverInicio()

    elif menu == 2:
        misCategorias = mostrarCategorias(mi_ruta)
        miCategoria = elegirCategoria(misCategorias)
        crearReceta(miCategoria)
        volverInicio()

    elif menu == 3:
        crearCategoria(mi_ruta)
        volverInicio()

    elif menu == 4:
        misCategorias = mostrarCategorias(mi_ruta)
        miCategoria = elegirCategoria(misCategorias)
        misRecetas = mostrarRecetas(miCategoria)
        if len(misRecetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            miReceta = elegirRecetas(misRecetas)
            leerReceta(miReceta)
        eliminarReceta(miReceta)
        volverInicio()

    elif menu == 5:
        misCategorias = mostrarCategorias(mi_ruta)
        miCategoria = elegirCategoria(misCategorias)
        eliminarCategoria(miCategoria)
        volverInicio()

    elif menu == 6:
        finalizarPrograma =True

