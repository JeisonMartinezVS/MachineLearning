import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns
import os

x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10, dtype=int)

#La funcion "linspace" genera una Array formado por N numeros equiespaciados entre dos dados
# Sintaxis np.linspace(valor-inicial, valor-final, numero de valores)

#Se crea un diccionario
d = {"x": x, "y": y}

#Convertimos el diccionario en un dataframe
df = pd.DataFrame(d)

#Imprimimos el Dataframe creado del diccionario Y
# print(df.y)

#__________________________________________________________#

"""
📌 Metodos para leer un DataFrame
Método            | Explicación
----------------- | ----------------------------------------------------------------------
read_csv         | Lee un archivo CSV (valores separados por comas) y lo convierte en un DataFrame.
read_excel       | Lee un archivo Excel y lo convierte en un DataFrame.
read_sql         | Lee una consulta SQL y la ejecuta en una base de datos, devolviendo el resultado como un DataFrame.
read_json        | Lee un archivo JSON (JavaScript Object Notation) y lo convierte en un DataFrame.
read_html        | Lee todas las tablas HTML contenidas en una página web o en un archivo HTML y las convierte en una lista de DataFrames.
read_parquet     | Lee un archivo Parquet, un formato binario para almacenar datos tabulares, y lo convierte en un DataFrame.
read_feather     | Lee un archivo Feather, un formato binario para almacenar datos tabulares, y lo convierte en un DataFrame.
read_hdf         | Lee un archivo HDF5 (Hierarchical Data Format), un formato para almacenar datos científicos, y lo convierte en un DataFrame.
read_clipboard   | Lee el contenido del portapapeles y lo convierte en un DataFrame.

"""

#Este metodo devuelve el directorio de trabajo actual
path = os.getcwd()
# print("El directorio actual de este trabajo es: ", path)

path = "https://github.com/hernansalinas/Curso_aprendizaje_estadistico/blob/main/datasets/sesion_01b_country_vaccinations.xlsx?raw=true"

#Se importa esta libreria para poder leer elementos de excel .xlsx
import openpyxl

df = pd.read_excel(path)

# print(df)

"""
📌 Comandos básicos para describir un DataFrame

| Comando            | Explicación |
|--------------------|------------------------------------------------------------------|
| `df.head()`       | Muestra las primeras 5 filas del DataFrame. Se puede pasar un número para especificar cuántas filas mostrar. |
| `df.tail()`       | Muestra las últimas 5 filas del DataFrame. También permite especificar el número de filas. |
| `df.describe()`   | Genera un resumen estadístico con métricas como media, desviación estándar, mínimo y máximo para columnas numéricas. |
| `df.info()`       | Muestra información general del DataFrame, incluyendo el número de filas y columnas, tipos de datos y valores nulos. |
| `df.shape`        | Devuelve una tupla con el número de filas y columnas del DataFrame. |
| `df.columns`      | Devuelve un objeto con los nombres de las columnas del DataFrame. |
| `df.index`        | Devuelve un objeto con los índices de las filas del DataFrame. |
| `df.dtypes`       | Muestra el tipo de datos de cada columna. |
| `df.memory_usage()` | Devuelve el uso de memoria en bytes para cada columna del DataFrame. |
"""

#print(df.memory_usage())

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSHCOR8_Ha6TvBQwIcpjvJ0bzHYel1S8DXl4NHnMhVvdbibrgL_SP6rffuESpaJvPwLuUizXblQtHox/pub?output=csv"
df = pd.read_csv(url)
# print(df)

#Asignacion a la columna index la columna date
df = pd.read_csv(url, index_col="date")

#Convertimos los valores de la columna date a tipo datetime64 asegurandonos que sea un formato fecha
df.index = pd.to_datetime(df.index)


#Renombar columnas
df1 = df.rename(columns={"location": "Locacion",
                         "vaccine": " Vacuna ",
                         "total_vaccinations": "Total de vacunaciones"} ).copy()

df1 = df
#Inicializando el indice a valores enteros
new_df = df1.reset_index()

#Convirtiendo a minusculas todas las columnas
df1.columns #Tomamos las columnas del DataFrame

new_df = df1.rename(mapper = str.lower, axis="columns")

"""
.rename() -> Permite cambiar los nombres de las columnas o filas de un dataframe
mapper -> Argumento que define como se va a transformar los nombres
str.lower -> Convierte todas las letras de los nombres de las columnas a minusculas
axis="columns" -> Indica que las transformacion se aplicara a nombres de las columnas
"""

new_df2 = new_df.rename(mapper= str.strip, axis="columns")

#Ejercicio: Construir un cóidigo que cambie el nombre de las columnas a Camel Case

cols_camelCase = [''.join([x if i == 0 else x.title() for i,x in enumerate(col.split("_"))]) for col in df.columns]
df1.columns = cols_camelCase

#Unimos las palabras en un solo string sin espacios, la primera palabra la dejamos igual, la segunda la convertimos en Title Case, recoremos las lista y dividimos las palabras que tienen '_', y por ultimo recorremos todas las columnas

print(df1.columns)


# dfp = sns.load_dataset('penguins')
# print(dfp)