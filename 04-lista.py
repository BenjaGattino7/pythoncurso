palabra ='python'

lista =[]

for letra in palabra:
    lista.append(letra)

print (lista)

#↓↓↓↓↓↓↓↓↓↓

palabra ='vibora'

lista =[letra for letra in palabra]

print (lista)

#↓↓↓↓↓↓↓↓↓↓

lista =[letra for letra in 'serpiente']
print (lista)

#numeros

lista=[n for n in range (0,20,1) if n%3 ==0]
print(lista)

#conversion

pies = [10, 15, 20, 30]
metros = [round(p / 3.281, 2) for p in pies]

print(metros)