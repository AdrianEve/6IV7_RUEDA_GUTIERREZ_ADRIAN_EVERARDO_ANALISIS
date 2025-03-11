#Vamos a crear un programa que pregunte un usuario por las ventas 

import pandas as pd 

inicio=int(input('Introduce el año inicial de ventas: '))

fin=int(input('Introduce el año final de ventas: '))
ventas={}
for i in range(inicio, fin+1):
    ventas[i]=float(input('Introduce las ventas del año '+str(i) + ': '))
    
ventas=pd.Series(ventas)
print('Ventas \n ', ventas*0.9)