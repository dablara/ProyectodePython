# Nombre: menu.py
# Autor: Daniel Blanco Aranda
# Fecha: 17-07-2024 


# Importamos las librerías
import subprocess # Nos permite ejecutar comando tanto en Linux como en Windows
import os # Nos permite interactuar con el Sistema operativo. 

print( " Bienvenido al menú de opciones")
# Creamos el menú con sus opciones

ops = True
while ops:
    print( """
    1. Crear Usuario
    2. Listar Usuarios 
    3. Borrar Usuario
    4. Mostrar interfaces de red
    5. Ejecutar Update 
    6. Ejecutar Upgrade
    7. Salir 
    """)
     
    ops= input("¿Qué opción deseas? ")
    if ops == "1":
       print("\n Se va a crear un usuario")
       name = input("¿Cómo se llama el nuevo usuario?")
       comando = ["sudo","adduser",name]
       subprocess.run(comando) #subprocess sirve para ejecutar comandos
       print(f"Usuario {name} creado")
    
    elif ops == "2":
        user= print("\n Se van a listar los usuarios")
        
    
    elif ops == "3":
        user= input ("¿Que usuario deseas borrar? ")
        comando ["sudo","userdel",user]
    
    elif ops == "4":
        print ("\n Estas son las interfaces del equipo")
        comando = ["ifconfig"]
        subprocess.run(comando)
   
    elif ops == "5":
        print("\n Ejecutando update")
        comando = ["sudo apt-get update"]
        subprocess.run(comando)
   
    elif ops == "6":
        print("\n Ejecutando upgrade")
        comando = ["sudo","apt-get upgrade"]
        subprocess.run(comando)
   
    elif ops == "7":
        print("\n Adiós")
        quit ()       
   
    elif ops !="":
        print ("Elige una opción correcta")
        
        
