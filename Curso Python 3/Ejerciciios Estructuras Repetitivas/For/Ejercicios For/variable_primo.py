# Escribe un programa que diga si un número introducido por teclado es o no primo y sui no siga preguntando 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

numero_primo = False

while not numero_primo:
    numero = int(input("Introduce un número: "))
    numero_primo = True

    for num in range(2, numero):
        if numero % num == 0:
            numero_primo = False
            print("No es un número primo. Vuelve a escribir")
            break

if numero_primo:
    print("Es un número primo")