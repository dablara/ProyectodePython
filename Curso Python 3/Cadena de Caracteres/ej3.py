#Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), 
# realiza un programa que cuente cuantas palabras tiene.

cont = 0
posicion = 0
cad = input("Introduce una cadena por teclado ")

# Eliminamos los espacios que haya en la cadena 
cad= cad.strip() # Asi se quitan los espacios al principio y al final
# Buscamos los demas espacios 
posicion = cad.find(" ", posicion)
while posicion != -1:
        cont = cont + 1
        
        while cad[posicion + 1] == " ":
            posicion = posicion + 1
print ("La frase tiene",cont + 1, "palabras.")
