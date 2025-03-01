import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Problema: Dataset de pinguinos

df = sns.load_dataset('penguins')
print(df)

"""
1. ¿Cuántas especies diferentes de pingüinos hay en el dataset?

2. ¿Cuál es la longitud media del pico de los pingüinos de la especie Adelie?

3. ¿Cuál es la masa corporal promedio de los pingüinos de la especie Gentoo?

4. ¿Cuál es la relación entre la longitud del pico y la masa corporal de los pingüinos?

5. ¿Cuál es la isla con mayor número de pingüinos en el dataset?

6. ¿Cuál es la desviación estándar de la longitud de la aleta de los pingüinos de la especie Chinstrap?

7. ¿Qué pingüino tiene el pico más largo en el dataset y cuál es su especie?

8. ¿Cuál es la proporción de machos y hembras en la especie Adelie?

9. ¿Existe una correlación significativa entre la longitud del pico y la masa corporal en las diferentes especies de pingüinos?

10. ¿Cuál es la distribución de la masa corporal entre las especies de pingüinos?

11. ¿Cuál es la longitud mínima y máxima de la aleta entre las tres especies de pingüinos?

12. ¿Cuántos pingüinos tienen una masa corporal superior a 5000 gramos?

13. ¿Cómo varía la longitud del pico entre las diferentes especies de pingüinos en las distintas islas?

14. ¿Cuál es la relación entre la longitud de la aleta y la masa corporal en los pingüinos de la especie Gentoo?

15. ¿Cuántos pingüinos tienen datos faltantes en alguna de sus características?

16. ¿Cuál es la isla con la mayor variación en la longitud del pico entre las tres especies de pingüinos?

17. ¿Cuál es la diferencia en masa corporal promedio entre machos y hembras de la especie Chinstrap?

18. ¿Qué especie de pingüino tiene la longitud de aleta promedio más alta?

19. ¿Cuál es la longitud del pico más pequeña registrada en el dataset y de qué especie es?

20. ¿Cuál es la relación entre el sexo y la longitud de la aleta en los pingüinos de la especie Adelie?
"""

# 1. ¿Cuántas especies diferentes de pingüinos hay en el dataset?
total_species = df['species'].nunique()
print('1. Cantidad de especies diferentes R/',total_species)

# 2. ¿Cuál es la longitud media del pico de los pingüinos de la especie Adelie?
adelie = df[df['species'] == 'Adelie']
length_bill = adelie['bill_length_mm'].mean()
print('2. longitud media del pico de los pingüinos de la especie Adelie R/', length_bill)

# 3. ¿Cuál es la masa corporal promedio de los pingüinos de la especie Gentoo?
gentoo = df[df['species'] == 'Gentoo']
body_mass = gentoo['body_mass_g'].mean()
print('3. Masa corporal promedio de los pingüinos de la especie Gentoo R/', body_mass)

# 4. ¿Cuál es la relación entre la longitud del pico y la masa corporal de los pingüinos?
relationPenguis = df['bill_length_mm'].corr(df['body_mass_g'])
print('4. Correlación entre la longitud del pico y la masa corporal R/', relationPenguis)

# 5. ¿Cuál es la isla con mayor número de pingüinos en el dataset?
island = df['island'].value_counts().idxmax()
print('5. Isla con mayor número de pingüinos R/', island)

# 6. ¿Cuál es la desviación estándar de la longitud de la aleta de los pingüinos de la especie Chinstrap?
chinstrap = df[df['species'] == 'Chinstrap']
std_flippers = chinstrap['flipper_length_mm'].std()
print('6. Desviación estándar de la longitud de la aleta de los pingüinos de la especie Chinstrap R/', std_flippers)

# 7. ¿Qué pingüino tiene el pico más largo en el dataset y cuál es su especie?
penguinBillMax = df['bill_length_mm'].idxmax()
penguinBillMax = df.loc[penguinBillMax]
print('7. Pingüino con el pico más largo en el dataset R/', penguinBillMax['species'], 'Con un tamaño de:', penguinBillMax['bill_length_mm'])

# 8. ¿Cuál es la proporción de machos y hembras en la especie Adelie?
adelie = df[df['species'] == 'Adelie']
sexAdelie = adelie['sex'].value_counts(normalize=True)
print('8. Proporción de machos y hembras en la especie Adelie R/', sexAdelie)

# 9. ¿Existe una correlación significativa entre la longitud del pico y la masa corporal en las diferentes especies de pingüinos?


# 10. ¿Cuál es la distribución de la masa corporal entre las especies de pingüinos?
# 11. ¿Cuál es la longitud mínima y máxima de la aleta entre las tres especies de pingüinos?
# 12. ¿Cuántos pingüinos tienen una masa corporal superior a 5000 gramos?
# 13. ¿Cómo varía la longitud del pico entre las diferentes especies de pingüinos en las distintas islas?
# 14. ¿Cuál es la relación entre la longitud de la aleta y la masa corporal en los pingüinos de la especie Gentoo?
# 15. ¿Cuántos pingüinos tienen datos faltantes en alguna de sus características?
# 16. ¿Cuál es la isla con la mayor variación en la longitud del pico entre las tres especies de pingüinos?
# 17. ¿Cuál es la diferencia en masa corporal promedio entre machos y hembras de la especie Chinstrap?
# 18. ¿Qué especie de pingüino tiene la longitud de aleta promedio más alta?
# 19. ¿Cuál es la longitud del pico más pequeña registrada en el dataset y de qué especie es?
# 20. ¿Cuál es la relación entre el sexo y la longitud de la aleta en los pingüinos de la especie Adelie?