# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:02:56 2021

@author: camilo lopez
"""
cuadradonumero=0
acomuladorsuma=0
num=1
#procesos
#ciclopara de 1 hasta 100
cantidadnumeros= int(input("cantidad de numeros: "))
for num in range(cantidadnumeros+1):
    cuadradonumero=num*num
    acumuladorsuma=acomuladorsuma+cuadradonumero
    print ("el cuadrado de :",num,"es:",cuadradonumero)
    print("la suma acomulada es: ",acomuladorsuma)
    #fin de ciclo
    print("la suma de los cuadrados es: ",acumuladorsuma)