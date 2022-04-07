matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
maior = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um número [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])
            while matriz[1][coluna]:
                maior.append(matriz[1][coluna])
                break
print('='*30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end="")
    print()

print(f"A soma de todos os pares é igual a: {sum(pares)}")
print(f"A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}")
print(f"O maior numero da segunda linha é: {max(maior)}")