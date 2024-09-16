# Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.


suma = 0
cont = 0
numero = int(input("Introduce un número "))
while numero > 0:
    suma = suma + numero
    cont = cont + 1
    numero = int(input("Introduce un número "))

if cont > 0:
    media = suma / cont
else:
    media = 0
    
print ("Suma: ",suma)
print ("Media: ",media)



    