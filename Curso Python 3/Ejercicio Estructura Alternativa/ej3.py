# Algoritmo que te pide tres números y te los ordena de mayor a menor 

n1 = int(input("Introduce número 1 "))
n2 = int(input ("Introduce número 2 "))
n3 = int(input ("Introduce número 3 "))

if n1>n2 and n1>n3:
    if n2>n3:
        print (n1,n2,n3)
    else:
        print (n1,n3,n2)

if n2>n1 and n2 >n3:
    if n1>n3:
        print (n2,n1,n3)
    else:
        print (n2,n3,n1)
if n3>n1 and n3>n2:
    if n3>n1:
        print (n3,n1,n2)
    else:
        print (n3,n1,n2)
