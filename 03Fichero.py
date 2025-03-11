#vAMOS A HACER UN EJEMPLO DE CARFA DE ARCGIVO Y APKICAR MIN, MAX, MEDIA, DESCIACION ENTANDAR

import pandas as pd
def cotizacion(fichero):
    df=pd.read_csv(fichero,sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], index=['Minimo', 'Maximo', 'Media', 'desviacion estandar'])

print(cotizacion('./EstadisticaDescriptiva/cotizacion.csv'))