# Crear un programa Python que permita cifrar y descifrar mediante el sistema César
# El programa debe poder
    # 1. Recibir un parámetro numérico.
    # 2. Recibir un texto en claro o un texto cifrado.
    # 3. Indicar la acción que queremos realizar: cifrar o descifrar.
    
while True:
    
    op= input('¿Quieres (C)ifrar o (D)escifrar? ').lower()

    if (op == "c"):
        cifrado= input('¿Que quieres cifrar ')
        if cifrado == cifrado.upper():
            alfa="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" # Mayusculas
        else:
            alfa="abcdefghijklmnñopqrstuvwxyz" # Minusculas
        num= int(input('Introduce el número del saltos a los que quieres cifrar ')) # Número de desplazmiento que se van a dar 
        resultado="" # Aqui se almacena el resultado
        for cifra in cifrado:
            if cifra in alfa:
               resultado += alfa[(alfa.index(cifra) + num) % len(alfa)]  # Esta es la línea corregida # Recorre la cadena alfa tantas veces como tenga el valor num
            else:
                resultado+=cifra # Si no está en el alfabeto, lo agrega tal cual
        print("El texto cifrado es",resultado) # Toma el valor de cifra y lo añade a resultado tal como está.
        break # Sale del bucle si la opción es válida
    
    elif (op == "d"):
        descifrado = input('Introduce texto a descifrar ')
        if descifrado ==descifrado.upper():
            alfa="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" # Mayusculas
        else:
            alfa="abcdefghijklmnñopqrstuvwxyz" # Minusculas
        num2= int(input('Introduce el número del saltos a los que quieres cifrar ')) # Número de desplazmiento que se van a dar 
        resultado="" # Aqui se almacena el resultado
        for cifra in descifrado:
            if cifra in alfa:
               resultado += alfa[(alfa.index(cifra) - num2) % len(alfa)]  # Esta es la línea corregida # Recorre la cadena alfa tantas veces como tenga el valor num
            else:
                resultado+=cifra # Si no está en el alfabeto, lo agrega tal cual
        print("El texto descifrado es",resultado) # Toma el valor de cifra y lo añade a resultado tal como está.
        break
   
    else:
        print ("Los parametros permitidos son (C)ifrar o (D)escifrar ")


 