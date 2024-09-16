# Realizar un programa que inicialice una lista con 10 valotrd 
# aleatorios y posteriormente muestre en pantalla cada elemento de la lista 
# y sy cubo

import random # como vamos a usar aleatorios usamos la libreria random
lista_numeros = []
# Hacemos el recorrido que lee la lista 
for indice in range (1,11):
    lista_numeros.append(random.randint(1,10))
# volvemos a hacer el recorrido
for numero in lista_numeros:
    print(numero," ",numero ** 2," ",numero **3)


