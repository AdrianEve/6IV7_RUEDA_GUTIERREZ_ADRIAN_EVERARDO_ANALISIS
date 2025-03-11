import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

print(df.head())


print(df.tail())

print(df.iloc[7])

print(df["ocean_proximity"])

mediacuartos=df["total_rooms"].mean()

medianapopularidad=df["population"].mean()

print('Media de los cuartos: ', mediacuartos)

print('Mediana de popularidad: ', medianapopularidad)

std_age = df["housing_median_age"].std()
print('Desviacion Estandar en años: ', std_age)

filtrodelooceano= df[df["ocean_proximity"] == "ISLAND"]

print("Filtro de proximidad del oceano: ", filtrodelooceano)

#crear grafico

plt.scatter(df["ocean_proximity"][:10], df["housing_median_age"][:10], )

#definir x y
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de dispersion de proximidad al oceno vs precio')
plt.show()