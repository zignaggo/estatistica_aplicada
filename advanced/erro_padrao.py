import math
import statistics as st
import numpy as np

"""
Erro padrão 
EP(x) = S / sqrt(n)
"""
def obter_erro_padrao(array: list):
    """
    array: Int[]\n
    """
    
    # como é o calculo do desvio da AMOSTRA ddof=1 é igual ao -1 da formula
    desvio_padrao = np.std(array, ddof=1)
    tamanho_amostra = len(array)
    
    return desvio_padrao / math.sqrt(tamanho_amostra)



## Base de dados
amostra = [41.48, 41.6, 41.72, 41.81, 41.86, 41.95, 42.04, 42.18, 42.26, 42.34]
tamanho_amostra = len(amostra)

## Dados da amostra
desvio_padrao = np.std(amostra, ddof=1)
erro_padrao = obter_erro_padrao(amostra)
media = np.mean(amostra)

## Intervalo para média populacional
intervalo = [media - 3 * erro_padrao, media + 3 * erro_padrao]

## Saída
# print(f"Desvio padrão: {desvio_padrao:.3f}")
# print(f"Erro padrão: {erro_padrao:.3f}")
# print(f"Média: {media:.3f}")
# print(f"Intervalo para média populacional: {intervalo}")

def bootstrap(amostra, n):
    boostrap_medias = []
    for _ in range(n):
        bootstrap_sample = np.random.choice(amostra, size=tamanho_amostra)
        media_bootstrap = bootstrap_sample.mean()
        boostrap_medias.append(media_bootstrap)
    return boostrap_medias

boostrap_medias = bootstrap(amostra, 200)
media_boostrap_medias = np.mean(boostrap_medias)
desvio_boostrap_medias = np.std(boostrap_medias, ddof=1)
# print("Média final", media_boostrap_medias)
# print("Desvio final", desvio_boostrap_medias)

## amostra do tempo de pedidos de emprestimos em horas
amostra_emprestimos = [24.1514, 27.4145, 20.4, 22.5151, 28.5152, 28.5611, 21.2489, 20.9983, 24.984, 22.6245]

## Dados estatísticos
desvio_padrao_emprestimos = np.std(amostra_emprestimos, ddof=1)
erro_padrao_emprestimos = obter_erro_padrao(amostra_emprestimos)
media_emprestimos = np.mean(amostra_emprestimos)
intervalo_emprestimo = [media_emprestimos - 3 * erro_padrao_emprestimos, media_emprestimos + 3 * erro_padrao_emprestimos]
print(f"Intervalo para média populacional: {intervalo_emprestimo}")

## Saída
print(f"Desvio padrão: {desvio_padrao_emprestimos:.3f}")
print(f"Erro padrão: {erro_padrao_emprestimos:.3f}")
print(f"Média: {media_emprestimos:.3f}")
print(f"Intervalo para média populacional: {intervalo_emprestimo}")

boostrap_medias_emprestimo = bootstrap(amostra_emprestimos, 200)
media_boostrap_medias_emprestimo = np.mean(boostrap_medias_emprestimo)
desvio_boostrap_medias_emprestimo = np.std(boostrap_medias_emprestimo, ddof=1)
print("Média final", media_boostrap_medias_emprestimo)
print("Desvio final", desvio_boostrap_medias_emprestimo)