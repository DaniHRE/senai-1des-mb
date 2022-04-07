from random import randint
from time import sleep

jogos_sorteados = [[], [], [], [], []]

for i in range(5, 0, -1):
    for j in range(0, 5):
        numeros = randint(0, 60)
        jogos_sorteados[j].append(numeros)

print("====JOGO DA MEGASENA====")
for k in range(0, 5):
    sleep(1)
    print(f"O {k + 1}º jogo é {jogos_sorteados[k]}")

print("====BOA SORTE====")

