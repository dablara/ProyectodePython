# Pide una cadena y un caracter por teclado (valida que sea un caracter)
# y muestra cuantas veces aparece ese caracter en la cadena

cad = input("Introduce una cadena ")
while True:
    carac = input("Introduce un caracter ")
    if len(carac) == 1: break

if cad.count(carac):
    print ("En la cadena",cad "aparecen",cad.count(carac),"veces el caracter",carac))
else:
    print ("El caracter NO aparece en la cadena")

    
