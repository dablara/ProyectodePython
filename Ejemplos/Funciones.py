# Aqui vere las funciones 
# La funciones pueden devolver cosas o pueden estar vacias
# Funciones predefinidas del propio lenguaje y funciones propias las que tu creas

#Repetiremos 5 veces estas funciones con funciones 

#definicion de la funcion

print ("Funcion para sacar el mensaje")
def mensaje():    # def se usa para definir  y dentro de los oparentesis puede o no haber algo
    print ("Hola mundo")
    print ("Me llamo Daniel")
    print ("Tengo 26 años")

# Llamada a la funcion
mensaje()

print ("---------------------")
print ("Ejecutando codigo fuera de la funcion")

print ("---------------------")

mensaje()

print ("---------------------")

print ("Ahora haremos una suma con una función")

# Haremos una suma

def suma():
    num1= 5
    num2= 7
    print (num1+num2)

suma()

print ("---------------------")

# Ahora usaremos argumentos en las funciones para en cada llamada haga una suma diferentre

print ("Ahora usaremos argumentos en las funciones para en cada llamada haga una suma diferentre")
def suma2(num1, num2): # Zona de parametros
    print (num1+num2)

print ("Primera suma")
suma2(35,548) # num 1 es igual a 35 y num2 es igual a 548
print ("Segunda suma")
suma2(5,7)
print ("Tecera suma")
suma2(45,8)

# Usaremos funcion return , que devuelve un valor
print ("Usaremos la funcion return")

def suma2(num1, num2): # Zona de parametros
    resultado=(num1+num2)

    return resultado #Devuelve la variable resultado

print ("Primera suma")
print (suma2(35,548)) # Esto si devolvera el resultado gracias a return , y con los demas no
print ("Segunda suma")
suma2(5,7)
print ("Tecera suma")
suma2(45,8)

print ("----------------------")
print ("Almacaneramos en una variable ")
def suma2(num1, num2): # Zona de parametros
    resultado=(num1+num2)

    return resultado #Devuelve la variable resultado

guarda_resultado = suma2(35,348)
print (guarda_resultado) # Aqui iria el resultado de la suma

