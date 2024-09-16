#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horapart = int(input("Hora de salida "))
mintpart = int(input("minutos  de salida "))
segpartida = int(input("segundos  de salida "))
segviaje =  int(input("Tiempo en segundos "))

# Convierto la hora de salida en segundos 
seginicial = horapart * 3600 + mintpart*60 + segpartida
# Sumo los segundo que ha tardado
segfinal = seginicial + segviaje
# Convierto los egundo a horas,minutos y segundos 
horallegada = segfinal // 3600; 
minllegada = (segfinal % 3600) // 60;
segllegada = (segfinal %3600) % 60;

print ("Hora de llegada")
print (horallegada,":",minllegada,":",segllegada)