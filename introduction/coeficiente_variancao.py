import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from main import sync1, asyncr1


print("-----DATA-----")
print("Média: ", sync1.mean())
print(f'mediana 1: {np.median(sync1)}')

print("-----DATA_2-----")
print("Média 2: ", asyncr1.mean())
print(f'mediana 2: {np.median(asyncr1)}')
# bins o numero para dividir o intervalo, grpos de quanto
# # range > minimo e máximo = diferença => multiplo do bin
# plt.hist(sync1, 5, (65, 95))
# plt.show()



# Distribuição assimetrica a direita
# Nesse caso a média vai ser maior que a mediana
# O valor da média é arrastado pela cauda, nesse caso, valores a direita, maiores valores, maior média
# plt.hist(asyncr1, 5, (65, 95))
# plt.show()


# Distribuição assimetrica a esquerda
# A média ficará menor que a mediana
# O valor da média é arrastado pela cauda, nesse caso, valores a esquerda, menores valores, menor média


# 1.5
sns.boxplot([sync1, asyncr1])
plt.xticks([0, 1], ['Sync', 'Async'])
plt.show()
