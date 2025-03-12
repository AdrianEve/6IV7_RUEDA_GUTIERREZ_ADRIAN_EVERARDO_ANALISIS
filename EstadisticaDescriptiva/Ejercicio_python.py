#Obtener Media, mediana, moda, rango, varianza,
# desviasion estandar con su tabla de 
# frecuencias del archivo housing, deberan de 
# mostrarse en un formato de tablas separado 
# con sus elementos solicitados.

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#media
df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media= df["median_house_value"].mean()
mediana=df["median_house_value"].median()
moda=df["median_house_value"].mode()
desviacionEstandar=df["median_house_value"].std()
varianza=df["median_house_value"].var()
rango=df["median_house_value"].max() - df["median_house_value"].min()

df['median_house_value_vs_population'] = df['median_house_value'] / df['population']
plt.figure(figsize=(10, 6))
sns.barplot(x='median_house_value', y='population', data=df, color='blue', label="Median House Value vs Population")
# Añadir etiquetas y título
plt.xlabel('Median House Value')
plt.ylabel('Population')
plt.title('Comparación de Median House Value con Population y su Promedio')
plt.legend()

# Mostrar el gráfico
plt.show()

print("Media", media)
print("Mediana", mediana)
print("Moda", moda)
print("Varianza", varianza)
print("Rango", rango)
print("desviacion estandar", desviacionEstandar)


#df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')