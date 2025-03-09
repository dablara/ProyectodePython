# Operadores


dividendo = int(input("¿Cual es el dividendo? "))
divisor = int(input("¿Cual es el divisor? "))

division = dividendo / divisor
division_sindecimal = "{:.1f}".format(division)
conciente = dividendo // divisor
resto = dividendo % divisor

print ("El resultado de dividir ",dividendo ,"entre", divisor ,"es ",division_sindecimal, " el cociente de dicha division es ",conciente, " y su resto es ",resto )