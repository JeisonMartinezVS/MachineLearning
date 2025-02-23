import pandas as pd
import numpy as np
from numba import njit
from functools import reduce
import matplotlib.pyplot as plt
import seaborn as sns

my_list = []
for number in range(0, 21):
    if number % 2 == 0:
        my_list.append(number)
# print(my_list[1:])

my_list2 = [number for number in range (0,21) if number % 2 == 0]
# print(my_list2[1:])

@njit
def pares_numpy():
    N = 20
    v = np.zeros(int(N/2)+1)
    i = 0
    for number in range (0, 21):
        if number % 2 == 0:
            v[i] = number
            i += 1
        return v
    
# print(pares_numpy())

## DEFINICION DE FUNCIONES ##
def times_tables1():
    """
    Params:
    ---
    Return:
    --- lst: list
    """
    lst = []
    for i in range (10):
        for j in range(10):
            lst.append(i*j)
    return lst
        
#print(times_tables1())

## Filter Funtion ##

def multiple(number): # Declaramos una funcion condicional
    if number % 5 == 0: # Comprobamos si este numero es multiplo de cinco
        return True

numeros = [2, 5, 10, 23, 50]
a = filter(multiple, numeros)
print(list(a))
    
a = map(multiple, numeros)
print(list(a))

## ------------------------------------------------ ##
a = [1,2,3,4,5]
b = reduce(lambda x, y: x + y, a,a)
print(list(b))

