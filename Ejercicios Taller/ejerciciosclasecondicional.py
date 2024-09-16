# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si  el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

# Autor: Daniel Blanco Aranda
edad = int(input('¿Que edad tiene el cliente '))

if edad <= 4:
  print ('Enhorabuena no pagas nada')
elif edad >=4 and  edad<= 18:
    print ('La entrada te costara 5€')
elif edad > 18:
    print ('La entrada te costara 10€')
print ('----------------')
#Escribe un programa que le introduzcas el número del mes y te imprima por pantalla el nombre(ej. 1 --> enero)

mes = int(input('Di el numero del mes '))

if mes == 1:
  print = ('El mes es Enero')
elif mes ==2:
  print ('El mes es Febrero')
elif mes ==3:
  print ('El mes es Marzo')
elif mes == 4:
  print ('El mes Abril')
elif mes == 5:
  print ('El mes es Mayo')
elif mes == 6:
  print ('El mes es Junio')
elif mes == 7:
  print ('El mes es Julio')
elif mes == 8:
  print ('El mes es Agosto')
elif mes == 9:
  print ('El mes es Septiembre') 
elif mes == 10:
  print ('El mes es Octubre')
elif mes == 11:
  print ('El mes es Noviembre')
elif mes == 12:
  print ('El mes es Diciembre') 
else:
  print ('Solo hay 12 meses')

print ('----------------')
 
  # Otra forma de hacer lo de los meses con listas- Recorre la lista
meses = ['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
opcion = int(input('Número:'))
print(f'El mes es {meses[opcion]} ')

print ('----------------')

# Escribe un programa donde introduzcas un número y su divisor, si el resto de la división no es 0 que aparezca el resto por pantalla, sino que solo salga la división.
print ('Haremos un division')
numero = int(input('Introduce el numero'))
divisor = int(input('Introduce el divisor'))

cuenta = numero/divisor

resto= numero%divisor

if resto != 0:
  print (f'El resto es {resto}')
else:
  print(f'El resultado de la division de {numero} y {divisor} es {cuenta}')

print ('----------------')

# Crea un programa que determine si un número es positivo, negativo o cero.

numero = int(input('Introduce el numero'))

if numero ==0:
  print ('El numero es 0 ')
elif numero >= 1:
  print ('El numero es positivo ')
elif numero < 0:
  print ('El numero es negativo ')

