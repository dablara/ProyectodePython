# 7. Realiza un programa que reciba una cantidad de minutos y 
# muestre por pantalla a cuantas horas y minutos corresponde.

# Autor: Daniel Blanco Aranda

minutos = int(input('Introduce un número de minutos '))

horas= minutos//60
minutaje = minutos%60

print (f'{minutos} minutos son {horas} horas y {minutaje} minutos ')

