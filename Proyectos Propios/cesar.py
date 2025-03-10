# Nombre: Daniel Blanco Aranda
    # Crear un programa Python que permita cifrar y descifrar mediante el sistema César
    # El programa debe poder
        # 1. Recibir un parámetro numérico.
        # 2. Recibir un texto en claro o un texto cifrado.
        # 3. Indicar la acción que queremos realizar: cifrar o descifrar.
# Fecha: 26/02/2025

while True:
    ope = input('¿Quieres (C)ifrar o (D)escifrar? ').lower()
    if ope in ['c', 'd']:
        texto = input(f'¿Qué quieres {"cifrar" if ope == "c" else "descifrar"}? ')
        
        num = int(input('Introduce el número de saltos: '))

        resultado = ""
        for cifra in texto:
            if cifra.isalpha(): 
                if cifra.isascii():  # ciframos o desciframos si la letra está en ascii si es ñ o con acento se queda tal cual
                    # se usa ASCII de la letra
                    inicio = ord('a') if cifra.islower() else ord('A')  # determinamos el inicio según minúsculas o mayúsculas
                    # se calcula el nuevo valor ASCII desplazado
                    valor_nuevo = (ord(cifra) - inicio + (num if ope == "c" else -num)) % 26 + inicio
                    resultado += chr(valor_nuevo)  # Convertimos el código ASCII de vuelta a un carácter
                else:
                    
                    resultado += cifra
            else:
                # Si no es una letra (espacios, puntuación, etc.), la dejamos igual
                resultado += cifra

        print(f'El texto {"cifrado" if ope == "c" else "descifrado"} es: {resultado}')
        break
    else:
        print("Los parámetros permitidos son (C)ifrar o (D)escifrar.")
