import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("coaster_db.csv")
datos = df
datos.head() # Primeros 5
datos.tail() # Ultimos 5
datos.columns # Muestra los nombre de las columnas
datos.dtypes # Muestra los tipos de datos de la coluna
datos.describe() # Muestra las estadisticas descriptivas de todas las columnas que tiene Int o Float
longitud = datos['longitude'].describe()
promedio = datos['longitude'].mean()
print(promedio)

#_____________________________________________________
