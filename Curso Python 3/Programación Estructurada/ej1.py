#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def esmultiplo(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
    
numero1 = int(input("Intriduce primero número "))
numero2 = int(input("Introduce segundo número "))

if esmultiplo(numero1,numero2):
    print(numero1," es múltiplo de",numero2)
else:
    print(numero1," NO es múltiplo de",numero2)