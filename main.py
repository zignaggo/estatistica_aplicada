import statistics as st
import numpy as np

sync1 = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]) # 22
asyncr1 = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]) # 14

# media = sync1.mean()
# media_2 = asyncr1.mean()
# print("Média: ", media)
# print(f'mediana 1: {np.median(sync1)}')

# print("Média 2: ", media_2)
# print(f'mediana 2: {np.median(asyncr1)}')

# percentil1 = np.percentile(sync1, [ 25, 50, 75 ])
# percentil2 = np.percentile(asyncr1, [ 25, 50, 75 ])
# print("Quartil 1 e 3 do sync1", percentil1)
# print("Quartil 1 e 3 do asyncr1", percentil2)

# print(st.mode(sync1))
# print(st.multimode(asyncr1))

# print('amplitude: ', sync1.ptp())
# print('amplitude2: ', asyncr1.ptp())

# print('variancia sync1: ', sync1.var(ddof=1)) # amostra
# print('variancia asyncr1: ', sync1.var(ddof=0))

# print('variancia2 asyncr1: ', asyncr1.var(ddof=1)) # população
# print('variancia2 asyncr1: ', asyncr1.var(ddof=0))

# print('desvio padrão', sync1.std(ddof=1))
