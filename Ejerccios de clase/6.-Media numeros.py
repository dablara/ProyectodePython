# 6. Calcular la media de tres números pedidos por teclado.

# Autor: Daniel Blanco Aranda



import math
n1 = int(input('Introduce el primer número '))
n2 = int(input('Introduce el segundo número '))
n3 = int(input('Introduce el tercer número '))



conjunto = [n1,n2,n3]
suma = n1+n2+n3
media = suma/len(conjunto)


print(f'Los tres números son {conjunto} y la media es {media}')

