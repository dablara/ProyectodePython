# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y
# nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios = {"aguacate": 3,"manzana":1, "platano":1.5,"naranja":2}

while True:
    fruta = input("¿Que fruta quieres ? ")
    if fruta.lower() not in precios:
        print ("No disponemos de esa fruta en estos momentos")
    else:
        cantidad= int(input("¿Que cantidad quieres de esta fruta? "))
        print("El precio es de %f" % (cantidad * precios[fruta.lower()]))
    opcion = input("¿Quires más frutas (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quires más frutas (s/nS)")
    if opcion.lower()=="n":
        print("Gracias por confiar en nosotros la esperamos")
        break