"""
1) O que é Regressão Linear?
É a busca por uma relação de variáveis, para estabelecer uma dependencia matemática entre elas.

Em outras palavras é necessário uma função que passa mapear predizer algumas das variáveis suficientemente bem.


2) Elementos
Em uma regressão as variáveis dependentes as respostas(responses) e saídas(outputs) eas variáveis independentes são os regressores(regressors) ou entradas


3) Para que precisamos e uma regressão?
A regressão é necessária sempre que se quiser responder **porque/como** alguns fenomenos influenciam outros ou omo variáveis estão relacionadas


4) Regressão linear
Temos um conjunto de variáveis x={x1, x2, x3} onde né o número de preditores, e y é a resposta.

y = B1 . x1 + B2 . x2 + ... + E

"""
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)
print(model.coef_)
print(model.intercept_)
print(model.intercept_ + model.coef_ + 55)

_y = model.predict(x)
print(_y)
