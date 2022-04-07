ficha = {
    'Nome ': input('Digite o nome da pessoa: '),
    'AnoNasc': int(input('Digite o ano de nascimento: ')),
    'ctps': int(input('Digite a carteira de trabalho: '))
}

if ficha['ctps'] != 0:
    ficha['Ano de contratação'] = int(input('Ano de contr: '))
    ficha['Salário'] = int(input('Salário é: '))
    aposentadoria = 2022 - ficha['AnoNasc'] + (ficha['Ano de contratação'] + 35) - 2022
    ficha['Aposentadoria'] = aposentadoria

for k, v in ficha.items():
    print(f'{k} tem o valor de {v}')
