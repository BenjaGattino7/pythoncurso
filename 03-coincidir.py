
'''#Sin Match
serie = "1"

if   serie == "1":
    print("Samsung")
elif serie=="2":
    print("nokia")
elif serie =="3":
    print("motorola")

#Con Match

serie="2"
match serie:
    case "1":
        print("Samsung")
    case "2":
        print("nokia")
    case "3":
        print("motorola")'''

cliente ={'nombre': 'Federico',
          'edad':23,
          'ocupacion': 'Caminar'}

pelicula ={'titulo':'matrix',
           'ficha_tecnica':{'protagonista':'Keanu Reeves',
                            'director':'Hermanos Wachowski'}}
elementos =cliente, pelicula, 'libro'

for e in elementos:
    match e:
        case{'nombre':nombre,
             'edad':edad,
             'ocupacion':ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case{'titulo':titulo,
             'ficha_tecnica':{'protagonista':protagonista,
                              'director':director}}  :
            print("es una pelicula")
            print(titulo,protagonista,director)


