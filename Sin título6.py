# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:13:43 2021

@author: Usuario
"""
import math
#programa que calcula la hipotenusa y el area de un triangulo rect
#variables
ve_catetoUno=0.0
ve_catetoDos=0.0

vps_hipotenusa=0.0
vps_perimetro=0.0
# entradas

ve_catetoUno = int (input("digite cateto uno: "))
ve_catetoDos = int (input("digite cateto dos: "))
#procesos
vps_hipotenusa= math.sqrt(math.pow(ve_catetoUno,2)+ math.pow (ve_catetoDos,2)
#salida
print("hipotenusa: ",vps_hipotenusa)


