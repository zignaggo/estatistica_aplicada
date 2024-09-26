import scipy.stats
import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

IRIS = pd.read_csv('./data/iris.csv')
STOCK = pd.read_csv('./data/stock_data.csv')
LIMIT = 0.05


def get_unique_column_values(column):
    return pd.unique(IRIS[column]).tolist()


def get_data_by_specie(index):
    species = get_unique_column_values('Species')
    filtered_csv = pd.DataFrame(IRIS.loc[IRIS['Species'] == species[index]])
    return filtered_csv


def get_species_means():
    means = []
    species = get_unique_column_values('Species')
    for index, specie in enumerate(species):
        petal_length_cm = get_data_by_specie(index)['PetalLengthCm'].tolist()
        mean = np.array(petal_length_cm).mean()
        means.append([specie, mean])
    return means


def get_statistics(data):
    mean = data.mean()
    median = np.median(data)
    std = data.std(ddof=1)
    quartile = np.percentile(data, [25, 50, 75])
    variance = data.var(ddof=1)
    mode = st.mode(data)
    return {
        'max': data.max(),
        'min': data.min(),
        'mean': mean,
        'median': median,
        'deviation': std,
        'quartiles': quartile,
        'variance': variance,
        'mode': mode,
    }


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
def dispersal_length(index=0):
    species = get_unique_column_values('Species')
    print(f"{species[index]}")
    info = get_data_by_specie(index)
    sepal = info['SepalLengthCm']
    petal = info['PetalLengthCm']

    p_value_sepal = scipy.stats.shapiro(sepal).pvalue
    p_value_petal = scipy.stats.shapiro(petal).pvalue
    dispersal_index = None

    print("Pvalue sepal: ", p_value_sepal)
    print("Pvalue petal: ", p_value_petal)

    if p_value_sepal < LIMIT or p_value_petal < LIMIT:
        print('Esse gráfico é assimétrico')
        dispersal_index = scipy.stats.spearmanr(sepal, petal)
    else:
        print('Esse pode ser simétrico')
        # se pelo menos um dos dados for assimetrico será utilizado o spearmanr
        dispersal_index = scipy.stats.pearsonr(sepal, petal)

    # mais próximo do 0 --> mais disperso --> menor correlacao --> colunas mais independentes
    # Mais proximo do 1 --> menos disperso --> maior correlacao -->
    print('Indice de dispersão da correlação dos dados: ',
          dispersal_index.statistic)
    print(30*'-'+'\n')
    min_value = petal.min()
    max_value = petal.max()
    print(f"Valor mínimo: {min_value}, Valor máximo: {max_value}")
    sns.scatterplot(data=IRIS, x=sepal, y=petal)
    plt.show()


def show_hist_boxsplot(index=0, boxsplot=False, petal=True):
    species = get_unique_column_values('Species')
    print(f"{species[index]}")
    info = get_data_by_specie(index)
    petal_sepal = info['PetalLengthCm'] if petal else info['SepalLengthCm']
    bin_value = math.ceil(
        math.log2(len(petal_sepal)) + 1)
    min_value = math.ceil(petal_sepal.min())
    max_value = math.ceil(petal_sepal.max())
    if boxsplot:
        sns.boxplot(petal_sepal)
    else:
        plt.hist(petal_sepal, (bin_value), (min_value, max_value))
    plt.show()


# Setosa = 0
# Versicolor = 1
# Virginica = 2

# dispersal_length(0)
# dispersal_length(1)
# dispersal_length(2)

# 3) Qual a distribuição das espécies no banco de dados
def show_column_info(database: pd.DataFrame, colum_names: list[str]):
    column_values = []
    _, graficos = plt.subplots(nrows=2, ncols=4)
    plt.tight_layout()
    for i, column in enumerate(colum_names):
        column_statisticts = get_statistics(database[column])
        quartiles = column_statisticts['quartiles']
        median = column_statisticts['median']
        mean = column_statisticts['mean']
        mode = column_statisticts['mode']
        deviation = column_statisticts['deviation']

        column_value = database[column].values
        column_values.append(column_value)
        inf, sup = mean - deviation * 3, mean + deviation * 3
        outliers = list(
            database[column][(column_value < inf) | (column_value > sup)])

        print(f"Coluna {column}")
        print(f"Média: {mean:.2f} cm")
        print(f"Moda: {mode} cm")
        print(f"Mediana: {median} cm")
        print(f"Desvio padrão: {deviation:.2f} cm")
        print(f"Amplitude interquartil: {
              quartiles[2] - quartiles[0]:.2f} cm")
        print(f"outliers ({len(outliers)}): {outliers} cm")
        print("-" * 40)
        print("\n")
        # bin_value = math.ceil(
        #     math.log2(len(database[column])) + 1)
        # sns.histplot(database[column], bins=bin_value, ax=graficos[0][i])
        sns.boxplot(database[column], ax=graficos[0][i], orient='x')
    plt.show()


setosa_data = get_data_by_specie(0)
versicolor_data = get_data_by_specie(1)
virginica_data = get_data_by_specie(2)
# Dados da Iris-Setosa
# show_column_info(
#     setosa_data, ["SepalLengthCm", "SepalWidthCm",
#                   "PetalLengthCm", "PetalWidthCm"])

# Dados da Iris-Versicolor
# show_column_info(
#     versicolor_data, ["SepalLengthCm", "SepalWidthCm",
#                   "PetalLengthCm", "PetalWidthCm"])

# Dados da Iris-Virginica
show_column_info(
    virginica_data, ["SepalLengthCm", "SepalWidthCm",
                  "PetalLengthCm", "PetalWidthCm"])