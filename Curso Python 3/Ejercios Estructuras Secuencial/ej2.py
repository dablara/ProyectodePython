# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math
cateto1 = float ( input ("Introduce cateto 1 " ))
cateto2 = float ( input ("Introduce cateto 2 " ))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 **2)

print ("El resultado de la suma de los cateto es %.2f" %hipotenusa) # %.2f se usa en este caso para sacar dos decimales

