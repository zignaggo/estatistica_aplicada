import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Data
IRIS = pd.read_csv('./data/iris.csv')
STOCK = pd.read_csv('./data/stock_data.csv')


def showDictValues(data: dict):
    for key in data:
        print(f"{key}: {data[key]}")


def getColumnValues(csv: pd.DataFrame, column: str):
    if not column in csv.columns.values:
        return None
    return np.array(csv[column].tolist())


def getStatistics(data):
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


def showColumnStats(csv: pd.DataFrame, column: str):
    column_data = getColumnValues(csv, column)
    if column_data is None:
        return
    statistics = getStatistics(column_data)
    print(column)
    showDictValues(statistics)
    # box
    sns.boxplot(column_data)
    plt.xticks([0], [column])
    plt.show()


def showCsvStatistics(csv: pd.DataFrame, csv_name: str, ignored_columns: list):
    print('CSV: ', csv_name)
    print(20*'-')
    boxplot_values = []
    xticks_index = []
    columns_names = []
    for index, column in enumerate(csv.columns.values):
        if not column in ignored_columns:
            column_data = csv[column].tolist()
            boxplot_values.append(column_data)
            xticks_index.append(index-1)
            columns_names.append(column)
            stats = getStatistics(column_data)
            # showing values
            print(column)
            showDictValues(stats)
            print('_'*20, '\n')

    sns.boxplot(boxplot_values)
    plt.xticks(xticks_index, columns_names)
    plt.show()
    print('\n')


# showCsvStatistics(IRIS, 'Iris', ['Id', 'Species'])
# showCsvStatistics(STOCK, 'Stock', ['Date',  'Name'])
# showColumnStats(IRIS, 'SepalWidthCm')

# IRIS SepalLengthCm HIST
# column_data = getColumnValues(IRIS,  'SepalLengthCm')
# plt.hist(column_data, 8, (4, 8))
# plt.show()


# STOCK High HIST
# showColumnStats(STOCK, 'High')
# column_data_value = getColumnValues(STOCK,  'High')
# plt.hist(column_data_value, 5, (10, 70))
# plt.show()