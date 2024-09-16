#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#* 55% del promedio de sus tres calificaciones parciales.
#* 30% de la calificación del examen final.
#* 15% de la calificación de un trabajo final

nota1 = int(input('Introduce primera nota parcial '))
nota2 = int(input('Introduce segunda nota parcial '))
nota3 = int(input('Introduce tercera nota parcial '))
nota4 = int(input('Introduce nota de examen final '))
nota5 = int(input('Introduce nota de trabajo '))

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
    print ('Las notas deben estar comprendidas entre 0 y 10')
elif (nota3 < 0 or nota3 > 10) or (nota4 < 0 or nota4 > 10):
   print('Las notas deben estar comprendidas entre 0 y 10')
elif nota5 < 0 or nota5 > 10:
     print('Las notas deben estar comprendidas entre 0 y 10')
else:
    notasparciales= nota1+nota2+nota3
    promedio = notasparciales/3
    tres = 55*promedio/100
    notafinal = 30*nota4/100
    trabajo =  15*nota5/100
    evaluacion = tres+notafinal+trabajo
   
    print (f'Las notas de los parciales son {nota1},{nota2},{nota3} ')
    print (f'La nota del examen final es {nota4}')
    print (f'La nota del trabajo final es {nota5}')
    print (f'La nota final de la evaluación es {evaluacion:.1f}') 