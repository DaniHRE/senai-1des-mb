jogador = {
    'Nome': str(input('Digite o nome do jogador: '))
}
partidas = list()

total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range(total):
    partidas.append(int(input(f"Quantos gols na partida {i}: ")))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print(jogador)

print('-='*30)
print('O campo nome tem o valor {}'.format(jogador['Nome']))
print('O campo gols tem o valor {}'.format(jogador['Gols']))
print('O campo total tem o valor {}'.format(jogador['Total']))

print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {total} partidas')

for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i}, fez {v} gols')

print(f'Total de {jogador["Total"]} gols')

