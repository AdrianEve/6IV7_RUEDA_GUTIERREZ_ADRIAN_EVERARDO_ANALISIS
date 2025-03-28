import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt

#Conocer ventas totales del comercio
df_ventas = pd.read_excel('C:/Users/Alumno/Desktop/6IV7_RUEDA_GUTIERREZ_ADRIAN_EVERARDO_ANALISIS-main/EstadisticaDescriptiva/proyecto1.xlsx')
ventas_totales=df_ventas['ventas_tot'].sum()

print("Ventas totales: ",ventas_totales)

#Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
Adeudos=df_ventas['B_adeudo'].value_counts()
print('Adeudos: ', Adeudos.get('Con adeudo', 0) )
print('Sin adeudos: ', Adeudos.get('Sin adeudo', 0))


#Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 
#Reparar el pequeño error
df_ventas['B_mes'] = pd.to_datetime(df_ventas['B_mes']) 

ventas_tot = df_ventas['ventas_tot']
B_mes = df_ventas['B_mes']

plt.figure(figsize=(12, 6))

plt.bar(B_mes, ventas_tot, color='blue', width=9)

plt.gca().xaxis.set_major_formatter(dt.DateFormatter('%Y-%m-%d')) 
plt.gca().xaxis.set_major_locator(dt.AutoDateLocator()) 

plt.title('Ventas totales respecto del tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Ventas totales')
plt.show()


#Grafica donde se pueda visualizar la desviación estándar de los pagos 
#realizados del comercio respecto del tiempo

df_sucursal = pd.read_excel('C:/Users/Alumno/Desktop/6IV7_RUEDA_GUTIERREZ_ADRIAN_EVERARDO_ANALISIS-main/EstadisticaDescriptiva/Catalogo_sucursal.xlsx')

df_ventas['B_mes'] = pd.to_datetime(df_ventas['B_mes'], format='%Y-%m')  

df_merged = df_ventas.merge(df_sucursal, on='id_sucursal', how='left')

#Desviacion Estandar
df_std = df_merged.groupby(['B_mes', 'suc'])['pagos_tot'].std().reset_index()

plt.figure(figsize=(12, 6))

# Graficar cada sucursal
colors = [
    '#FF5733',  # Vibrant Red-Orange
    '#FF8D1A',  # Bright Orange
    '#FFC300',  # Golden Yellow
    '#FFEB3B',  # Bright Yellow
    '#33FF57',  # Bright Green
    '#4CAF50',  # Medium Green
    '#00FF7F',  # Spring Green
    '#00FFFF',  # Aqua
    '#1E88E5',  # Bright Blue
    '#2196F3',  # Vibrant Blue
    '#03A9F4',  # Light Blue
    '#673AB7',  # Deep Purple
    '#9C27B0',  # Bright Purple
    '#E91E63',  # Pink
    '#F06292',  # Light Pink
    '#FF4081',  # Hot Pink
    '#FF1744',  # Red
    '#D32F2F',  # Red
    '#0288D1',  # Blue
    '#8BC34A',  # Light Green
    '#CDDC39',  # Lime Green
    '#FF9800',  # Orange
    '#FF5722',  # Deep Orange
    '#795548',  # Brown
    '#9E9E9E',  # Grey
    '#607D8B',  # Blue Grey
    '#512DA8',  # Purple
    '#AB47BC',  # Medium Purple
    '#0D47A1',  # Dark Blue
    '#0288D1',  # Sky Blue
    '#F44336',  # Red
    '#00BCD4',  # Light Cyan
    '#FF4081',  # Bright Pink
    '#8E24AA',  # Bright Purple
    '#FFEB3B',  # Yellow
    '#FF9800',  # Orange
    ]  

for i, sucursal in enumerate(df_std['suc'].unique()):
    sucursal_data = df_std[df_std['suc'] == sucursal]
    plt.bar(sucursal_data['B_mes'], sucursal_data['pagos_tot'], label=sucursal, width=20, color=colors[i])
    
plt.title('Desviación estándar de los pagos realizados')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar de Pagos Totales')
plt.legend(title='Sucursal')
plt.show()

#Cuanto es la deuda total de los clientes
deuda1 = 'B_adeudo'  
columna_id = 'id_sucursal' 
con_adeudo_data = df_ventas[df_ventas[deuda1] == 'Con adeudo']
total_deudas = con_adeudo_data['adeudo_actual'].sum()

print("Deuda total de los clientes: ",total_deudas )

