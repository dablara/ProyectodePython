while True:
    try:
        x = int(input("Introduce un numero "))
        break
    except ValueError:
        print ("Debes introducir un número ")