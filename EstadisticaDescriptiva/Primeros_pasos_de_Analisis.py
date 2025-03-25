import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

#Conocer ventas totales del comercio
df_ventas = pd.read_excel('C:/Users/Alumno/Desktop/6IV7_RUEDA_GUTIERREZ_ADRIAN_EVERARDO_ANALISIS-main/EstadisticaDescriptiva/proyecto1.xlsx')
ventas_totales=df_ventas['ventas_tot'].sum()

print("Ventas totales: ",ventas_totales)

#Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
Adeudos=df_ventas['B_adeudo'].value_counts()
print('Adeudos: ', Adeudos.get('Con adeudo', 0) )
print('Sin adeudos: ', Adeudos.get('Sin adeudo', 0))

#Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 

ventas_por_fecha = df_ventas.groupby["ventas_tot"].sum()
plt.figure(figsize=(12, 6))
ventas_por_fecha.plot(kind="bar", color="skyblue", edgecolor="black")