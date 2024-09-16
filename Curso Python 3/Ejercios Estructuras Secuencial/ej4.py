# Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = int(input("Introduce las variable "))
b = int(input("Introduce las variable "))
        
aux = a # Guardo el varlo de a en aux 
a = b # hacemos el intercambio
b = aux # lo que tenia en aux ahora esta en b

print ("Nuevo valor de a",a)
print ("Nuevo valor de b",b)

