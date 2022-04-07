valores = [[], []]

for i in range(0, 7):
    i += 1
    numeros = int(input(f"Digite o {i} número: "))
    if numeros % 2 == 0:
        valores[0].append(numeros)
    else:
        valores[1].append(numeros)

print("Pares: {}".format(valores[0]))
print("Impares: {}".format(valores[1]))
