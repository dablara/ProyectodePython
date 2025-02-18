# Crear un programa Python que permita cifrar y descifrar mediante el sistema César
# El programa debe poder
    # 1. Recibir un parámetro numérico.
    # 2. Recibir un texto en claro o un texto cifrado.
    # 3. Indicar la acción que queremos realizar: cifrar o descifrar.
    
while True:
    op = input('¿Quieres (C)ifrar o (D)escifrar? ').lower()
    if op in ['c', 'd']:
        texto = input(f'¿Qué quieres {"cifrar" if op == "c" else "descifrar"}? ')
        alfa = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" if texto.isupper() else "abcdefghijklmnñopqrstuvwxyz"
        num = int(input('Introduce el número de saltos: '))
        resultado = ""
        for cifra in texto:
            if cifra in alfa:
                resultado += alfa[(alfa.index(cifra) + (num if op == "c" else -num)) % len(alfa)]
            else:
                resultado += cifra
        print(f'El texto {"cifrado" if op == "c" else "descifrado"} es: {resultado}')
        break
    else:
        print("Los parametros permitidos son (C)ifrar o (D)escifrar.")
        