contra = "Cordoba"
 
clave = input ("Dime la clave: ")

while clave != contra:
    print ("Clave Incorrecta ")
    otra = input("¿Quieres introducir otra Clave? (S/N)? ")
    if otra.upper()=="N":
        break;
    clave = input ("Dime la clave ")
if clave == contra:
    print ("Clave Correcta: Bienevido !!!")
print ("Programa terminado")


 