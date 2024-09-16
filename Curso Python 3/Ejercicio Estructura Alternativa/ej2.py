# Escribe un programa que pida un nombre de usuario y una contraseña
# Si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

user = input("Introduce el usuario ")
contra = input("Introduce la contraseña ")

if user == 'pepe' and contra == 'asdasd':
    print ("Credenciales correcta: Bienvenido pepe")
else:
    print ("Las credenciales no son correctas")
    print ("Programa terminado")
    
    
    