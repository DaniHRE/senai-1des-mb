import pandas as pd

d = {
        'Nome':[
            'Danizin', 'Tanã', 'Nayuri'
        ],
        'Idade':[
            '18', '34', '50'
        ]
    }

dados = pd.DataFrame(data=d)
print(dados)
dados.to_excel('dados.xlsx', index=False)
