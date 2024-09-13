import pandas as pd
import numpy as np

data = {
    'vendas': [150, 200, 250, 300, 350, 400, 450, 500, 550]
}

df = pd.DataFrame(data)

media_vendas = np.mean(df['vendas'])
mediana_vendas = np.median(df['vendas'])
desvio_padrao_vendas = np.std(df['vendas'])
maximo_vendas = np.max(df['vendas'])
minimo_vendas = np.min(df['vendas'])

print(f'Média: {media_vendas:.2f}')
print(f'Mediana: {mediana_vendas:.2f}')
print(f'Desvio Padrão: {desvio_padrao_vendas:.2f}')
print(f'Máximo: {maximo_vendas:.2f}')
print(f'Mínimo: {minimo_vendas:.2f}')
