# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
#(comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.




notas=[]
for indice in range (1,6):
    while True:
        nota = int(input("Introduce la nota %d: " % indice)) # Intriducimos la nota que estara en la lista
        if nota >=0 and nota<=10: break # Si no estan entre 0 a 10 acaba el programa
    notas.append(nota)
            
# Mostramos los resultados 

print ("Notas: ",end="")
for nota in notas:
    print(nota," ",end="") # Mostrar todas las notas
print()
print( "Nota media: ", sum(notas)/len(notas)) # Nota media
print( "Nota Maxima: ",max(notas)) # Nota maxima
print ("Notas min",min(notas)) # Nota minima
 

         

