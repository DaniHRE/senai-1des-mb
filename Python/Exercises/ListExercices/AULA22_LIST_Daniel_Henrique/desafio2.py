list = [10, 20, 30, 40]


while True:
    num = int(input("Digite um número: "))

    if num in list:
        nlist = list.index(num)
        print(f"Esse número já existe na lista e está na posição: {nlist}")

    else:
        list.append(num)
        print('Número adicionado com sucesso!!!')
        new_list = sorted(list)
        print(new_list)
        op_usuario = str(input("Deseja continuar? [S/N]: ")).strip().upper()

        if op_usuario == "S":
            continue
        elif op_usuario == "N":
            break
