estado= dict()
brasil =list()
for i in range(2):
    estado['uf']=input('Unidade Federativa:')
    estado['sigla']=input('Sigla: ')
    brasil.append(estado.copy())
print(brasil)