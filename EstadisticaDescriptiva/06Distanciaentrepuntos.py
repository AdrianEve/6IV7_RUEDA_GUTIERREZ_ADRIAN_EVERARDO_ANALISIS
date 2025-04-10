import pandas as pd
from scipy.spatial import distance

# Definimos las coordenadas de los puntos
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertimos las coordenadas en un DataFrame para facilitar el cálculo
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']

# Inicializamos los DataFrame para los resultados de distancias
distancias_euclidiana = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_manhattan = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_chebyshev = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

# Calculamos las distancias
for i in df_puntos.index:
    for j in df_puntos.index:
        # Distancia Euclidiana
        distancias_euclidiana.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        
        # Distancia Manhattan
        distancias_manhattan.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        
        # Distancia Chebyshev
        distancias_chebyshev.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostrar los resultados
print('Distancia Euclidiana entre los puntos:')
print(distancias_euclidiana)

print('\nDistancia Manhattan entre los puntos:')
print(distancias_manhattan)

print('\nDistancia Chebyshev entre los puntos:')
print(distancias_chebyshev)

# Determinamos los puntos más cercanos y más alejados para cada tipo de distancia

# Función para encontrar el punto más cercano y más alejado
def obtener_extremos(distancias):
    distancias_unstack = distancias.unstack()
    distancias_unstack = distancias_unstack[distancias_unstack != 0]  # Eliminamos las distancias a sí mismos
    min_distancia = distancias_unstack.idxmin()
    max_distancia = distancias_unstack.idxmax()
    return min_distancia, distancias_unstack[min_distancia], max_distancia, distancias_unstack[max_distancia]

# Obtener los extremos para cada tipo de distancia
min_euclidiana, dist_min_euclidiana, max_euclidiana, dist_max_euclidiana = obtener_extremos(distancias_euclidiana)
min_manhattan, dist_min_manhattan, max_manhattan, dist_max_manhattan = obtener_extremos(distancias_manhattan)
min_chebyshev, dist_min_chebyshev, max_chebyshev, dist_max_chebyshev = obtener_extremos(distancias_chebyshev)

print("\nDistancia más cercana y más lejana en Euclidiana:")
print(f'Más cercana: {min_euclidiana} con distancia {dist_min_euclidiana}')
print(f'Más lejana: {max_euclidiana} con distancia {dist_max_euclidiana}')

print("\nDistancia más cercana y más lejana en Manhattan:")
print(f'Más cercana: {min_manhattan} con distancia {dist_min_manhattan}')
print(f'Más lejana: {max_manhattan} con distancia {dist_max_manhattan}')

print("\nDistancia más cercana y más lejana en Chebyshev:")
print(f'Más cercana: {min_chebyshev} con distancia {dist_min_chebyshev}')
print(f'Más lejana: {max_chebyshev} con distancia {dist_max_chebyshev}')
