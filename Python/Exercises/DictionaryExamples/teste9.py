estado= dict()
brasil =list()
for i in range(2):
    estado['uf']=input('Unidade Federativa:')
    estado['sigla']=input('Sigla: ')
    brasil.append(estado.copy())
for j in brasil:
    for k in j.values():
        print(f'{k}', end=' ')