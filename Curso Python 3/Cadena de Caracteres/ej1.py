# Realiza un programa que comprueba si una cadena leida por teclado
# comienza por una subcadena introducida por tecladi

cad = input("Introduce la cadena ")
subcad = input("Introduce la otra cadena ")

if cad.startswith(subcad): # Comprobamos si contiene la cadena
    print ("La cadena comienza por la subcadena")
else:
    print("La cadena NO comienza por la subcadena")
    
    