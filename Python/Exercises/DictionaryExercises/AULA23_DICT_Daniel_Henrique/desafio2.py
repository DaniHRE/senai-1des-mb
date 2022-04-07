from random import randint
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

print("-"*20)
print('Valores sorteados')

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f"{i + 1}º colocado {v[0]} com {v[1]}.")