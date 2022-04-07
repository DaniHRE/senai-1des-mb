pessoas = []
cadastradas = 0
peso_list = []

while True:
    name = str(input("Digite o nome para cadastro: "))
    peso = int(input("Digite o peso para cadastro: "))
    cadastradas += 1
    pessoas.append(name)
    pessoas.append(peso)
    peso_list.append(peso)

    op_user = str(input("Deseja continuar: [S/N]")).strip().upper()
    if op_user == "S":
        continue
    elif op_user == "N":
        break

peso_sorted = sorted(peso_list)

print("\n", pessoas)
print(f"Foram cadastradas: {cadastradas} pessoas")
print(f"O maior peso foi: {max(peso_sorted)} ")
print(f"O menor peso foi: {min(peso_sorted)} ")
