import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as NDates
import scipy.stats
import threading


# Data
IRIS = pd.read_csv('./data/iris.csv')
STOCK = pd.read_csv('./data/stock_data.csv')
STOCK_NEW_DATE = STOCK.copy()
STOCK_NEW_DATE['Date'] = pd.to_datetime(STOCK_NEW_DATE['Date'])

def show_dict_values(data: dict):
    for key in data:
        print(f"{key}: {data[key]}")


def get_column_values(csv: pd.DataFrame, column: str):
    if not column in csv.columns.values:
        return None
    return np.array(csv[column].tolist())


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
        'media': mean,
        'mediana': median,
        'desvio_padrao': std,
        'quartis': quartile,
        'varianca': variance,
        'moda': mode,
    }


def show_column_stats(csv: pd.DataFrame, column: str):
    column_data = get_column_values(csv, column)
    if column_data is None:
        return
    statistics = get_statistics(column_data)
    print(column)
    show_dict_values(statistics)
    # box
    sns.boxplot(column_data)
    plt.xticks([0], [column])
    plt.show()


def show_csv_statistics(csv: pd.DataFrame, csv_name: str, ignored_columns: list):
    print('CSV: ', csv_name)
    print(20*'-')
    boxplot_values = []
    xticks_index = []
    columns_names = []
    for index, column in enumerate(csv.columns.values):
        if not column in ignored_columns:
            column_data = get_column_values(csv, column)
            boxplot_values.append(column_data)
            xticks_index.append(index-1)
            columns_names.append(column)
            stats = get_statistics(column_data)
            # showing values
            print(column)
            show_dict_values(stats)
            print('_'*20, '\n')

    sns.boxplot(boxplot_values)
    plt.xticks(xticks_index, columns_names)
    plt.show()
    print('\n')


# show_csv_statistics(IRIS, 'Iris', ['Id', 'Species'])
# show_csv_statistics(STOCK, 'Stock', ['Date',  'Name'])
# print(STOCK.head())
# showColumnStats(IRIS, 'SepalWidthCm')

# IRIS SepalLengthCm HIST
# column_data = get_column_values(IRIS,  'SepalLengthCm')
# plt.hist(column_data, 8, (4, 8))
# plt.show()

# STOCK High HIST
# showColumnStats(STOCK, 'High')
# column_data_value = get_column_values(STOCK,  'High')
# plt.hist(column_data_value, 5, (10, 70))
# plt.show()

# Time series
# Gráfico em função do tempo
# sns.lineplot(data=STOCK_NEW_DATE, x="Date", y="Open")
# sns.lineplot(data=STOCK_NEW_DATE, x="Date", y="Close")
# sns.lineplot(data=STOCK_NEW_DATE, x="Date", y="High")
# sns.lineplot(data=STOCK_NEW_DATE, x="Date", y="Low")
# plt.show()

# # Gráfico de dispersão
# x = IRIS['SepalLengthCm']
# y = IRIS['SepalWidthCm']

# # Distribuição assimétrica
# nesse caso é o statistics
# print(scipy.stats.spearmanr(x, y))


# # Distribuição Normal 
# # Teste paramétrico utiliza a média como comparação
# # scipy.stats.pearsonr(x, y)
# sns.scatterplot(x=x, y=y)
# plt.show()



# Gráfico de dispersão
# species = pd.unique(IRIS['Species']).tolist()
#     for specie in species:
#         print(f'Species == {specie}')
        
#         filtered_csv = IRIS.loc[IRIS['Species'] == specie]
#         x = filtered_csv['SepalLengthCm']
#         y = filtered_csv['SepalWidthCm']
        
#         scipy.stats.spearmanr(x, y)
#         sns.scatterplot(x=x, y=y)
        
#         plt.show()
    

# def show_graph(index):
#     species = pd.unique(IRIS['Species']).tolist()
#     print(f'Species == {species[index]}')
    
#     filtered_csv = IRIS.loc[IRIS['Species'] == species[index]]
#     x = filtered_csv['SepalLengthCm']
#     y = filtered_csv['SepalWidthCm']

#     Dispersão
#     scipy.stats.spearmanr(x, y)
#     sns.scatterplot(x=x, y=y)
    
#     plt.show()


# show_graph(0)
    

def getSpeciesInfo(index):
    species = pd.unique(IRIS['Species']).tolist()
    print(f'Species == {species[index]}')

    filtered_csv = IRIS.loc[IRIS['Species'] == species[index]]
    x = filtered_csv['SepalLengthCm']
    y = filtered_csv['SepalWidthCm']
