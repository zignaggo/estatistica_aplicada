import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats
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
        means.append({specie: np.array(petal_length_cm).mean()})
    return means

# Qual espécie tem maior comprmento de pétala:
# print(get_species_means())
# Colocar a medida: Centimetros

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

#  dispersal_length()
# Pvalue sepal:  0.4595010578632355
# Pvalue petal:  0.054648224264383316
# Esse pode ser simétrico
# Indice de dispersão da correlação dos dados:  0.26387409291868696
# ------------------------------

# Pvalue sepal:  0.4647378921508789
# Pvalue petal:  0.1584763377904892
# Esse pode ser simétrico
# Indice de dispersão da correlação dos dados:  0.7540489585920164
# ------------------------------

# Pvalue sepal:  0.25831347703933716
# Pvalue petal:  0.10977503657341003
# Esse pode ser simétrico
# Indice de dispersão da correlação dos dados:  0.8642247329355762
# ------------------------------