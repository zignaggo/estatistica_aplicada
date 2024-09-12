import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data
iris = pd.read_csv('./data/iris.csv')
stock = pd.read_csv('./data/stock_data.csv')



def getCsvStatistics(csv: pd.DataFrame, csv_name: str, ignored_columns: list):
    print('CSV: ', csv_name)
    print(20*'-')
    boxplot_values = []
    xticks_index = []
    columns_names = []
    for index, column in enumerate(csv.columns.values):
        if not column in ignored_columns:
            column_data = np.array(csv[column].tolist())
            boxplot_values.append(column_data)
            xticks_index.append(index-1)
            columns_names.append(column)

            # showing values
            print(f'Column: {column}')
            print(f"Média: {column_data.mean():.2f}")
            print(f"Mediana: {np.median(column_data):.2f}")
            print(f"Desvio padrão: {column_data.std(ddof=1):.2f}")
            print('_'*20)
            break

    sns.boxplot(boxplot_values)
    print(xticks_index, columns_names)
    plt.xticks(xticks_index, columns_names)
    plt.show()
    print('\n')


getCsvStatistics(iris, 'Iris', ['Id', 'Species'])
getCsvStatistics(stock, 'Stock', ['Date',  'Name'])
