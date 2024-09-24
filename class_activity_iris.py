import scipy.stats
import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


IRIS = pd.read_csv('./data/iris.csv')
STOCK = pd.read_csv('./data/stock_data.csv')
LIMIT = 0.05


def get_unique_column_values(column):
    return pd.unique(IRIS[column]).tolist()


def get_species_info(index):
    species = get_unique_column_values('Species')
    filtered_csv = pd.DataFrame(IRIS.loc[IRIS['Species'] == species[index]])
    return filtered_csv


def get_species_means():
    means = []
    species = get_unique_column_values('Species')
    for index, specie in enumerate(species):
        petal_length_cm = get_species_info(index)['PetalLengthCm'].tolist()
        mean = np.array(petal_length_cm).mean()
        means.append([specie, mean])
    return means


# 1) Qual espécie de íris (Setosaa, Versicolor, Virginica) tem maior média comprimento de pétala:
"""
species_means = get_species_means()
for specie_mean in species_means:
    print(f"{specie_mean[0]}: {specie_mean[1]:.2f} cm")
"""
"""
Result
Iris-setosa: 1.46 cm
Iris-versicolor: 4.26 cm
Iris-virginica: 5.55 cm

Virginica é 30% maior em média de comprimento da pétala do que a Versicolor.
Virginica é quase 4 vezes maior que a média do comprimento da pétala de Setosa.
Versicolor é quase 3 vezes maior que a média do comprimento da pétala de Setosa.
"""


# 2) Qual a correlação entre o comprimento da sépala e comprimento da pétala?
def dispersal_length():
    species = get_unique_column_values('Species')
    for index, specie in enumerate(species):
        print(f"{specie}")
        info = get_species_info(index)
        sepal = info['SepalLengthCm']
        petal = info['PetalLengthCm']

        p_value_sepal = scipy.stats.shapiro(sepal).pvalue
        p_value_petal = scipy.stats.shapiro(petal).pvalue
        dispersal_index = 0

        print("Pvalue sepal: ", p_value_sepal)
        print("Pvalue petal: ", p_value_petal)

        if p_value_sepal < LIMIT or p_value_petal < LIMIT:
            print('Esse gráfico é assimétrico')
            dispersal_index = scipy.stats.spearmanr(sepal, petal)
        else:
            print('Esse pode ser simétrico')
            # se pelo menos um dos dados for assimetrico será utilizado o spearmanr
            dispersal_index =  scipy.stats.pearsonr(sepal, petal)

        # mais próximo do 0 --> mais disperso --> menor correlacao --> colunas mais independentes
        # Mais proximo do 1 --> menos disperso --> maior correlacao -->
        print('Indice de dispersão da correlação dos dados: ', dispersal_index.statistic)
        print(30*'-'+'\n')
        sns.scatterplot(data=IRIS, x=sepal, y=petal)
        plt.show()

dispersal_length()
