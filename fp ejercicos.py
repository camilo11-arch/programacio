# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:39:10 2021

@author: Usuario
"""

import random

cont_rep = 0
acu_sum_totl = 0
acu_sum_pos = 0
acu_sum_neg = 0
acu_div_positivos=0
acu_div_negativos=0
promedio_numpostivos=0
promedio_nuemrosnegativos=0
promedio_numerostotal=0
cant_num = int(input("ingrese la cantidad de numeros : "))

for cont_rep in range (cant_num +5):
    num = random.randint(-100,100)
    print("el numero es : ",num)
    acu_sum_totl = acu_sum_totl + num
    if num > 0:
        acu_sum_pos = acu_sum_pos + num
    else:
        acu_sum_neg = acu_sum_neg + num
        acu_sum_pos=acu_sum_neg
    
print("la suma de todos los numeros es : ", acu_sum_totl)
print("la suma de todos los positivos es : ", acu_sum_pos)
print ("la suma de todos los negativos es : ",acu_sum_neg)
