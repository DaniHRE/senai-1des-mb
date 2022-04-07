count = 0
list = []

for i in range(0, 5):
    num = int(input("Digite um valor: "))
    count += 1
    list.append(num)
    op_usuario = str(input("deseja continuar? [S/N]: ")).strip().upper()

    if op_usuario == "S":
        continue
    elif op_usuario == "N":
        break

new_list = sorted(list)
inverted_list = new_list[::-1]

print(f"Valores invertidos: {inverted_list}")
print(f"Foram digitados: {count} ")

if 5 in inverted_list:
    print(f"O 5 está presente na posição: {inverted_list.index(5)}")
else:
    print("5 não foi encontrado ")
