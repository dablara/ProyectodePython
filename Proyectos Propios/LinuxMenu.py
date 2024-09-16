# Nombre: linuxmenu.py
# Descripción: Un script básico en Python para la administración de Linux, con los comandos más usados en dicho sistema operativo.
# Autor: Daniel Blanco Aranda
# Fecha: 17-07-2024 


# Importamos las librerías
import subprocess # Nos permite ejecutar comando tanto en Linux como en Windows
import os # Nos permite interactuar con el Sistema operativo. 

print("Bienvenido al menú de opciones")
print ("En este menú podras elegir entre varias opciones para una buena Administración de Linux")

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
        print("\nSe va a crear el usuario")
        name = input("¿Cómo se llamará el usuario ? ")
        if name:
            comando = ["sudo","adduser", name,"--force-badname"]
        try:
            subprocess.run(comando, check=True) # Se asegura que la ejecución del comando sea efectiba
            print(f"Usuario {name} creado")
        except subprocess.CalledProcessError as e: # Maneja el error cuando un comando ejecutado con subprocess no funciona correctamente, se pone "e" despues de as como abreviación de error
            print(f"Error al crear el usuario: {e}")
        else:
            print("El nombre no puede estar vacío")

    
    elif ops == "2":
        print ("Se listaran los usuarios")
        comando = ["less","/etc/passwd"]
        try:
            subprocess.run(comando,check= True)
        except subprocess.CalledProcessError as e:
            print ("No se ha listado bien los usuarios")
    
    elif ops == "3":
        name = input("¿Qué usuario deseas eliminar? " )
        comando = ["sudo","deluser",name]
        try:
            subprocess.run(comando,check=True)
            print(f"El usuario {name} ha sido eliminado")
        except subprocess.CalledProcessError as es:
            print ("No se han escrito un usuario correcto")
         
    
    elif ops == "4":
        print(f"Estas son las interfaces de red del equipo")
        comando = ["ifconfig"]
        try:
            subprocess.run(comando,check=True)
        except subprocess.CalledProcessError as e:
            print(f"Te has equivocado de comando")
    
    elif ops == "5":
        print ("Se actulizarán los paquetes")
        comando= ["sudo","apt","update"]
        try:
            subprocess.run(comando,check= True)
        except subprocess.CalledProcessError as e:
            print("No se ha puesto bien el comando")
    
    elif ops == "6":
        print ("Se actulizarán los paquetes")
        comando= ["sudo","apt","upgrade"]
        try:
            subprocess.run(comando,check= True)
        except subprocess.CalledProcessError as e:
            print("No se ha puesto bien el comando")
    elif ops == "7":
        print(f"Adios, Gracias por usar nuestro script")
        quit()
    else:
        print ("Elige un opcion que este entre 1 y 7")
        
