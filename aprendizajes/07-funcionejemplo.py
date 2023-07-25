"""

for cafe,precio in preciocafe:
    print(cafe,precio)"""

def cafeMasCaro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro=''
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe

    return cafe_mas_caro , precio_mayor

preciocafe=[('capucchino',500),('expreso',400),('Moka',700)]
resultado=cafeMasCaro(preciocafe)
print(resultado)