# Crear un programa Python que permita cifrar y descifrar mediante el sistema César
# El programa debe poder
    # 1. Recibir un parámetro numérico.
    # 2. Recibir un texto en claro o un texto cifrado.
    # 3. Indicar la acción que queremos realizar: cifrar o descifrar.
    
while True:
    
    accion = input('¿Que quieres hacer (C)ifrar o (D)escifrar? ').lower()

    if (accion == "c"):
        cifrado= input('Introduce texto a cifrar ')
        num= int(input('Introduce el número del saltos a la que quieres que cifre '))
        break # Sale del bucle si la opción es válida
    
    elif (accion == "d"):
        print ('Introduce texto a descifrar ')
        num2= int(input('Introduce el número del saltos a la que quieres que descifre '))
        break
   
    else:
        print ("La parametros permitidos son (C)ifrar o (D)escifrar ")


 