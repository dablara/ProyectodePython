# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
import random
def calcularMaxin(lista_numero):
    return (max(lista_numero),min(lista_numero))




numeros = []
# Se  inicia la lista con valores aleatorios 
for i in range(10):
    numeros.append(random.randint(1,100))
vmax,vmin= calcularMaxin(numeros)
print ("El valor maximo es ",vmax)
print ("El valor minimo es ",vmin)