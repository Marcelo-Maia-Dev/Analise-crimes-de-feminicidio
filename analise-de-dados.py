# Desafio 

# Ver o que tem na base de dados

# Importando bibliotecas e lendo o arquivo em csv
import pandas as pd  
import numpy as np
import matplotlib.piplot as plt
import seaborn as sns


df = pd.read_excel("Feminicidio_2015_2022.xlsx")

print(df)

# Panorama geral da base de dados
total_morte = pd[df].groupby("MUNICIPIO_CIRCUNSCRICAO").sum()

# Começar a analise top => down 


# Entrar no detalhe para entender
