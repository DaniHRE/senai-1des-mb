import pandas as pd

planilha = pd.read_excel(r'./tables/pessoas.xlsx')

while True:
    print("=" * 30)
    print(planilha)
    print("=" * 30)

    op = input("ID que deseja listar?")

    for x,y in enumerate(planilha['ID']):
        if id == y:
            indice = x
    print(planilha['Nome'][indice])
    print(planilha['Idade'][indice])
    print(planilha['Peso'][indice])
