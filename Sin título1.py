# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:46:24 2021

@author: camilo lopez
"""
import random

cont_rep = 0
acu_sum_totl = 0
acu_sum_pos = 0
acu_sum_neg = 0
prom_num_totl = 0
prom_num_pos = 0
prom_num_neg = 0


cant_num = int(input("ingrese la cantidad de numeros : "))

while cont_rep <= cant_num:
    num = random.randint(-100,100)
    print("el numero es : ",num)
    acu_sum_totl = acu_sum_totl + num
    if num > 0:
        acu_sum_pos = acu_sum_pos + num
    else:
        acu_sum_neg = acu_sum_neg + num
    cont_rep = cont_rep + 1

print("la suma de todos los numeros es : ", acu_sum_totl)
print("la suma de todos los positivos es : ", acu_sum_pos)
print ("la suma de todos los negativos es : ",acu_sum_neg)
print("la suma de todos los numeros : ", prom_num_totl)
print("el promedio de los numeros positivos es : ", prom_num_pos)
print("el promedio de los numeros negativos es : ", prom_num_neg)
