import numpy as np
import scipy.stats as stats

LIMIT = 0.05

sync1 = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]) # 22
asyncr1 = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]) # 14

# Como saber se as médias são diferentes?
# Seguir o passo a passo abaixo


# # Passo 1:
# # Medir a normalidade
# # Rodar teste de normalidade
# normality_sync1 = stats.shapiro(sync1)
# normality_asyncr1 = stats.shapiro(asyncr1)
# if normality_sync1.pvalue < LIMIT:
#     print("rejeitar h0: ", normality_sync1.pvalue)
# else:
#   print("não rejeitar h0: ", normality_sync1.pvalue)
# if normality_asyncr1.pvalue < LIMIT:
#     print("rejeitar h0: ", normality_asyncr1.pvalue)
#  else:
#   print("não rejeitar h0: ", normality_asyncr1.pvalue)



# # Passo 2:
# # Medir a variança
# # Varianças iguais pois o pValue deu 
# _, p_value_var = stats.levene(sync1, asyncr1)
# print(f"Pvalue Teste de levene: {p_value_var}")
# if p_value_var < LIMIT:
#     print("rejeitar h0: ", p_value_var)
# else:
#   print("não rejeitar h0: ", p_value_var)


# Passo 3:
# Teste que necessita de: Normalidade e variança igual
# Verifica se 2 médias são iguais quando as amostras são normais e variança igual
# Pega as 2 médias e compara
# Compara se as médias são iguais

ttest, p_value_ttest = stats.ttest_ind(sync1, asyncr1)
print("p value: ", p_value_ttest)
print("Desde que a hipotese for de um lado >> use p_value / 2 >> p_value")

if p_value_ttest / 2 < LIMIT:
    print("rejeitar h0: ", p_value_ttest)
else:
    print("não rejeitar h0: ", p_value_ttest)

# Médias das populações são diferentes porque o p_value é menor que 0.05, rejeitamos a hipotese nula e assumimos a hipotese alternativa
# Além de o estudo da média sync1 é maior que o asyncr1 


# 2 tipos de testes:
# - One sided -> usar p_value
# - Two sided -> usar p_value / 2 -> pois two sided são duplicados