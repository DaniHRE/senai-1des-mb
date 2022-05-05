import pandas as pd

data = pd.read_excel('pessoas.xlsx')
nds = pd.DataFrame()

colunas = list(data.columns)

# while True:
for i in colunas:
    nds[i] = [input(f'Digite {i}: ')]

print(nds)


