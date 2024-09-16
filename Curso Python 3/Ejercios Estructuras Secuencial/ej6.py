# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input ("Introduce tu nombre ")
ap1 = input ("Introduce tu primer apellido ")
ap2 = input ("Introduce tu segundo apellido ")

inicial = nombre[0]
inicial = inicial + ap1[0]
inicial = inicial + ap2[0]
inicial = inicial.upper()

print("Tus iniciales son ",inicial)

 