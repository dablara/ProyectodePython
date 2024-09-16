# Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado


tabla = int(input("Introduce un número "))
for numero in range(1,11):
    print ("%d * %d = %d" % (numero,tabla,numero * tabla))
    
    