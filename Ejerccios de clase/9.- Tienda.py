# 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
# cuanto deberá pagar finalmente por su compra.

# Autor: Daniel Blanco Aranda

precio =  float (input('Introduzca el precio de la compra '))

ahorro = (15*precio)/100 #tambien podemos poner precio*0.15
precio_final = precio - ahorro

print (f'El precio base del producto es {precio}€ y el precio final con 15% de descuento es {precio_final:.2f}€ y nos hemos ahorrado {ahorro:.2f}€')
