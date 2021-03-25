# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:17:48 2021

@author: Usuario
"""
print ("SISTEMAS DE NOTAS DE UN CURSO DE PROGRAMACIOS")

#ENTRADA


num_est = int(input("Digite la cantidad de estudiantes del grupo: "))


#Declarar la variable que controla el ciclo
contadorRepeticiones = 0

cantidadEstudiantesAprobaron = 0

CantidadEstudiantesReprobaron = 0

sumaDefinitivaDeEstudiantes = 0.0

sumaDefinitivaDeEstudiantesAprobaron = 0.0

sumaDefinitivaDeEstudiantesReprobaron = 0.0

promedioDefinitivaEstudiantes = 0.0
promedioDefinitivaEstudiantesAprobaron = 0
promedioDefinitivaEstudiantesReprobaron = 0
#Proceso
#Iniciar ciclo

while contadorRepeticiones <= num_est :
    
#lectura de las notras de cada estudiante 

    nom_estudiante = (input("Digite nombre del estudiante :"))

    not_1 = float(input("Digite la nota del primer parcial del estudiante :"))

    not_2 = float(input("Digite la nota del segundo parcial del estudiante :"))

    not_3 = float(input("Digite la nota del tercer  parcial del estudiante :"))
    
    #Calcular la definitiva de cada estudiante 
    not_definitiva = (not_1 + not_2 + not_3)/3
    #Sumar las definitivas de los estudiantes para calcular el promedio 
    sumaDefinitivaDeEstudiantes = sumaDefinitivaDeEstudiantes+not_definitiva
    print("La definitiva es :", not_definitiva)
    if(not_definitiva >= 3.0):
        cantidadEstudiantesAprobaron = cantidadEstudiantesAprobaron+1
        #sumar las notas de los estudiantes que aprobaron 
        sumaDefinitivaDeEstudiantesAprobaron=sumaDefinitivaDeEstudiantesAprobaron+not_definitiva
   
    else:
        CantidadEstudiantesReprobaron = CantidadEstudiantesReprobaron+1
        #sumar las notas de los estudiantes que reprobaron
        sumaDefinitivaDeEstudiantesReprobaron = sumaDefinitivaDeEstudiantesReprobaron+not_definitiva
        

    #Incrementar la variable que controla el ciclo 
    contadorRepeticiones = contadorRepeticiones+1
    
    
    #Fin del ciclo
#calcular el promedio del grupo
promedioDefinitivaEstudiantes = sumaDefinitivaDeEstudiantes/num_est
promedioDefinitivaEstudiantesAprobaron = sumaDefinitivaDeEstudiantesAprobaron/cantidadEstudiantesAprobaron
promedioDefinitivaEstudiantesReprobaron = sumaDefinitivaDeEstudiantesReprobaron/CantidadEstudiantesReprobaron
    
    
print("OTROS CALCULOS")
print("2. Cantidad de estudiantes que aprobaron :" , cantidadEstudiantesAprobaron)
print("3. Cantidad de estudiantes que reprobaron :", CantidadEstudiantesReprobaron)
print("4. Promedio del grupo:", promedioDefinitivaEstudiantes)
print("5. promedio de estudiantes que aprobaron :", promedioDefinitivaEstudiantesAprobaron)
print("6.promedio de estudiantes que reprobaron : ",promedioDefinitivaEstudiantesReprobaron)



