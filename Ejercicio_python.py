#Obtener Media, mediana, moda, rango, varianza,
# desviasion estandar con su tabla de 
# frecuencias del archivo housing, deberan de 
# mostrarse en un formato de tablas separado 
# con sus elementos solicitados.

import pandas as pd 

#media
df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media= df["median_house_value"].mean()
mediana=df["median_house_value"].median()
moda=df["median_house_value"].mode()
desviacionEstandar=df


print("Media", media)
print("Mediana", mediana)
print("Moda", moda)
