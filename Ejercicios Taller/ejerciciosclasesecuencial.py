
#Escribe un programa que pregunte el nombre y la edad del usuario y despues los muestre por pantalla con la frase 
# "Tu nombre es (nombre) y tu edad es (edad)"

# Autor: Daniel Blanco Aranda
nombre = input ('¿Como te llamas')
edad = input ('¿Que edad tienes?')

print (f'El alumno se llama {nombre} y tiene  {edad} años')
print ('----------------------')


#Preguntale al usuario el lado de un cuadrado y calcula su área(lado x lado), despues muestrala por pantalla
l1 = int (input ('¿Cuanto mide el primer lado? '))
l2 = int (input('¿Cuanto mide el segundo lado? '))

resultado = l1 * l2

print (f'El resultado de los lados del cuadrdo es: {resultado} ')

print ('----------------------')


#Preguntale al usuario el nombre  y el primer apellido y muestrale sus inicales
nombre = input ('Cual es tu nombre?' )
apellido = input ('¿Cual es tu primer apellido?' )

iniciales = nombre[1]+apellido[1]

print (f'Mis iniciales son {iniciales}')
print ('----------------------')

#Pide al usuario dos numeros, sumalos, restalos, dividelos y multiplícalos entre si y muestra por pantalla el resultado de cada operaión
n1 = int(input('¿Cual es el primer numero?' ))
n2 = int (input('¿Cual es el segundo numero' ))

suma= n1+n2
resta= n1-n2
multiplicacion = n1*n2
division = n1/n2

print (f'El resultado de la suma es: {suma}')
print (f'El resultado de la resta es: {resta} ')
print (f'El resultado de la multiplicacion es: {multiplicacion} ')
print (f'El resultado de la division es: {division} ')

print ('----------------------')

#Programa que te pida la cantidad que vas a comprar de un producto, tambien te pida el precio individual de este y despues muestres por pantalla lo que cuesta tu compra 
cant = int(input('¿Que cantidad vas a comprar?'))
precio = float(input('¿Cuanto cuesta el producto?'))

result = cant*precio

print(f'Tu compra de hoy ha sido {result}')

print ('----------------------')


#Pedir al usuario el número  de objetos que tengo y entre cuantos los tengo que dividir, y que me digan cuantos van a sobrar si los quiero repartir en parte iguales


objetos = int(input('¿Cuantos objetos vas a coger '))
div = int(input('¿Entre cuantas personas vas a repartirlo '))


sobre = objetos%div

print(f'Has cogido {objetos} y van a sobrar {sobre} objetos')