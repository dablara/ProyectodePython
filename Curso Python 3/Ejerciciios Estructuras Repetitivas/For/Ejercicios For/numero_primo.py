# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

primo = True


numero = int(input("Introduce un número "))


for num in range(2,numero):
    if numero % num == 0:
        primo = False
        break
if primo:
    print ("Es un número primo")
else:
    print ("No es un número primo")
    